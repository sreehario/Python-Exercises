first_subject = int(input("Enter the mark of first subject: "))
second_subject = int(input("Enter the mark of second subject: "))
third_subject = int(input("Enter the mark of third subject: "))
fourth_subject = int(input("Enter the mark of fourth subject: "))
fifth_subject = int(input("Enter the mark of fifth subject: "))
sixth_subject = int(input("Enter the mark of sixth subject: "))

total_mark = first_subject+second_subject+third_subject+fourth_subject+fifth_subject+sixth_subject
print(f"Total mark is {total_mark}")

average_mark = total_mark/6
print(f"Average mark is {average_mark}")

if average_mark >= 90:
    print("Grade is A plus")

elif average_mark >= 80:
    print("Grade is A")

elif average_mark >= 70:
    print("Grade is B plus")

elif average_mark >= 60:
    print("Grade is B")

elif average_mark >= 50:
    print("Grade is C plus")

elif average_mark >= 40:
    print("Grade is C")

else:
    print("Failed")