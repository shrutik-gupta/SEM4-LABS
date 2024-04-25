class Employee():
    def __init__(self,emp_id, emp_name):
        self.emp_name= emp_name
        self.emp_id= emp_id
        self.emp_salary = None
        self.emp_department = None

    def  calculate_emp_salary(self, emp_salary):
        self.emp_salary = emp_salary-(0.2*emp_salary)
        print("Salary calculated after tax")
    def emp_assign_department(self,emp_department):
        self.emp_department = emp_department
        print("Department assigned")

    def print_employee_details(self):
        print("Employee's name is: ", self.emp_name)
        print("Employee's id is: ", self.emp_id)
        print("Employee's department is: ", self.emp_department)
        print("Employee's salary is: ", self.emp_salary)

e1 = Employee(101, "Shrutik")
e1.calculate_emp_salary(10000)
e1.emp_assign_department("Logistics")
e1.print_employee_details()