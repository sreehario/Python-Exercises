class Employee:

    def get_data(self):
        self.number = int(input("Enter the employee number:"))
        self.name = input("Enter the name:")
        self.designation = input("Enter the designation:")
        self.address = input("Enter the address:")
        self.phone_no = int(input("Enter the phone number:"))

    def put_data(self):
        print(f'Employee number is :{self.number}')
        print(f'Employee name is :{self.name}')
        print(f'Employee designation is :{self.designation}')
        print(f'Employee address is :{self.address}')
        print(f'Employee phone number is :{self.phone_no}')

class Salary(Employee):

    def get_data1(self):
        self.get_data()
        self.basic_pay = int(input("Enter the Basicpay:"))
        self.income_tax = int(input("Enter the income tax:",))

    def calculate(self):
        self.da = self.basic_pay * 0.08
        self.hra = self.basic_pay * 0.15
        self.gross_pay = self.basic_pay * 0.05
        self.pf = self.basic_pay * 0.10
        self.net_pay = self.da + self.hra + self.basic_pay + self.gross_pay +self.income_tax+ self.pf

    def display(self):
        self.put_data()
        print("Basic pay is:", self.basic_pay)
        print("Income tax is:", self.income_tax)
        print("DA is:", self.da)
        print("HRA is:", self.hra)
        print("Gross pay is:", self.gross_pay)
        print("PF is:", self.pf)      
        print("Net pay is:", self.net_pay)    


salary = Salary()
salary.get_data1()
salary.calculate()            
salary.display()