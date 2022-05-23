items = int(input("Enter how many items you are buying:"))

if items < 10:
    price = items * 12
    print(f'price is {price}')

elif items >= 10 and items <= 99:
    price = items * 10
    print(f'price is {price}')

else:
    price = items * 7
    print(f'price is {price}')


