# creating a class employee that has total employees, names, family name, salary, and department of employee
class Employee(object):
    total = 0
    name = []
    family = []
    salary = []
    department = []

    # constructor
    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        self.main(n, f, s, d)

    # keeps track of each new employee
    def main(self, n, f, s, d):
        Employee.total += 1
        Employee.name.append(n)
        Employee.family.append(f)
        Employee.salary.append(s)
        Employee.department.append(d)

    # return average salary of all employee
    def averagesalary(self):
        totalsalary = 0
        for e in Employee.salary:
            totalsalary += e
        return totalsalary / len(Employee.salary)

# create inheritance class of full time employee from employee
class FulltimeEmployee(Employee):
    def __init__(self, n, f, s, d):
        Employee.__init__(self, n, f, s, d)

# creating class objects and printing accordingly
fte1 = FulltimeEmployee('Bob', 'Builder', 50000, 'Construction')
fte2 = FulltimeEmployee('Jack', 'Jones', 20000, 'Engineering')
fte3 = FulltimeEmployee('John', 'Smith', 50000, 'Medicine')
e1 = Employee('Hello', 'World', 70000, 'Art')
e2 = Employee('Py', 'Charm', 100000, 'Fitness')
e3 = Employee('First', 'Last', 35000, 'Education')

print("Total full time employee: ", fte1.total)
print("Full time employee names: ", fte1.name)
print("Full time employee family: ", fte1.family)
print("Full time employee salary: ", fte1.salary)
print("Full time employee department: ", fte1.department)
print("Average full time employee salary: ", FulltimeEmployee.averagesalary(Employee))

print("________________________")

print("Total employee: ", e1.total)
print("Employee names: ", e1.name)
print("Employee family: ", e1.family)
print("Employee salary: ", e1.salary)
print("Employee department: ", e1.department)
print("Average employee salary: ", e1.averagesalary())

print("________________________")

print(Employee.name)
print(Employee.family)
print(Employee.salary)
print(Employee.department)

print("________________________")

print(FulltimeEmployee.name)
print(Employee.family)
print(Employee.salary)
print(Employee.department)