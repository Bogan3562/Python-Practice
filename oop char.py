from datetime import datetime, date

# Base Class: Person
class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def get_age(self):
        dob_date = datetime.strptime(self.dob, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        return

# Derived Class: Employee (inherits from Person)
class Employee(Person):
    def __init__(self, name, dob, employee_id, department, salary):
        super().__init__(name, dob)
        self.employee_id = employee_id 
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nDOB: {self.dob}\nDepartment: {self.department}\nSalary: {self.salary}"

# Class: Attendance
class Attendance:
    def __init__(self):
        self.attendance_list = []

    def mark_attendance(self, date):
        self.attendance_list.append(date)

    def get_attendance_count(self):
        return len(self.attendance_list)

# Class: Payroll
class Payroll:
    def calculate_pay(self, attendance_count):
        return attendance_count * 1000

# Final Class: HRSystem (inherits from Employee, Attendance, and Payroll)
class HRSystem(Employee, Attendance, Payroll):
    def __init__(self, name, dob, employee_id, department, salary):
        Employee.__init__(self, name, dob, employee_id, department, salary)
        Attendance.__init__(self)

    def generate_report(self):
        attendance_count = self.get_attendance_count()
        final_salary = self.calculate_pay(attendance_count)
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.get_age()}")
        print(f"Department: {self.department}")
        print(f"Total Attendance: {attendance_count}")
        print(f"Final Salary: {final_salary}")

# Testing the system with two employee objects
employee1 = HRSystem("Alice", "1990-05-15", "E001", "HR", 50000)
employee2 = HRSystem("Bob", "1985-03-10", "E002", "Finance", 60000)

# Marking attendance
employee1.mark_attendance(date(2025, 4, 15))
employee1.mark_attendance(date(2025, 4, 16))

employee2.mark_attendance(date(2025, 4, 15))

# Generating reports
print("Employee 1 Report:")
employee1.generate_report()
print("\nEmployee 2 Report:")
employee2.generate_report()