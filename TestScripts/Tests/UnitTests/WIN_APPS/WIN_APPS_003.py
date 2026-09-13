# encoding: utf-8

# Import Required Libraries
import os
import time
import logging
import winreg
import subprocess
from pywinauto import Application
from pywinauto.keyboard import send_keys
from TestScripts.Utils.Base.WindowsApp_Test_Base import *
from TestScripts.Utils.Managers.WindowManager import *


class WIN_APPS_003(WindowsApp_Test_Base):
    """System Properties test: Add a new user environment variable ('TestApp' = 'NewValue')."""

    m_sTestDescription = "System Properties - Add new user environment variable TestApp=NewValue"
    m_sTestResultFileName = "TestResult.txt"

    def __init__(self, sModuleName):
        logging.info("WIN_APPS_003::WIN_APPS_003()")
        self.m_sTestID = type(self).__name__
        self.m_sModuleName = sModuleName
        config = Test_Config(
            self.m_sModuleName,
            self.m_sTestID,
            self.m_sTestDescription,
            self.m_sTestResultFileName
        )
        super(WIN_APPS_003, self).__init__(config)

    def BeforeTest(self):
        logging.info("WIN_APPS_003::BeforeTest()")

    def RunAutomation(self):
        logging.info("WIN_APPS_003::RunAutomation()")

        # 1. Launch Environment Variables dialog directly
        proc = subprocess.Popen(["rundll32.exe", "sysdm.cpl,EditEnvironmentVariables"])
        time.sleep(2)

        # 2. Attach PyWinAuto application directly to the launched process ID
        app = Application(backend="win32").connect(process=proc.pid)
        env_dlg = app.window(title="Environment Variables")
        env_dlg.wait("visible", timeout=5)
        env_dlg.set_focus()
        time.sleep(1)

        # 3. Trigger "New..." User Variable dialog using hotkey (Alt+N)
        send_keys("%n")
        time.sleep(1)

        # 4. Attach to the "New User Variable" dialog
        new_var_dlg = app.window(title="New User Variable")
        new_var_dlg.wait("visible", timeout=5)
        new_var_dlg.set_focus()

        # 5. Populate fields: Variable name -> Tab -> Variable value
        target_var_name = "TestApp"
        expected_var_value = "NewValue"
        send_keys(f"{target_var_name}{{TAB}}{expected_var_value}")
        time.sleep(1)
        self.TakeScreenshot()

        # 6. Confirm and close open dialogs using keyboard Enter sequences
        send_keys("{ENTER}")  # Close "New User Variable" dialog (OK)
        time.sleep(0.5)


        env_dlg.set_focus()
        send_keys("{ENTER}")  # Close "Environment Variables" dialog (OK)
        time.sleep(0.5)


        # -----------------------------------------------------------------
        # TEST RESULTS AREA
        # -----------------------------------------------------------------
        # Read the environment variable directly from the Windows Registry
        actual_value = os.environ.get(target_var_name)

        if actual_value is None:
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_READ) as key:
                    actual_value, _ = winreg.QueryValueEx(key, target_var_name)
            except FileNotFoundError:
                actual_value = "NOT_FOUND"

        # Format as complete variable details: "KEY=VALUE"
        full_variable_detail = f"{target_var_name}={actual_value}"

        # Write actual result formatted as "TestApp=NewValue"
        with open(self.m_Config.get_ActualResultFileName(), "w", encoding="utf-8") as resultFile:
            resultFile.write(full_variable_detail)

    def AfterTest(self):
        logging.info("WIN_APPS_003::AfterTest()")