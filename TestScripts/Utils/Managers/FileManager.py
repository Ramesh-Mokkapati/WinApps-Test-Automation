# Import Required Libraries
import shutil
import time

from PIL import ImageGrab
from pathlib import Path
from TestScripts.Utils.Managers.CommonFunctions import *

class FileManager:
    """ FileManager, Class for handling File & Folder related activities """

    m_sTestResultsFolder = ""
    m_sExpectedResultsFolder = ""

    def __init__(self):
        """ FileManager::Constructor - Assigns folder paths """
        logging.info("FileManager::FileManager()")
        self.m_sTestResultsFolder = os.getcwd() + "/TestResults/"
        logging.debug("FileManager::FileManager() - TestResultsFolder: %s", self.m_sTestResultsFolder)

        self.m_sExpectedResultsFolder = os.getcwd() + "/ExpectedResults/"
        logging.debug("FileManager::FileManager() - ExpectedResultsFolder: %s", self.m_sExpectedResultsFolder)

    def __CreateFolder(self, sFolder):
        """ FileManager::__CreateFolder() - Creates a folder if it does not already exist """
        logging.info("FileManager::__CreateFolder()")
        sFolderName = os.getcwd() + sFolder
        logging.debug("FileManager::__CreateFolder() - FolderName: %s", sFolderName)
        if not os.path.exists(sFolderName):
            os.makedirs(sFolderName)

    def CreateTestResults(self):
        """ FileManager::CreateTestResults() - Creates the top-level TestResults folder """
        logging.info("FileManager::CreateTestResults()")
        self.__CreateFolder('\\TestResults\\')

    def CreateTestResults(self, sModuleName):
        """ FileManager::CreateTestResults() - Creates a TestResults sub-folder for a module """
        logging.info("FileManager::CreateTestResults()")
        logging.debug("FileManager::CreateTestResults() - ModuleName: %s", sModuleName)
        self.__CreateFolder('\\TestResults\\' + sModuleName + "\\")

    def CreateTestResultsFolder(self, sModuleName, sTestID):
        """ FileManager::CreateTestResultsFolder() - Creates the per-test results folder """
        logging.info("FileManager::CreateTestResultsFolder()")
        sFolderName = '\\TestResults\\' + sModuleName + "\\" + sTestID
        logging.debug("FileManager::CreateTestResultsFolder() - FolderName: %s", sFolderName)
        self.__CreateFolder(sFolderName)

    def CleanTestResultsFolder(self, sModuleName, sTestID):
        """ FileManager::CleanTestResultsFolder() - Removes the per-test results folder """
        logging.info("FileManager::CleanTestResultsFolder()")
        dirpath = Path(self.m_sTestResultsFolder) / sModuleName / sTestID
        logging.debug("FileManager::CleanTestResultsFolder() - Target Folder: %s", dirpath)
        if dirpath.exists() and dirpath.is_dir():
            shutil.rmtree(dirpath)

    def GetTestResultsFolder(self, sModuleName, sTestID):
        """ FileManager::GetTestResultsFolder() - Returns the path for a module/test results folder """
        logging.info("FileManager::GetTestResultsFolder()")
        sFolderName = self.m_sTestResultsFolder + "//" + sModuleName + "//" + sTestID + "//"
        logging.debug("FileManager::GetTestResultsFolder() - TestResultsFolder: %s", sFolderName)
        return sFolderName

    def GetExpectedResultsFolder(self, sModuleName, sTestID):
        """ FileManager::GetExpectedResultsFolder() - Returns the path for a module/test expected results folder """
        logging.info("FileManager::GetExpectedResultsFolder()")
        sFolderName = self.m_sExpectedResultsFolder + "//" + sModuleName + "//" + sTestID + "//"
        logging.debug("FileManager::GetExpectedResultsFolder() - ExpectedResultsFolder: %s", sFolderName)
        return sFolderName

    def TakeScreenshot(self, sModuleName, sTestID, nImageNumber):
        """ FileManager::TakeScreenshot() - Captures a full-screen screenshot and saves it as a JPEG """
        logging.info("FileManager::TakeScreenshot()")
        time.sleep(1)
        sImageName = (self.GetTestResultsFolder(sModuleName, sTestID) +
                      sTestID + "_Snapshot_" + str(nImageNumber).zfill(3) + ".jpg")
        logging.debug("FileManager::TakeScreenshot() - Image: %s", sImageName)
        snapshot = ImageGrab.grab()
        snapshot.save(sImageName)

    def __GetNumberOfFilesFromFolder(self, sFolderName):
        """ FileManager::__GetNumberOfFilesFromFolder() - Counts files in a given folder """
        logging.info("FileManager::__GetNumberOfFilesFromFolder()")
        nFileCount = sum(
            1 for path in os.listdir(sFolderName)
            if os.path.isfile(os.path.join(sFolderName, path))
        )
        logging.debug("FileManager::__GetNumberOfFilesFromFolder() - Folder %s has %s files",
                      sFolderName, nFileCount)
        return nFileCount
