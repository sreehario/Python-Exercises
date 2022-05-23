sample_string = input("Enter a string:")
sample_list = sample_string.split()
word = input("Enter the word:")

for i in sample_list:
    if word == i:
        sample_list.remove(i)

modified_string = ' '.join(sample_list)
print(f'Modified String is :{modified_string}')


