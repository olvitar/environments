import os
import re
import yaml

from utils.project_utils import ProjectUtils


class ConfigReader:
    '''
    Config Reader provides a singleton instance of ConfigReader for looking up 
    values for config variables.
    '''

    CONFIG_LOCATION = 'configs/'
    DEFAULT_CONFIG_FILE = 'default'
    CONFIG_EXT = '.yaml'

    ENV_VARS = "WTF_ENV"
    ENV_PREFIX = "WTF_"

    _dataMaps = None  # instance variable to store config data loaded.
    _singleton_instance = None  # class variable to track singleton.

    def __init__(self, _env_var_=None):
        self._dataMaps = []

        # load default yaml file if this is not a unit test.
        try:
            if _env_var_ != None:
                # We pass in a custom env var for unit testing.
                configs = re.split(",|;", _env_var_)
                for config in reversed(configs):
                    self.__load_config_file(config)
            elif not ConfigReader.ENV_VARS in os.environ:
                # print("Config file not specified.  Using config/defaults.yaml")
                self.__load_config_file(ConfigReader.DEFAULT_CONFIG_FILE)
            else:
                # Read and load in all configs specified in reverse order
                configs = re.split(",|;", str(os.environ[ConfigReader.ENV_VARS]))
                for config in reversed(configs):
                    self.__load_config_file(config)


        except Exception as e:
            # Fall back to default.yaml file when no config settings are specified.
            print("An error occurred while loading config file:", e)
            raise e

    class __NoDefaultSpecified__(object):
        "No default specified to config reader."
        pass

    def get(self, key, default_value=__NoDefaultSpecified__):
        '''
        Gets the value from the yaml config based on the key.

        No type casting is performed, any type casting should be 
        performed by the caller.

        @param key: Name of the config you wish to retrieve.  
        @type key: str
        @param default_value: Value to return if the config setting does not exist. 
        '''
        # First attempt to get the var from OS enviornment.
        os_env_string = ConfigReader.ENV_PREFIX + key
        os_env_string = os_env_string.replace(".", "_")
        if type(os.getenv(os_env_string)) != type(None):
            return os.getenv(os_env_string)

        # Otherwise search through config files.
        for data_map in self._dataMaps:
            try:
                if "." in key:
                    # this is a multi levl string
                    namespaces = key.split(".")
                    temp_var = data_map
                    for name in namespaces:
                        temp_var = temp_var[name]
                    return temp_var
                else:
                    value = data_map[key]
                    return value
            except (AttributeError, TypeError, KeyError):
                pass

        if default_value == self.__NoDefaultSpecified__:
            raise KeyError("Key '{0}' does not exist".format(key))
        else:
            return default_value

    def __load_config_file(self, file_name):
        try:
            config_file_location = os.path.join(ProjectUtils.get_project_root() +
                                                ConfigReader.CONFIG_LOCATION +
                                                file_name +
                                                ConfigReader.CONFIG_EXT)
            # print "locating config file:", config_file_location
            config_yaml = open(config_file_location, 'r')
            dataMap = yaml.load(config_yaml, Loader=yaml.FullLoader)
            self._dataMaps.insert(0, dataMap)
            config_yaml.close()
        except Exception as e:
            print("Error loading config file " + file_name)
            raise ConfigFileReadError("Error reading config file " + file_name, e)


class ConfigFileReadError(RuntimeError):
    """
    Raised when a config file is not found.
    """
    pass