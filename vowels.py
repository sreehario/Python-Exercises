vowels = 0
sample_string = input("ENter the string:")

for i in sample_string.upper():
    if i == "A" or i =="E" or i == "I" or i == "O" or i == "U":
        vowels = vowels+1
print(f"Total number of vowels in the string is {vowels}")