# Import Required Libraries
import filecmp
from abc import ABC, abstractmethod
from TestScripts.Utils.Managers.FileManager import *
from TestScripts.Utils.Base.Test_Config import *


class Test_Base(ABC):
    """Abstract base class for an individual test case."""

    m_FM = FileManager()
    m_CF = CommonFunctions()
    m_Config = Test_Config("", "", "", "")
    m_nImageNumber = 0

    def __init__(self, config):
        logging.info("Test_Base::Test_Base() - Test Base Class")
        self.m_Config = config
        self.m_Config.set_ActualResultFileName(
            self.m_FM.GetTestResultsFolder(self.m_Config.get_ModuleName(), self.m_Config.get_TestID()) +
            self.m_Config.get_TestResultsFileName()
        )
        self.m_Config.set_ExpectedResultFileName(
            self.m_FM.GetExpectedResultsFolder(self.m_Config.get_ModuleName(), self.m_Config.get_TestID()) +
            self.m_Config.get_TestResultsFileName()
        )

    @abstractmethod
    def BeforeTest(self):
        pass

    @abstractmethod
    def RunAutomation(self):
        pass

    @abstractmethod
    def AfterTest(self):
        pass

    def RunTest(self):
        """Execute the test and compare the produced output with expected results."""
        logging.info("Test_Base::RunTest() - Execute the Test")
        self.m_Config.set_TestStartTime(self.m_CF.GetCurrentTime())
        self.m_FM.CleanTestResultsFolder(self.m_Config.get_ModuleName(), self.m_Config.get_TestID())
        self.m_FM.CreateTestResultsFolder(self.m_Config.get_ModuleName(), self.m_Config.get_TestID())
        self.BeforeTest()
        self.RunAutomation()
        self.AfterTest()
        self.PrepareResults()

    def GetTestResults(self):
        return self.m_Config

    def PrepareResults(self):
        logging.info("Test_Base::PrepareResults() - Prepare the Test Results")
        self.m_Config.set_TestEndTime(self.m_CF.GetCurrentTime())
        actualResultFile = self.m_Config.get_ActualResultFileName()
        expectedResultFile = self.m_Config.get_ExpectedResultFileName()
        result = self._compare_results(actualResultFile, expectedResultFile)
        if result:
            self.m_Config.set_TestResult("Passed")
        else:
            self.m_Config.set_TestResult("Failed")

    def _compare_results(self, actualResultFile, expectedResultFile):
        """Compare text files semantically and fall back to binary file comparison."""
        actualExtension = os.path.splitext(actualResultFile)[1].lower()
        expectedExtension = os.path.splitext(expectedResultFile)[1].lower()

        if actualExtension == ".txt" and expectedExtension == ".txt":
            with open(actualResultFile, encoding="utf-8") as actualHandle:
                actualContent = actualHandle.read().replace("\r\n", "\n").strip()
            with open(expectedResultFile, encoding="utf-8") as expectedHandle:
                expectedContent = expectedHandle.read().replace("\r\n", "\n").strip()
            return actualContent == expectedContent

        return filecmp.cmp(actualResultFile, expectedResultFile, shallow=False)

    def TakeScreenshot(self):
        logging.info("Test_Base::TakeScreenshot() - Take a Screenshot")
        self.m_nImageNumber = self.m_nImageNumber + 1
        self.m_FM.TakeScreenshot(
            self.m_Config.get_ModuleName(),
            self.m_Config.get_TestID(),
            self.m_nImageNumber
        )
