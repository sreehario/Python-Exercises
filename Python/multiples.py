sum = 0
for i in range(1, 21):
    if i % 2 != 0 and i%3 != 0:
       sum = sum + i
       print(f"Values are {i}")
print(f"Sum of the number is {sum}")
