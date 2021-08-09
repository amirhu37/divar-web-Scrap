import regex as re

e_in =input()

match = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

if (re.search(match, e_in)):
    print('OK')
else:
    print('WRONG')
