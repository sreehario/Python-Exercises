class Student:
    
    def get_data(self):
        self.name = input("Enter name:")
        self.roll_no = int(input("Enter rollno:"))

    def print_data(self):
        print(f'Name is {self.name} and Roll number is {self.roll_no}')

class Mark(Student):

    def input_data(self):
        self.get_data()
        self.mark1 = int(input("Enter mark of physics:"))
        self.mark2 = int(input("Enter mark of biology:"))
        self.mark3 = int(input("Enter mark of chemistry:"))
        self.mark4 = int(input("Enter mark of maths:"))
        self.mark5 = int(input("Enter mark of english:"))
        self.mark6 = int(input("Enter mark of malayalam:"))
        self.total = self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5 +self.mark6
    
    def out_data(self):
        self.print_data()
        print('Mark of physics is', self.mark1)
        print('Mark of biology is', self.mark2)
        print('Mark of chemistry is', self.mark3)
        print('Mark of maths is', self.mark4)
        print('Mark of english is', self.mark5)
        print('Mark of malayalam is', self.mark6)
        print('Total mark is', self.total)

student1 = Student()
marks = Mark()
marks.input_data()
marks.out_data()
