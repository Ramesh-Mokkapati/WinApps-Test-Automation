# Import Required Libraries
from TestScripts.Tests.UnitTests.WIN_APPS.WIN_APPS_TestManager import *


class UnitTestsManager(TestManager):
    """Top-level manager for unit tests."""

    def __init__(self):
        logging.info("UnitTestsManager::UnitTestsManager()")
        super().__init__()
        self.m_WinAppsMgr = WIN_APPS_TestManager()

    def RunTests(self):
        self.m_WinAppsMgr.RunTests()

    def GetTestResults(self):
        return self.m_WinAppsMgr.GetTestResults()
