import re
pattern = re.compile("^user\w+")
txt = ['users', 'users_affiliates', 'fignya', 'white_noise', 'users_stats']
"""
for i in txt:
	result=pattern.search(i)
	print(result)

RESULT:
<re.Match object; span=(0, 5), match='users'>
<re.Match object; span=(0, 16), match='users_affiliates'>
None
None
<re.Match object; span=(0, 11), match='users_stats'>	
"""

#[print(line) for line in test_data]

for i in txt:
	result=pattern.search(i)
	if result is not None:
		print(result.group(0))

""" RESULT:		
users
users_affiliates
users_stats
"""