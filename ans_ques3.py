class Department:
    def __init__(self, name):
        self.name = name
        self.manager = None
        self.employees = {}

class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.department = None

class Organization:
    def __init__(self, president):
        self.president = president
        self.departments = {}
        self.employees = {}

    def add_department(self, department_name):
        department = Department(department_name)
        self.departments[department_name] = department
        return department

    def add_employee(self, employee_name, title, department):
        employee = Employee(employee_name, title)
        employee.department = department
        department.manager = employee
        department.employees[employee_name] = employee
        self.employees[employee_name] = employee
        return employee

    def create_org_chart(self):
        chart = "President: " + self.president.name + "\n"
        for department_name, department in self.departments.items():
            chart += "\tVice President " + department_name + ": " + department.manager.name + "\n"
            for employee_name, employee in department.employees.items():
                chart += "\t\t" + employee.title + ": " + employee.name + "\n"
        return chart

# Create the organization
organization = Organization(Employee("Paul Ross", "President"))

# Add finance department and employees
finance_department = organization.add_department("Finance")
accounts_department = organization.add_department("Accounts")
treasury_department = organization.add_department("Treasury")
organization.add_employee("Mark Davis", "Vice President Finance", finance_department)
organization.add_employee("John Smith", "Manager", accounts_department)
organization.add_employee("Jane Doe", "Manager", treasury_department)

# Add HR department and employees
hr_department = organization.add_department("Human Resources")
operations_department = organization.add_department("Operations")
recruitment_department = organization.add_department("Recruitment")
staff_development_department = organization.add_department("Staff Development")
organization.add_employee("Roy", "Vice President HR", hr_department)
organization.add_employee("Mike Green", "Manager", operations_department)
organization.add_employee("Sarah Lee", "Manager", recruitment_department)
organization.add_employee("David Brown", "Manager", staff_development_department)

# Add other departments and employees (similarly)

# Print the organization chart
print(organization.create_org_chart())
