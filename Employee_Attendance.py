import random

class employee_wage_computation:

    check = random.randint(0, 1)

    def attendance(self):
        if employee_wage_computation.check == 0:
            print("Employee is absent")
        else:
            print("Employee is present")


emp = employee_wage_computation()
emp.attendance()






