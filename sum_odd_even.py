sum_of_even = 0
sum_of_odd = 0
for i in range(15, 36):
    if i % 2 == 0:
        sum_of_even = sum_of_even + i
    else:
        sum_of_odd = sum_of_odd + i
print(f"Sum Of Even numbers is {sum_of_even}")
print(f"Sum_Of_Odd numbers is {sum_of_odd}")
