"""class A:
    __A = "Sakun" #private variable
    _B = "Palpa" #protected variable
    course = "Python" #public variable
"""

"""class Veichle:
    _model = "C897"
    __engine = "asdfghj"
    TAX = 0.13
    ADDITIONAL_MARGIN = 10000
    def __init__(self,price,manufacture):
        self.price = price
        self.manufacture = manufacture
 
    def getSellingPrice(self):
        return self.price + self.price * self.TAX + self.ADDITIONAL_MARGIN
 
    def _getManufacture(self):
        return self.manufacture
    
    def getModel(self):
        return self._model
    
    def getEngine(self):
        return self.__engine
 
# This class is inherited from the Veichle
# In the bracket the class name given from which it is inherited
 
class MotorBike(Veichle):
    def __init__(self, cost, manufacture):
        Veichle.__init__(self, cost, manufacture)
 
    def getNumberOfWheels(self):
        return 2
 
    def getRoadtax(self):
        return 4000
    
    def getModel(self):
        return self._model
        
    def __str__(self):
        return "this is __str__ function"
    

pulsar = MotorBike(250000, "Bajaj")
vech = Veichle(300000, "Honda")
# Here pulsar is the object of the Motorbike but it has the method of the Veichle class aswell
# This is what inheritance features
print("Selling price = {} ".format(pulsar.getSellingPrice()))
print("manufacturer = {}".format(pulsar._getManufacture()))
print("Number of wheels = {}".format(pulsar.getNumberOfWheels()))
print("Road Tax = {}".format(pulsar.getRoadtax()))
print("Bajaj Model = {}".format(pulsar.getModel()))

#print("EngineClass Model = {}".format(vech.getEngine()))
#print("Honda Model = {}".format(vech.__getManufacture()))

print(pulsar._model)
print(pulsar.getEngine())
print(pulsar)
"""


from abc import ABCMeta, abstractmethod