"""
import pytest
from hamcrest import *
from utils.mysql import MySQLDB

db = MySQLDB()
db_collation = db.get_db_collation()

class TestTable:

	@pytest.mark.parametrize("row", db_collation)
	def test_table_collation(self, row):
		assert_that(row['TABLE_COLLATION'], equal_to('utf8_unicode_ci'), 'table {} has no utf8_unicode_ci collation'.format(row['table_name']))

if __name__ == '__main__':
    pytest.main()
"""


import pytest

from hamcrest import *
from config import ConfigReader as cr
from contextlib import closing
import pymysql.cursors  
 
# Подключиться к базе данных.
connection = pymysql.connect(host=cr('db').get('mysql_host'),
							port=cr('db').get('mysql_port'),
                            user=cr('db').get('mysql_user'),
                            password=cr('db').get('mysql_password'),
                            db=cr('db').get('mysql_dbname'),
                            charset='utf8',
                            use_unicode=True,
                            cursorclass=pymysql.cursors.DictCursor)
connection.autocommit(True)

def collation():
	with closing(connection.cursor()) as cursor:
		sql = "SELECT `table_name`, TABLE_COLLATION FROM `information_schema`.`tables` WHERE `table_schema`=DATABASE() GROUP BY `table_name`;"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result

class TestTable:

	@pytest.mark.parametrize("row", collation())
	def test_table_collation(self, row):
		assert_that(row['TABLE_COLLATION'], equal_to('utf8_unicode_ci'), 'table {} has no utf8_unicode_ci collation'.format(row['table_name']))

if __name__ == '__main__':
    pytest.main()
