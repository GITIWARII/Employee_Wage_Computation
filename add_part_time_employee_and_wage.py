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
        part_time = random.randint(0,1)
        if employeeWageComputation.attendance == 1:
            if part_time == 1:
                print("Part time employee")
                employee_hours = 4
            else:
                print("Full time employee")
                employee_hours = 8
        else:
            employee_hours = 0
        employee_wage = employee_hours * wage_per_hour
        print("Employee's daily Wage is :", employee_wage)

employee = employeeWageComputation()
employee.check()
employee.dailyWage()
