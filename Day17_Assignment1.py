#  list comprehension to filter out the employees who work in the 'Sales' department and convert their names to uppercase. 
# Given Employees Details
employees = [
    {"name": "John Doe", "department": "Sales"},
    {"name": "Jane Smith", "department": "Marketing"},
    {"name": "Emily Johnson", "department": "Sales"},
    {"name": "Michael Brown", "department": "HR"}
]

sales_employees = [employee['name'].upper() for employee in employees if employee['department'] == 'Sales']

print(sales_employees)

'''     OUTPUT
['JOHN DOE', 'EMILY JOHNSON']
'''
