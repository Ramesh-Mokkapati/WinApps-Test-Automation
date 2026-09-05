# Import Required Libraries
import re
from pywinauto.keyboard import send_keys
from TestScripts.Utils.Base.WindowsApp_Test_Base import *
from TestScripts.Utils.Managers.WindowManager import *


class WIN_APPS_002(WindowsApp_Test_Base):
    """Calculator test: perform 7 + 6 + 7 and verify the result is 20."""

    m_sTestDescription = "Calculator - Verify basic addition: 7 + 6 + 7 = 20"
    m_sTestResultFileName = "TestResult.txt"

    def __init__(self, sModuleName):
        logging.info("WIN_APPS_002::WIN_APPS_002()")
        self.m_sTestID = type(self).__name__
        self.m_sModuleName = sModuleName
        config = Test_Config(
            self.m_sModuleName,
            self.m_sTestID,
            self.m_sTestDescription,
            self.m_sTestResultFileName
        )
        super(WIN_APPS_002, self).__init__(config)

    def BeforeTest(self):
        logging.info("WIN_APPS_002::BeforeTest()")

    def RunAutomation(self):
        logging.info("WIN_APPS_002::RunAutomation()")
        window = WindowManager.LaunchAndFindWindowForProfile(
            "calc.exe",
            WindowManager.PROFILE_CALCULATOR
        )
        window.set_focus()

        time.sleep(1)
        send_keys("%1")
        time.sleep(0.5)
        send_keys("{ESC}")
        send_keys("7{+}6{+}7=")
        time.sleep(1)

        self.TakeScreenshot()

        resultControl = window.child_window(auto_id="CalculatorResults", control_type="Text")
        resultControl.wait("ready", timeout=10)
        rawDisplay = resultControl.wrapper_object().window_text()
        normalizedResult = re.sub(r"[^0-9.-]", "", rawDisplay)

        with open(self.m_Config.get_ActualResultFileName(), "w", encoding="utf-8") as resultFile:
            resultFile.write(normalizedResult)

        window.close()

    def AfterTest(self):
        logging.info("WIN_APPS_002::AfterTest()")