import random


class employeeWageComputation:
    attendance = random.randint(0, 1)

    def check(self):
        if employeeWageComputation.attendance == 1:
            print("Employee is Present")
        else:
            print("Employee is Absent")

    def wages(self):
        i = 1
        wage_per_hour = 20
        monthly_wage = 0
        employee_total_working_days = 0
        employee_total_hours = 0

        while employee_total_working_days <20:

            part_time = random.randint(0, 1)
            if employeeWageComputation.attendance == 1:
                employee_total_working_days += 1
                if part_time == 0:

                    employee_hours = 8
                else:
                    employee_hours = 4

                if employee_total_hours + employee_hours <= 100:
                    employee_total_hours += employee_hours
                else:
                    employee_hours = 100 - employee_total_hours
                    employee_total_hours += employee_hours




            else:
                employee_hours = 0

            employee_wage = employee_hours * wage_per_hour
            monthly_wage += employee_wage



        print("Employee's total monthly wage is :", monthly_wage)


employee = employeeWageComputation()
employee.check()
employee.wages()
