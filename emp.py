class Employee:
    total_employees = 0
    def __init__(self, first_name, last_name, salary, department):
        self.__first_name = first_name
        self.__last_name = last_name
        self.salary = salary
        self.__department = department
        Employee.total_employees += 1

    def average_salary(employees):
        total_salary = 0
        for employee in employees:
            total_salary += employee.salary
        return total_salary / Employee.total_employees

class FulltimeEmployee(Employee):

    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary, department)

    def full_time_benefits(self):
        print("Few benefits as full-time employee.")

def main():
    employees = []
    fulltimeemp1 = FulltimeEmployee("Employee1", "FamilyName1", 100000, "Technical")
    fulltimeemp1.full_time_benefits()
    employees.append(fulltimeemp1)
    fulltimeemp2 = FulltimeEmployee("Employee2", "FamilyName2", 170000, "Operational")
    employees.append(fulltimeemp2)
    emp1 = Employee("Employee3", "FamilyName3", 120000, "Program-Coordination")
    employees.append(emp1)
    emp2 = Employee("Employee4", "FamilyName4", 110000, "HR")
    employees.append(emp2)
    print("Average salary:", FulltimeEmployee.average_salary(employees))
if __name__ == "__main__":
    main()