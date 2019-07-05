import re

test_data = [{'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_pay_sys_daily',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_phones',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_project_mask',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_push_app_tokens',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_push_tokens',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_refcode_balances',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_reg_info',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_reg_landing',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_remarketing',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_special_info',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_stats',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_stats_additional_info',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_stats_ext',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_stats_numeration',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_stats_summary',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_unsubscribed',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_unsubscribed_phone',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'users_vip_track',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': 'without_users_logins',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': '_users_cid',
  'updates': '1'},
 {'column_name': 'updated_at',
  'has_key': '1',
  'table_name': '_users_cid_info',
  'updates': '1'}]
pattern = re.compile("^user\w+")
for line in test_data:
	table = (line['table_name'])
	#print(table)
	result=pattern.search(table)
	
	if result is not None and table == result.group(0):
		print(line)
	