# Import Required Libraries
import subprocess
import wmi
import time

from TestScripts.Utils.Managers.CommonFunctions import *

class ProcessManager:
    """ ProcessManager, Class for Managing processes, used in Regression Tests """

    def __init__(self):
        """ ProcessManager::Constructor, Create required objects """
        logging.info("ProcessManager::ProcessManager()")
        self.m_CF = CommonFunctions()
        self.m_Connection = wmi.WMI()

    def CheckProcess(self, process_name):
        """ ProcessManager::CheckProcess(), Checks if a given process is currently running """
        logging.info("ProcessManager::CheckProcess()")
        logging.debug("ProcessManager::CheckProcess() - ProcessName: %s", process_name)
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        # use buildin check_output right away
        output = subprocess.check_output(call).decode()
        # check in last line for process name
        last_line = output.strip().split('\r\n')[-1]
        # because Fail message could be translated
        return last_line.lower().startswith(process_name.lower())

    def InvokeProcess(self, process_name):
        """ ProcessManager::InvokeProcess(), Invokes the given process """
        logging.info("ProcessManager::InvokeProcess()")
        self.TerminateProcess(process_name)
        result = subprocess.Popen(process_name, shell=True, cwd=self.m_CF.GetBinFolder())

    def TerminateProcess(self, process_name):
        """ ProcessManager::TerminateProcess(), Terminates a given process """
        logging.info("ProcessManager::TerminateProcess()")
        # Initializing the wmi object
        for process in self.m_Connection.Win32_Process():
            if process.name == process_name:
                process.Terminate()

    def WaitForProcess(self, process_name):
        """ ProcessManager::WaitForProcess(), Waits for the process to complete its processing, using PollWaitPeriod """
        logging.info("ProcessManager::WaitForProcess()")
        print("ProcessManager::WaitForProcess()")
        time.sleep(self.m_CF.GetTestDelayInSeconds())
        while self.CheckProcess(process_name) != False:
            logging.debug("ProcessManager::WaitForEngine() - Wait for Process : %s", str(self.CheckProcess(process_name)))
            time.sleep(self.m_CF.GetPollWaitPeriod())
