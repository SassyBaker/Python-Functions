from abc import ABC, abstractmethod

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
#
#     def get_circumference(self):
#         pass
#
#
# c = Circle(5)
# print(c.get_area())


# class Temperature:
#     def convert_temp(self, celsius):
#         return (celsius * (9/5)) + 32
#
#
# temp = Temperature()
# print(temp.convert_temp(-42))


# class Vehicle:
#     color = "white"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
# class Bus(Vehicle):
#     pass
#
#
# class Car(Vehicle):
#     pass


# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#         self.cost = capacity * 10
#
#     def fare(self):
#         return self.capacity * 100
#
#
# class Bus(Vehicle):
#     def fare(self):
#         return super().fare() * 1.1
#
#
# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.cost)
