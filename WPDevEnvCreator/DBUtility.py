#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pipes

from WPDevEnvCreator.Utils.Logger import Logger


class DBUtility():
    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name
        pass

    def clear_db(self, db_host, db_name, db_user, db_password):
        SQL_FILE_PATH = os.path.join(self.path, self.file_name)+".sql"

        try:
            os.stat(self.path)
        except:
            os.makedirs(self.path)

        Logger.log("Clearing destination database " + db_name, "DBUtility")

        auth_data = "-h " + db_host + " -u " + db_user + " -p" + db_password + " " + db_name

        del_cmd1 = "mysqldump -d -h " + db_host + " -u " + db_user + " -p" + db_password + " --add-drop-table " + db_name + " > " + pipes.quote(SQL_FILE_PATH)
        os.system(del_cmd1)
        del_cmd2 = "mysql " + auth_data + " < " + pipes.quote(SQL_FILE_PATH)
        os.system(del_cmd2)

        #self.clean_up()

    def download_db(self, db_host, db_name, db_user, db_password):
        SQL_FILE_PATH = os.path.join(self.path, self.file_name)+".sql"

        try:
            os.stat(self.path)
        except:
            os.makedirs(self.path)

        Logger.log("Starting download of database " + db_name, "DBUtility")

        auth_data = "-h " + db_host + " -u " + db_user + " -p" + db_password + " " + db_name

        dumpcmd = "sudo mysqldump " + auth_data + " > " + pipes.quote(SQL_FILE_PATH)

        Logger.log(dumpcmd, "DBUtility")

        os.system(dumpcmd)

    def replace_in_db(self, search, replace):
        SQL_FILE_PATH = os.path.join(self.path, self.file_name) + ".sql"

        with open(SQL_FILE_PATH, 'r') as file:
            filedata = file.read()

        filedata = filedata.replace(search, replace)

        with open(SQL_FILE_PATH, 'w') as file:
            file.write(filedata)

    def upload_db(self, db_host, db_name, db_user, db_password):
        SQL_FILE_PATH = os.path.join(self.path, self.file_name) + ".sql"

        # Checking if backup folder already exists or not. If not exists will create it.
        try:
            os.stat(self.path)
        except:
            os.makedirs(self.path)

        Logger.log("Starting upload of database " + db_name, "DBUtility")

        auth_data = "-h " + db_host + " -u " + db_user + " -p" + db_password + " " + db_name

        upload_cmd = "sudo mysql " + auth_data + " < " + pipes.quote(SQL_FILE_PATH)

        Logger.log(upload_cmd, "DBUtility")

        os.system(upload_cmd)

    def clean_up(self):
        SQL_FILE_PATH = os.path.join(self.path, self.file_name) + ".sql"
        os.remove(SQL_FILE_PATH)

    def run_command(self, db_host, db_name, db_user, db_password, command):
        auth_data = "-h " + db_host + " -u " + db_user + " -p" + db_password + " " + db_name

        dumpcmd = "sudo mysql " + auth_data + " --execute=\""+command+"\""

        Logger.log(dumpcmd, "DBUtility")

        os.system(dumpcmd)

    def run_commands(self, db_host, db_name, db_user, db_password, commands):
        for command in commands:
            self.run_command(db_host, db_name, db_user, db_password, command)