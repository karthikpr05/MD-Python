#class ---> It is a blueprint or a templete used to create object
#Advantages:
#Reusable
#Easy to use
#Cleaner code
#We create object to referance the function defined under those cases


from calculator import Calculator
from student import Student
from employee import Employee


#Creating objects in order to access the functions defined under each classes
cal = Calculator()
std = Student()
emp = Employee()


cal.add(10,20)
cal.mul(10,20)
cal.sub(10,20)

std.display_name()
std.display_age()
std.display_marks()


emp.employee_name()
emp.salary()
emp.department()