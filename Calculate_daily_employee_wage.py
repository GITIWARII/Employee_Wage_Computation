import random

class employeeWageComputation:
    attendance = random.randint(0, 1)
    def check(self):
        if employeeWageComputation.attendance == 1:
            print("Employee is Present")
        else:
            print("Employee is Absent")

    def dailyWage(self):
        wage_per_hour = 20
        if employeeWageComputation.attendance == 1:
            employee_hours = 8
        else:
            employee_hours = 0
        employee_wage = employee_hours * wage_per_hour
        print("Employee's daily Wage is :", employee_wage)

employee = employeeWageComputation()
employee.check()
employee.dailyWage()