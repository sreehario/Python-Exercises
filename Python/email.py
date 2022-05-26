import re

email = input("Enter valid email address:")

result = re.split('@', email)
email_part = result[0]
print("first part of mail is:", email_part)