# Import Required Libraries
from abc import ABC
from TestScripts.Utils.Managers.FileManager import *

class TestManager(ABC):
    """Base class for a test manager that owns a collection of tests."""

    m_nTestDelayInSeconds = 0
    m_TestResults = []
    m_Tests = []
    m_FM = FileManager()

    def __init__(self):
        logging.info("TestManager::TestManager() - Test Manager (Base Class)")
        cf = CommonFunctions()
        self.m_nTestDelayInSeconds = cf.GetTestDelayInSeconds()
        self.m_TestResults = []
        self.m_Tests = []

    def PrepareTests(self):
        logging.info("TestManager::PrepareTests() - Add Individual Test Cases in Derived Class")

    def AddTest(self, testObject):
        logging.info("TestManager::AddTest() - Adding Test %s", testObject.m_sTestID)
        if testObject not in self.m_Tests:
            self.m_Tests.append(testObject)

    def RunTests(self):
        logging.info("TestManager::RunTests() - Execute all Tests")
        for test in self.m_Tests:
            logging.info("TestManager::RunTests() - Executing Test %s", test.m_sTestID)
            print("Running Test: " + test.m_sTestID)
            time.sleep(self.m_nTestDelayInSeconds)
            test.RunTest()

    def GetTestResults(self):
        logging.info("TestManager::GetTestResults() - Retrieve All Executed Test Results")
        self.m_TestResults = []
        for test in self.m_Tests:
            self.m_TestResults.append(test.GetTestResults())
        return self.m_TestResults
