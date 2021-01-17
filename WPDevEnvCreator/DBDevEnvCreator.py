from WPDevEnvCreator.DBUtility import DBUtility


class DBDevEnvCreator:
    def __init__(self, config, temp_path):
        self.config = config
        self.temp_path = temp_path
        self.db_utility = DBUtility(self.temp_path, 'temp_db')
        self.temp_path = temp_path
        pass

    def createDBDevEnv(self):
        domain_config = self.config['domains']
        db_config = self.config['database']

        table_prefix = db_config['table_prefix']
        old_db_config = db_config['old']
        new_db_config = db_config['new']

        old_domain = domain_config['from']
        new_domain = domain_config['to']

        self.db_utility.clear_db(new_db_config['host'], new_db_config['name'], new_db_config['user'], new_db_config['password'])

        self.db_utility.download_db(old_db_config['host'], old_db_config['name'], old_db_config['user'], old_db_config['password'])

        self.db_utility.replace_in_db(old_domain, new_domain)

        self.db_utility.replace_in_db(old_db_config['name'], new_db_config['name'])

        self.db_utility.upload_db(new_db_config['host'], new_db_config['name'], new_db_config['user'], new_db_config['password'])

        # set options in db
        self.db_utility.set_no_index(new_db_config['host'], new_db_config['name'], new_db_config['user'], new_db_config['password'], table_prefix)

        #delete downloaded db file
        self.db_utility.clean_up()

        pass