# class Employee:
#     def __init__(self):
#         self.__name = "Harry"

# a = Employee()
# # print(a.__name)  # Cannot be accessed directly
# print(a._Employee__name)  # Can be accessed indirectly
# print(a.__dir__())

class Student:
    def __init__(self):
        self._name = "Harry"
    
    def _funName(self):  # Protected method
        return "CodeWithHarry"
class Subject(Student):  # Inherited Class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())