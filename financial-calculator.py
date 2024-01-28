class Employee:
    def __init__(self):
        self.name = input("Employee Name ")
        self.code = int(input("Employee Code "))
        self.salary = float(input("Employee base salary "))
        self.dependents = int(input("Number of Dependents "))

class Paycheck:
    def fgts(salary):
        fgts = salary * 0.08
    def inns(salary):
        if salary <= 1412.00:
            inss = salary * 0.075
        elif salary >= 1412.01 and salary <= 2666.68:
            inss = salary * 0.09
        elif salary >= 2666.69 and salary <= 4000.03:
            inss = salary * 0.12
        else:
            inss = salary * 0.14
    def ir(salary):
        if salary <= 2112.00:
            ir = 0
        elif salary >= 2112.01 and salary <= 2826.65:
            ir = salary * 0.075
    def grossincome(self, salary):
        self.extras = float(input("Employee monthly extras: "))
        grossincome = salary + self.extras
    def liquidincome(grossincome, ir, inss):
        liquidincome = grossincome - ir - inss
   