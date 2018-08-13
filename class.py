"""class Person:
    name = "Sakun"
    course = "Python"
    address = "Palpa"
    
    def getName(self):
        return self.name
    def getCourse(self):
        return self.course
    def getAddress(self):
        return self.address
    def add(selfff):
        return selfff.name
        
std = Person()
print(std.getName())
print(std.getCourse())
print(std.getAddress())
print(std.add())
"""


"""class Ball:
    radius = '15 inch'
    color = 'white'
    cost = '1000'
    
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def getCost(self):
        return self.cost

foot = Ball()
print(foot.getRadius())
print(foot.getColor())
print(foot.getCost())




class Person:
    def __init__(self,name,course,address = "Palpa"):
        self.name = name
        self.course = course
        self.address = address
 
    def getName(self):
        return self.name
 
    def getCourse(self):
        return self.course
    
    def getAddress(self):
        return self.address
 
 
student = Person("Sakun", "Python")
learner = Person("Usha", "CSIT", "Lalitpur")
student.name = "me"


print(student.getName())
print(student.getCourse())
print(student.getAddress())

print(learner.getName())
print(learner.getCourse())

print("studentName = {}, studentCourse = {}, studentAddress = {}".format(student.getName(), student.getCourse(), student.getAddress()))
#print("learner = {}".format(learner.getName()))"""




class Vechile:
    TAX = 0.13
    ADDITIONAL_MARGIN = 1000
    def __init__(self, price, manufacture):
        self.price = price
        self.manufacture = manufacture
    
    def getSellingPrice(self):
        return self.price + self.price * self.TAX + self.ADDITIONAL_MARGIN
    
    def getManufacture(self):
        return self.manufacture

pulsar = Vechile(250000, 'Bajaz')
splender = Vechile(300000, 'Honda')
print("Pulsar price = {} and manufacture is {}".format(pulsar.getSellingPrice(),pulsar.getManufacture()))
print("Splender price = {} and manufacture is {}".format(splender.getSellingPrice(),splender.getManufacture()))