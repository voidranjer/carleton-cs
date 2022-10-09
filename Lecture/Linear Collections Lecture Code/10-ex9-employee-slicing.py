# Assume you have a long list of employee information. The list is formatted using the following structure:
# firstname1, lastname1, positon1, employeeid1, firstname2, lastname2, etc.
# Write a function that takes a list and an employee index. The function should return a new list containing only the information for the requested employee.

def get_employee_info(employees, index):
    start_index = index * 4
    end_index = start_index + 4
    return employees[start_index:end_index]


employees = [
    "Larry", "Page", "Co-Founder", 0,
    "Sergey", "Brin", "Co-Founder", 0,
    "Craig", "Silverstein", "Director of Technology", 1,
    "Marissa", "Mayer", "Software Engineer", 2,
    "Kendra", "DiGirolamo", "Sales Coordinator", 3,
    "Jim", "Reese", "Head Neurosurgeon", 4,
    "Gerald", "Aigner", "Supply Manager", 5
]


for i in range(10):
    print(get_employee_info(employees, i))
