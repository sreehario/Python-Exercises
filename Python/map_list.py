first_list = [i for i in input("Enter the first list:").split()]
second_list = [i for i in input("Enter the second list:").split()]

sample_dict = {}

j = 0
for i in first_list:
     sample_dict[i] = second_list[j]
     j = j+1

print('Dictionary is', sample_dict)

