upper_count = 0
lower_count = 0
def counts(sample_string):
    global upper_count
    global lower_count
    for i in sample_string:
       if i.isupper():
           upper_count = upper_count+1
       else:
           lower_count = lower_count + 1
    print(f"Number of upper case is {upper_count} and Number of lower case is {lower_count}")

sample_string = input('Enter the string:')
counts(sample_string)