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
