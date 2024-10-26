print("Lesson 5")

class Employee:
    def __init__(self, surname, name, age, experience):
        self.Surname = surname
        self.Name = name
        self.Age = age
        self.Experience = experience
        self.Rate = 400
        self.Salary= self.Experience * self.Rate + 8000

    def print_employee_info(self):
        print("Прізвище:", self.Surname)
        print("Імя:", self.Name)
        print("Досвід:", self.Experience)

    def to_receive_a_salary(self):
        print("Ваша ЗП:", self.Salary)

emloyee1=Employee("Sigma","Oleksand",37,7)

emloyee1.print_employee_info()
emloyee1.to_receive_a_salary()


class Driver(Employee):
    def __init__(self,surname, name, age, experience,transport):
        super().__init__(surname,name,age,experience)
        self.Rate=1100
        self.Transport=transport
        self.TSalary = experience * 1000 + 8000
    def show_transport(self):
        print("Транспорт:", self.Transport)
    def to_receive_a_salary(self):
        print("Ваша Зарплата:", self.TSalary)


print()

emloyee2=Driver("Kogut","Oleg",27,2,"AboBus Bohdan")

emloyee2.print_employee_info()
emloyee2.show_transport()
emloyee2.to_receive_a_salary()

class Sigmector(Employee):
    def __init__(self,surname, name, age, experience,licence):
        super().__init__(surname,name,age,experience)
        self.Rate=1100
        self.Licence=licence
        self.Lsalary = experience * 1000 + 8000

    def show_licence(self):
        print("Ліцензія:", self.Licence)
    def to_receive_a_salary(self):
        print("Ваша Зарплата:", self.LSalary)

print()
try:
    emloyee3=Sigmector("Skala","Mychailo",15,1,"BO4184821CI")
    emloyee3.print_employee_info()
    emloyee3.show_licence()
    emloyee3.to_receive_a_salary()
except TypeError as error:
    print(f"Error:{error}")
