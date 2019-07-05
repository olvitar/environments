"""
import pytest
from hamcrest import *
from utils.mysql import MySQLDB

db = MySQLDB()
updated_index = db.get_updated_index()

class TestTable:
    @pytest.mark.parametrize("row", updated_index)
    def test_updated_at(self, row):
        assert_that(row['has_key'], equal_to(1), 'table {} has no updated_at index'.format(row['table_name']))

if __name__ == '__main__':
    pytest.main()

"""


import pytest
import re
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

def updated_ind():
	with closing(connection.cursor()) as cursor:
		sql = sql = "SELECT `table_name`, `column_name`, IF(extra like '%on update CURRENT_TIMESTAMP%', 1, 0) AS `updates`, IF(column_key <> '', 1, 0) AS `has_key` FROM `information_schema`.`columns` WHERE (`table_schema`=DATABASE()) AND (`column_name`='updated_at') GROUP BY `table_name`, `column_name` HAVING `table_name` LIKE 'user%';"
		cursor.execute(sql)
		res = cursor.fetchall()		
		return res
"""		
for line in updated_ind():
	print(line)
"""
class TestTable:

	@pytest.mark.parametrize("row", updated_ind())
	def test_updated_at(self, row):
		assert_that(row['has_key'], equal_to('1'), 'table {} has no updated_at index'.format(row['table_name']))

if __name__ == '__main__':
    pytest.main()
