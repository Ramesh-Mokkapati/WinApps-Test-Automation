# Import Required Libraries
import logging


class Test_Config:
    """Stores metadata and file paths for a single test case."""

    m_sModuleName = ""
    m_sTestID = ""
    m_sTestDescription = ""
    m_sTestResultFileName = ""
    m_sTestStartTime = ""
    m_sTestEndTime = ""
    m_sTestResult = ""
    m_sActualResultFileName = ""
    m_sExpectedResultFileName = ""

    def __init__(self, sModuleName, sTestID, sTestDescription, sTestResultFileName):
        logging.info("Test_Config::Test_Config() - Test Config Base Class")
        self.m_sModuleName = sModuleName
        self.m_sTestID = sTestID
        self.m_sTestDescription = sTestDescription
        self.m_sTestResultFileName = sTestResultFileName

    def get_ModuleName(self):
        return self.m_sModuleName

    def set_ModuleName(self, sModuleName):
        self.m_sModuleName = sModuleName

    def get_TestID(self):
        return self.m_sTestID

    def set_TestID(self, sTestID):
        self.m_sTestID = sTestID

    def get_TestDescription(self):
        return self.m_sTestDescription

    def set_TestDescription(self, sTestDescription):
        self.m_sTestDescription = sTestDescription

    def get_TestResultsFileName(self):
        return self.m_sTestResultFileName

    def set_TestResultsFileName(self, sTestResultsFileName):
        self.m_sTestResultFileName = sTestResultsFileName

    def get_TestStartTime(self):
        return self.m_sTestStartTime

    def set_TestStartTime(self, sTestStartTime):
        self.m_sTestStartTime = sTestStartTime

    def get_TestEndTime(self):
        return self.m_sTestEndTime

    def set_TestEndTime(self, sTestEndTime):
        self.m_sTestEndTime = sTestEndTime

    def get_TestResult(self):
        return self.m_sTestResult

    def set_TestResult(self, sTestResult):
        self.m_sTestResult = sTestResult

    def get_ActualResultFileName(self):
        return self.m_sActualResultFileName

    def set_ActualResultFileName(self, sActualResultFileName):
        self.m_sActualResultFileName = sActualResultFileName

    def get_ExpectedResultFileName(self):
        return self.m_sExpectedResultFileName

    def set_ExpectedResultFileName(self, sExpectedResultFileName):
        self.m_sExpectedResultFileName = sExpectedResultFileName
