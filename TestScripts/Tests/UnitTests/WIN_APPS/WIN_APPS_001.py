# Import Required Libraries
from pywinauto.clipboard import GetData
from pywinauto.keyboard import send_keys

from TestScripts.Utils.Base.WindowsApp_Test_Base import *
from TestScripts.Utils.Managers.WindowManager import *


TEST_TEXT = "Hello World! This is an Automated Test."


class WIN_APPS_001(WindowsApp_Test_Base):
    """Notepad test: type text and verify the editor contains it."""

    m_sTestDescription = "Notepad - Verify text can be typed and retrieved from the editor"
    m_sTestResultFileName = "TestResult.txt"

    def __init__(self, sModuleName):
        logging.info("WIN_APPS_001::WIN_APPS_001()")
        self.m_sTestID = type(self).__name__
        self.m_sModuleName = sModuleName
        config = Test_Config(
            self.m_sModuleName,
            self.m_sTestID,
            self.m_sTestDescription,
            self.m_sTestResultFileName
        )
        super(WIN_APPS_001, self).__init__(config)

    def BeforeTest(self):
        logging.info("WIN_APPS_001::BeforeTest()")

    def RunAutomation(self):
        logging.info("WIN_APPS_001::RunAutomation()")
        window = WindowManager.LaunchAndFindWindowForProfile(
            "notepad.exe",
            WindowManager.PROFILE_NOTEPAD
        )

        document = window.child_window(control_type="Document")
        document.wait("ready", timeout=10)
        documentWrapper = document.wrapper_object()
        documentWrapper.click_input()
        send_keys("^a{BACKSPACE}")
        send_keys(TEST_TEXT, with_spaces=True)
        time.sleep(1)

        self.TakeScreenshot()

        send_keys("^a^c")
        time.sleep(1)
        actualText = GetData()
        with open(self.m_Config.get_ActualResultFileName(), "w", encoding="utf-8") as resultFile:
            resultFile.write(actualText)

        window.close()
        time.sleep(2)
        for candidate in Desktop(backend="uia").windows(visible_only=True):
            try:
                buttons = candidate.descendants(control_type="Button")
                for button in buttons:
                    text = button.window_text()
                    if text and ("save" in text.lower()) and ("don't" in text.lower() or "dont" in text.lower()):
                        button.click()
                        return
            except Exception:
                continue

    def AfterTest(self):
        logging.info("WIN_APPS_001::AfterTest()")