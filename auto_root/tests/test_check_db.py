import pytest

from utils.mysql import MySQLDB


class TestCheckDB:
    @pytest.yield_fixture(autouse=True)
    def run_around_tests(self):
        self.db = MySQLDB()
        yield
        self.db._db_connection.close()

    def test_check_db(self):
        self.db.get_token()
