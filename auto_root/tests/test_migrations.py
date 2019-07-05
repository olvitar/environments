# from config import ConfigReader
# from utils.cli_utils import run_console_command
#
#
# class TestMigrations:
#     def test_migrate_up(self):
#         _config_db = ConfigReader('db')
#         _config_url = ConfigReader('urls')
#         run_console_command('''
#         mysql -u {username} -p'{password}' -h {host} <<-EOF
#             drop database {db_name};
#             create database {db_name};
#         EOF
#             '''.format(username=_config_db.get('mysql_user'), password=_config_db.get('mysql_password'),
#                        host=_config_db.get('mysql_host'), db_name=_config_db.get('mysql_dbname')))
#         run_console_command(
#             "mysql -u {username} -p'{password}' -h {host} {db_name} < {analytics_home}/migrations/db-structure.sql".format(
#                 username=_config_db.get('mysql_user'), password=_config_db.get('mysql_password'),
#                 host=_config_db.get('mysql_host'), db_name=_config_db.get('mysql_dbname'),
#                 analytics_home=_config_db.get('mysql_dbname')))
#         run_console_command('export USE_OSC_MIGRATION=false')
#         run_console_command('{0}/yii migrate --migrationPath=@yii/rbac/migrations --interactive=0'.format(
#             _config_url.get('analytics_home')))
#         pass
