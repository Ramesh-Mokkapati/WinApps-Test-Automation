# Import Required Libraries
import logging

class GlossaryManager:
    """ GlossaryManager, Class for building the Glossary section of the Test Report """

    m_dGlossary = {}

    def __init__(self):
        """ GlossaryManager::Constructor - Populates the glossary dictionary """
        logging.info("GlossaryManager::GlossaryManager()")
        self.AddGlossary()

    def AddGlossary(self):
        """ GlossaryManager::AddGlossary() - Adds all glossary terms """
        logging.info("GlossaryManager::AddGlossary()")
        self.m_dGlossary["Notepad"]    = "A simple Text editor"
        self.m_dGlossary["Calc"]       = "Default Calculator"


    def GetGlossary(self):
        """ GlossaryManager::GetGlossary() - Returns the glossary dictionary """
        logging.info("GlossaryManager::GetGlossary()")
        return self.m_dGlossary
