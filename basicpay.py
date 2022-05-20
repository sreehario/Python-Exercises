employee_id = input("Enter the employee id:")
name = input("Enter the name:")
basic_pay = int(input("Enter the basic pay: "))

if basic_pay > 10000:
    hra = basic_pay * 0.15
    print(f"HRA is {hra}")
    da = basic_pay * 0.08
    print(f"DA is {da}")
    net_pay = basic_pay+hra+da
    print(f"Net pay is {net_pay}") 

if basic_pay <= 10000 and basic_pay >= 5000:
    hra = basic_pay * 0.10
    print(f"HRA is {hra}")
    da = basic_pay * 0.05
    print(f"DA is {da}")
    net_pay = basic_pay+hra+da
    print(f"Net pay is {net_pay}")

if basic_pay < 5000:
    hra = basic_pay* 0.05
    print(f"HRA is {hra}")
    da = basic_pay* 0.03
    print(f"DA is {da}")
    net_pay = basic_pay+hra+da
    print(f"Net pay is {net_pay}")
