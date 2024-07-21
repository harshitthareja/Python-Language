# RailwayForm --> class [blueprint]
# harry --> harry ki info wala form -->  object [entitiy]
# tom --> tom ki info wala form -->  object [entitiy]
# shubham --> shubham ki info wala form -->  object [entitiy]
# shubham.changeName("Shubhi")

class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()
a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()