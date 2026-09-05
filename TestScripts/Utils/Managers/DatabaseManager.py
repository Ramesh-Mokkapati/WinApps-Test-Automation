# Import Required Libraries
import mysql.connector

from TestScripts.Utils.Managers.FileManager import *

class DatabaseManager:
    """ DatabaseManager, Base Class for handling Database related activities """
    m_DBHost = ""
    m_DBUser = ""
    m_DBPassword = ""
    m_DBName = ""
    m_DataBase = mysql.connector.connect()
    m_FM = FileManager()

    # Initializing
    def __init__(self):
        """ DatabaseManager::Constructor, Assigns the required parameters """
        logging.info("DatabaseManager::DatabaseManager()")
        CF = CommonFunctions()
        self.m_DBHost = CF.GetDBHost()
        logging.debug("DatabaseManager::DatabaseManager() - Host: %s", self.m_DBHost)
        self.m_DBUser = CF.GetDBUserName()
        logging.debug("DatabaseManager::DatabaseManager() - DB User: %s", self.m_DBUser)
        self.m_DBPassword = CF.GetDBPassword()
        logging.debug("DatabaseManager::DatabaseManager() - DB Password: %s", self.m_DBPassword)
        self.m_DBName = CF.GetDBName()
        logging.debug("DatabaseManager::DatabaseManager() - DB Name: %s", self.m_DBName)

    def TruncateTable(self, sTableName):
        """ DatabaseManager::TruncateTable(), Truncates data from the given Table """
        logging.info("DatabaseManager::TruncateTable()")
        self.m_DataBase = mysql.connector.connect(user=self.m_DBUser, password=self.m_DBPassword,
                                                  host=self.m_DBHost, database=self.m_DBName)
        # preparing a cursor object
        cursorObject = self.m_DataBase.cursor()

        sQuery = "TRUNCATE TABLE " + sTableName
        logging.debug("DatabaseManager::TruncateTable() - Query: %s", sQuery)
        cursorObject.execute(sQuery)
        self.m_DataBase.commit()
        cursorObject.close()
        self.m_DataBase.close()

    def DropTable(self, sTableName):
        """ DatabaseManager::DropTable(), Drops a given Table """
        logging.info("DatabaseManager::DropTable()")
        self.m_DataBase = mysql.connector.connect(user=self.m_DBUser, password=self.m_DBPassword,
                                                  host=self.m_DBHost, database=self.m_DBName)
        # preparing a cursor object
        cursorObject = self.m_DataBase.cursor()

        sQuery = "DROP TABLE IF EXISTS " + sTableName
        logging.debug("DatabaseManager::DropTable() - Query: %s", sQuery)
        cursorObject.execute(sQuery)
        self.m_DataBase.commit()
        cursorObject.close()
        self.m_DataBase.close()
