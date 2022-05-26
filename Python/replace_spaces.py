import re

user_input = input("Enter the string:")
if "_" in user_input:
    string_replace = re.sub('_', ' ', user_input)
    print(string_replace)

if " " in user_input:
    string_replace = re.sub(' ', '_', user_input)
    print(string_replace)

