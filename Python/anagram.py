from itertools import permutations

word = input("Enter a word:")

a = permutations(word)
for i in list(a):
    print("Anagrams are:",''.join(list(i)))
   