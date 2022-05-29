words = input("Enter the words:").split()

dict = {}

for word in words:
      if word in dict:
         dict[word] = dict[word]+1
      else:
         dict[word] = 1

lst = []

for i in dict:
    lst.append(dict[i])

lst.sort()
occurance = [lst[-1], lst[-2], lst[-3]]

second_dict = {}

for i in occurance:
    for j in dict:
        if dict[j]==i:
            second_dict[j] = i
print("Occurances of text:",second_dict)
