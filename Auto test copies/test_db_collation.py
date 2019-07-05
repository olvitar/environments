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
