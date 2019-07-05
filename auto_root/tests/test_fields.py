import json

import pytest
from hamcrest import *
from config import ConfigReader
from utils.cli_utils import run_console_command

test_data = json.loads(run_console_command(
    '{0}/yii db-status/tables-timestamp --column=updated_at --json'.format(ConfigReader('urls').get('analytics_home'))))


class TestFields:

    @pytest.mark.parametrize("row", test_data)
    def test_updated_at(self, row):
        assert_that(row['has_key'], equal_to('1'), 'table {} has no updated_at index'.format(row['table_name']))


if __name__ == '__main__':
    pytest.main()
