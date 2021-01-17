from WPDevEnvCreator.DBDevEnvCreator import DBDevEnvCreator
from WPDevEnvCreator.FileDevEnvCreator import FileDevEnvCreator
from WPDevEnvCreator.Utils.Logger import Logger


class WPDevEnvCreator:
    def __init__(self, config, temp_dir):
        self.config = config
        self.db_dev_env_creator = DBDevEnvCreator(config, temp_dir)
        self.file_dev_env_creator = FileDevEnvCreator(config)

    def createDevEnv(self):
        self.db_dev_env_creator.createDBDevEnv()
        #self.file_dev_env_creator.createFileDevEnv()
        return
