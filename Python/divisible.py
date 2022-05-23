numbers =[int(i) for i in input("Enter the numbers:").split()]

for i in numbers:
    if i % 5 == 0:
        print("Numbers divisible by five are", i)