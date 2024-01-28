class Employee:
    def __init__(self):
        self.name = input("Employee Name ")
        self.code = int(input("Employee Code "))
        self.salary = float(input("Employee base salary "))
        assert self.salary > 0, "Salary must be greater than 0"
        self.dependents = int(input("Number of Dependents "))

    def fgts(self):
        return "%.2f" % (self.salary * 0.08)
    
    def inss(self):
        if self.salary <= 1412.00:
            return "%.2f" % (self.salary * 0.075)
        elif self.salary >= 1412.01 and self.salary <= 2666.68:
            return "%.2f" % (self.salary * 0.09)
        elif self.salary >= 2666.69 and self.salary <= 4000.03:
            return "%.2f" % (self.salary * 0.12)
        else:
            return "%.2f" % (self.salary * 0.14)
        
    def ir(self):
        if self.salary <= 2112.00:
            return 0
        elif self.salary >= 2112.01 and self.salary <= 2826.65:
            return "%.2f" % (self.salary * 0.075)
        else:
            return "%.2f" % (self.salary * 0.275)
        
    def grossIncome(self):
        self.extras = 1700 #float(input("Employee monthly extras: "))
        return "%.2f" % (self.salary + self.extras)
    
    # def liquidIncome(self):
    #     return self.grossIncome - self.ir - self.inss
        

# class Paycheck(Employee):
#     print(f"{Employee().name} ´s Paycheck")
#     print(f"Employee code: {Employee().code}")
#     print(f"Base salary: {Employee().salary}")
#     print(f"Extras: {Employee().extras}")
#     print(f"IR: {Employee().ir}")
#     print(f"INSS: {Employee().inss}")
#     print(f"Gross Income: {Employee().grossIncome}")
#     print(f"Liquid Income: {Employee().liquidIncome}")

employee1 = Employee()
print(f"{employee1.name} ´s Paycheck")
print(f"Employee code: {employee1.code}")
print(f"Base salary: {employee1.salary}")
# print(f"Extras: {employee1.extras}")
print(f"IR: {employee1.ir()}")
print(f"INSS: {employee1.inss()}")
print(f"Gross Income: {employee1.grossIncome()}")
# print(f"Liquid Income: {employee1.liquidIncome()}")