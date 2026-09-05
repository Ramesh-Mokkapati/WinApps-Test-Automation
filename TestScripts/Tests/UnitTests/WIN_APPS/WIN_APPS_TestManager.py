# Import Required Libraries
from TestScripts.Utils.Base.TestManager import *
from TestScripts.Tests.UnitTests.WIN_APPS.WIN_APPS_001 import *
from TestScripts.Tests.UnitTests.WIN_APPS.WIN_APPS_002 import *


class WIN_APPS_TestManager(TestManager):
    """Manager for Windows application tests."""

    def __init__(self):
        logging.info("WIN_APPS_TestManager::WIN_APPS_TestManager()")
        super().__init__()
        self.m_sModuleName = "WIN_APPS"
        self.m_FM.CreateTestResults(self.m_sModuleName)
        self.PrepareTests()

    def PrepareTests(self):
        logging.info("WIN_APPS_TestManager::PrepareTests()")
        self.AddTest(WIN_APPS_001(self.m_sModuleName))
        self.AddTest(WIN_APPS_002(self.m_sModuleName))
