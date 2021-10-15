"""
re.split(pattern, string, maxsplit=0, flags=0)
----------------------------------------------
- pattern: the regular expression pattern used for splitting the target string.
- string: The variable pointing to the target string (i.e., the string we want to split).
- maxsplit: The number of splits you wanted to perform. If maxsplit is 2, at most two splits occur, and the remainder of the string is returned as the final element of the list.
- flags: By default, no flags are applied.
"""

import re

target_string = "My name is maximums and my luck numbers are 12 45 78"
# split on white-space
word_list = re.split(r"\s+", target_string)
print(word_list)

target_string = "12-45-78"

# Split only on the first occurrence
# maxsplit is 1
result = re.split(r"\D", target_string, maxsplit=1)
print(result)
# Output ['12', '45-78']

# Split on the three occurrence
# maxsplit is 3
result = re.split(r"\D", target_string, maxsplit=3)
print(result)
# Output ['12', '45', '78']

target_string = "12,45,78,85-17-89"
# 2 delimiter - and ,
# use OR (|) operator to combine two pattern
result = re.split(r"-|,", target_string)
print(result)
# Output ['12', '45', '78', '85', '17', '89']

target_string = "PYnative   dot.com; is for, Python-developer"
# Pattern to split: [-;,.\s]\s*
result = re.split(r"[-;,.\s]\s*", target_string)
print(result)
# Output ['PYnative', 'dot', 'com', 'is', 'for', 'Python', 'developer']

target_string = "With the {74c695031a554c2ebfdb2ee123c8b4f6|something} link, the chain is forged. The {74c695031a554c2ebfdb2ee123c8b4f6|} speech censured, the {74c695031a554c2ebfdb2ee123c8b4f6|} thought forbidden, the {74c695031a554c2ebfdb2ee123c8b4f6|} freedom denied - chains us all irrevocably."

regex = r"\{(.*?)\}"
matches = re.finditer(regex, target_string, re.MULTILINE | re.DOTALL)

for matchNum, match in enumerate(matches):
    for groupNum in range(0, len(match.groups())):
        print(match.group(1))

regex = r'\{.*?\}'
res = re.findall(regex, target_string)
print(str(res))
for r in res:
    print(r)

# 74c695031a554c2ebfdb2ee123c8b4f6|something
# 74c695031a554c2ebfdb2ee123c8b4f6|
# 74c695031a554c2ebfdb2ee123c8b4f6|
# 74c695031a554c2ebfdb2ee123c8b4f6|
