# Import Required Libraries
import logging

from configparser import ConfigParser

class ConfigManager:
    """ ConfigManager, Base Class for handling Config file """
    m_sConfigFile = " "  # Default value

    def __init__(self, sConfigFile):
        """ ConfigManager::Constructor, Assigns the ConfigFile """
        logging.info("ConfigManager::ConfigManager()")
        logging.debug("ConfigManager::ConfigManager() - ConfigFile: %s", sConfigFile)
        self.set_ConfigFile(sConfigFile)

    def get_ConfigFile(self):
        """ ConfigManager::get_ConfigFile, Returns ConfigFile """
        logging.info("ConfigManager::get_ConfigFile()")
        logging.debug("ConfigManager::get_ConfigFile() - ConfigFile: %s", self.m_sConfigFile)
        return self.m_sConfigFile

    def set_ConfigFile(self, sConfigFile):
        """ ConfigManager::set_ConfigFile, Assigns ConfigFile """
        logging.info("ConfigManager::set_ConfigFile()")
        logging.debug("ConfigManager::set_ConfigFile() - ConfigFile: %s", sConfigFile)
        self.m_sConfigFile = sConfigFile

    def WriteToConfig(self, sSection, sParameter, sValue):
        """ ConfigManager::WriteToConfig, Writes new Section / Parameter to Config.ini """
        logging.info("ConfigManager::WriteToConfig()")
        config = ConfigParser()
        config.read(self.m_sConfigFile)
        if not config.has_section(sSection):
            logging.debug("ConfigManager::WriteToConfig() - Section %s not found, adding it", sSection)
            config.add_section(sSection)

        logging.debug("ConfigManager::WriteToConfig() - Parameter: %s  Value: %s", sParameter, sValue)
        config[sSection][sParameter] = sValue

        with open(self.m_sConfigFile, 'w') as configfile:
            config.write(configfile)
            configfile.close()

    def GetAllSections(self):
        """ ConfigManager::GetAllSections, Returns all Sections from the Config file """
        logging.info("ConfigManager::GetAllSections()")
        config = ConfigParser()
        sections = config.read(self.m_sConfigFile)
        logging.debug("ConfigManager::GetAllSections() - Sections: %s", sections)
        return sections

    def GetValue(self, sSection, sKey):
        """ ConfigManager::GetValue, Returns parameter value for a given Section and Key """
        logging.info("ConfigManager::GetValue()")
        config = ConfigParser()
        config.read(self.m_sConfigFile)
        logging.debug("ConfigManager::GetValue() - Section: %s  Key: %s  Value: %s",
                      sSection, sKey, config.get(sSection, sKey))
        return config.get(sSection, sKey)
