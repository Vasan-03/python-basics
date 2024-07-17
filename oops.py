# class laptop:
#     def __init__(self, price, processor, ram, model):
#         self.price = price
#         self.processor = processor
#         self.ram = ram
#         self.model = model
#
#     def display(self):
#         print("price:", self.price)
#         print("processor:", self.processor)
#         print("ram:", self.ram)
#
#
# dell = laptop(50000, "i15", "8gb", "dell10")
# hp = laptop(60000, "i16", "16gb", "hp10")
#
# hp.display()
# print("")
# dell.display()

# inheritance;
#
# class player:
#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
#
#     def details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#
#
# class playerinfo(player):
#     def positiondetails(self):
#         print("Position:", self.position)
#
#
# player1 = playerinfo("Grealish", 27, "left-winger")
# player2 = playerinfo("Kdb", 30, "mid-fielder")
#
# player1.details()
# player1.positiondetails()
# print("")
# player2.details()
# player2.positiondetails()

# polymorphism:
#
# class cat:
#     def __init__(self, dogsound, catsound):
#         self.dogsound = dogsound
#         self.catsound = catsound
#
#     def sound(self):
#         print("cat:", self.catsound)
#
#
# class dog(cat):
#     def sound(self):
#         print("dog:", self.dogsound)
#
#
# animal = dog("bark", "meow")
# animal.sound()


# encapsulation:

# class info:
#     def __init__(self):
#         self.__name = "vasan"
#         self._age = 21
#
#     def privatevariableaccess(self):
#         print(self.__name)
#
#     @property
#     def age(self):
#         return self._age
#
#
# a1 = info()
# #protected variable
# # we can access protected variable outside the class ,its  the way to communicate to other developers that these
# #are intended for internal use within the class or its subclass
# print(a1._age)
#
# #public varaible
# a1.privatevariableaccess()
#
# # but we cannot access private variable outside class like this
# print(a1.__name)

# abstraction

# from abc import ABC, abstractmethod
#
#
# class car(ABC):
#     @abstractmethod
#     def engine(self):
#         pass
#
#     @abstractmethod
#     def brake(self):
#         pass
#
#
# class shift(car):
#     def engine(self):
#         print("engine heated")
#
#     def brake(self):
#         print("brake alright")
#
#
# obj1 = shift()
# obj1.engine()
# obj1.brake()
# # note:if we inherit abstract base class to child class ,we must implement all abstract methods of base class to child class.
