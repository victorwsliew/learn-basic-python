employee_file = open("./assets/employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)
# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readlines()) #return array

employee_file.close()



