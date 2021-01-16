from WPDevEnvCreator.SSHUtility import SSHUtility
from WPDevEnvCreator.Utils.Logger import Logger


class FileDevEnvCreator:
    def __init__(self, config):
        self.config = config
        self.load_configs()
        pass

    def load_configs(self):
        self.ssh_config = self.config['ssh']

        self.directory_config = self.config['directory']
        self.from_dir = self.directory_config['from_dir']
        self.to_dir = self.directory_config['to_dir']
        self.ignore_dirs = self.directory_config['ignore_dirs']

        self.db_config = self.config['database']
        self.old_db_config = self.db_config['old']
        self.new_db_config = self.db_config['new']

    def createFileDevEnv(self):
        ssh_utility = SSHUtility(self.ssh_config['host'], self.ssh_config['user'], self.ssh_config['password'])

        #clean destination
        self.clean_destination(ssh_utility)

        #copy live dir to test
        self.copy_live_env_to_test(ssh_utility)

        #self.replace_db_credentials_in_config(ssh_utility)

        ssh_utility.close()

    def clean_destination(self, ssh_utility):
        ignore_delete_dirs = []
        if "delete_ignore" in self.directory_config:
            ignore_delete_dirs = self.directory_config['delete_ignore']

        delete_cmd = 'rm -r ' + self.to_dir

        for dir in ignore_delete_dirs:
            delete_cmd += " !(" + dir + ") "

        Logger.log(delete_cmd)

        ssh_utility.execute_cmd(delete_cmd)

    def copy_live_env_to_test(self, ssh_utility):
        copy_cmd = "rsync -arv "

        for dir in self.ignore_dirs:
            copy_cmd += "--exclude="+dir

        copy_cmd += " " + self.from_dir + "/* " + self.to_dir

        Logger.log(copy_cmd)

        ssh_utility.execute_cmd(copy_cmd)

    def replace_db_credentials_in_config(self, ssh_utility):
        # search & replace db_data in copied ftp dir
        replace_db_host_cmd = "sed -i 's/" + self.old_db_config['host'] + "/" + \
                              self.new_db_config['host'] + "/g' " + self.to_dir + "/wp-config.php"
        ssh_utility.execute_cmd(replace_db_host_cmd)

        replace_db_name_cmd = "sed -i 's/" + self.old_db_config['name'] + "/" + \
                              self.new_db_config['name'] + "/g' " + self.to_dir + "/wp-config.php"
        ssh_utility.execute_cmd(replace_db_name_cmd)

        replace_db_user_cmd = "sed -i 's/" + self.old_db_config['user'] + "/" + \
                              self.new_db_config['user'] + "/g' " + self.to_dir + "/wp-config.php"
        ssh_utility.execute_cmd(replace_db_user_cmd)

        replace_db_pass_cmd = "sed -i 's/" + self.old_db_config['password'] + "/" + \
                              self.new_db_config['password'] + "/g' " + self.to_dir + "/wp-config.php"
        ssh_utility.execute_cmd(replace_db_pass_cmd)