# Import Required Libraries
import os
import socket
from datetime import datetime
from TestScripts.Utils.Managers.ConfigManager import *

class CommonFunctions:
    """ CommonFunctions, Base Class for Common Functions used by the Test Framework """

    m_UserName = ""
    m_Password = ""
    m_BinFolder = ""
    m_sConfigFile = ""

    def __init__(self):
        """ CommonFunctions::Constructor - Reads common parameters from Config.ini """
        logging.info("CommonFunctions::CommonFunctions()")
        sConfigFile = os.path.abspath(os.path.join("Conf", "Config.ini"))
        logging.debug("CommonFunctions::CommonFunctions() - Config File: %s", sConfigFile)
        self.m_Config = ConfigManager(sConfigFile)
        self.m_UserName = self.GetUserName()
        self.m_Password = self.GetPassword()
        self.m_BinFolder = self.GetBinFolder()

    def GetUserName(self):
        """ CommonFunctions::GetUserName() - Retrieve UserName from Config file """
        logging.info("CommonFunctions::GetUserName()")
        return self.m_Config.GetValue("Credentials", "UserName")

    def GetPassword(self):
        """ CommonFunctions::GetPassword() - Retrieve Password from Config file """
        logging.info("CommonFunctions::GetPassword()")
        return self.m_Config.GetValue("Credentials", "Password")

    def GetBinFolder(self):
        """ CommonFunctions::GetBinFolder() - Retrieve BinFolder from Config file """
        logging.info("CommonFunctions::GetBinFolder()")
        return self.m_Config.GetValue("Deployment", "BinFolder")

    def GetDBUserName(self):
        """ CommonFunctions::GetDBUserName() - Retrieve DBUser from Config file """
        logging.info("CommonFunctions::GetDBUserName()")
        return self.m_Config.GetValue("Database", "DBUser")

    def GetDBPassword(self):
        """ CommonFunctions::GetDBPassword() - Retrieve DBPassword from Config file """
        logging.info("CommonFunctions::GetDBPassword()")
        return self.m_Config.GetValue("Database", "DBPassword")

    def GetDBHost(self):
        """ CommonFunctions::GetDBHost() - Retrieve DBHost from Config file """
        logging.info("CommonFunctions::GetDBHost()")
        return self.m_Config.GetValue("Database", "DBHost")

    def GetDBName(self):
        """ CommonFunctions::GetDBName() - Retrieve DBName from Config file """
        logging.info("CommonFunctions::GetDBName()")
        return self.m_Config.GetValue("Database", "DBName")

    def GetTestDelayInSeconds(self):
        """ CommonFunctions::GetTestDelayInSeconds() - Retrieve TestDelayInSeconds from Config file """
        logging.info("CommonFunctions::GetTestDelayInSeconds()")
        return int(self.m_Config.GetValue("TestConf", "TestDelayInSeconds"))

    def GetLogsInReport(self):
        """ CommonFunctions::GetLogsInReport() - Retrieve Logs flag from Config file """
        logging.info("CommonFunctions::GetLogsInReport()")
        return int(self.m_Config.GetValue("ReportGeneration", "Logs"))

    def GetExpectedResultsInReport(self):
        """ CommonFunctions::GetExpectedResultsInReport() - Retrieve ExpectedResults flag from Config file """
        logging.info("CommonFunctions::GetExpectedResultsInReport()")
        return int(self.m_Config.GetValue("ReportGeneration", "ExpectedResults"))

    def GetActualResultsInReport(self):
        """ CommonFunctions::GetActualResultsInReport() - Retrieve ActualResults flag from Config file """
        logging.info("CommonFunctions::GetActualResultsInReport()")
        return int(self.m_Config.GetValue("ReportGeneration", "ActualResults"))

    def GetScreenshotsInReport(self):
        """ CommonFunctions::GetScreenshotsInReport() - Retrieve Screenshots flag from Config file """
        logging.info("CommonFunctions::GetScreenshotsInReport()")
        return int(self.m_Config.GetValue("ReportGeneration", "Screenshots"))

    def GetVersionInfoInReport(self):
        """ CommonFunctions::GetVersionInfoInReport() - Retrieve VersionInfo flag from Config file """
        logging.info("CommonFunctions::GetVersionInfoInReport()")
        return int(self.m_Config.GetValue("ReportGeneration", "VersionInfo"))

    def GetPollWaitPeriod(self):
        """ CommonFunctions::GetPollWaitPeriod() - Retrieve PollWaitPeriod from Config file """
        logging.info("CommonFunctions::GetPollWaitPeriod()")
        return int(self.m_Config.GetValue("TestConfig", "PollWaitPeriod"))

    def GetUnitTests(self):
        """ CommonFunctions::GetUnitTests() - Retrieve UnitTests flag from Config file """
        logging.info("CommonFunctions::GetUnitTests()")
        return int(self.m_Config.GetValue("TestConfig", "UnitTests"))

    def GetGlossaryInReport(self):
        """ CommonFunctions::GetGlossaryInReport() - Retrieve Glossary flag from Config file """
        logging.info("CommonFunctions::GetGlossaryInReport()")
        return int(self.m_Config.GetValue("ReportGeneration", "Glossary"))

    def GetPDFGenerationInReport(self):
        """ CommonFunctions::GetPDFGenerationInReport() - Retrieve PDFReport flag from Config file """
        logging.info("CommonFunctions::GetPDFGenerationInReport()")
        return int(self.m_Config.GetValue("ReportGeneration", "PDFReport"))

    def GetCurrentTime(self):
        """ CommonFunctions::GetCurrentTime() - Returns the current time as a formatted string """
        logging.info("CommonFunctions::GetCurrentTime()")
        t = datetime.now()
        sCurrentTime = (str(t.day)  + "-" + str(t.month) + "-" + str(t.year) + " " +
                        str(t.hour) + ":" + str(t.minute) + ":" + str(t.second))
        logging.debug("CommonFunctions::GetCurrentTime() - CurrentTime: %s", sCurrentTime)
        return sCurrentTime

    def GetCurrentSystemFQDN(self):
        """ CommonFunctions::GetCurrentSystemFQDN() - Returns the fully-qualified domain name """
        logging.info("CommonFunctions::GetCurrentSystemFQDN()")
        sFQDN = socket.getfqdn()
        logging.debug("CommonFunctions::GetCurrentSystemFQDN() - FQDN: %s", sFQDN)
        return sFQDN

    def GetCurrentIPAddress(self):
        """ CommonFunctions::GetCurrentIPAddress() - Returns the current system's IP address """
        logging.info("CommonFunctions::GetCurrentIPAddress()")
        sIPAddress = socket.gethostbyname(socket.gethostname())
        logging.debug("CommonFunctions::GetCurrentIPAddress() - IPAddress: %s", sIPAddress)
        return sIPAddress
