# Class: are blueprint for creating new objects
# Objects: Instance of a class

# E.g
# Class: Human
# Objects: John, Mary, Jack

# class Point:
#     default_color = "red"  # Class level attribute
#
#     def __init__(self, x, y):  # Constructor
#         self.x = x  # Instance Attributes
#         self.y = y
#
#     @classmethod
#     def zero(cls):
#         return cls(0, 0)
#
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)  # Example usage

# point = Point(0, 0)  # Initialize
# point = Point.zero()  # Factory method
#
# point.draw()


# Magic methods
# https://rszalski.github.io/magicmethods/
# class Point:
#     def __init__(self, x, y):  # Constructor
#         self.x = x  # Instance Attributes
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# print(point)


# Comparing Objects (Works with arithmetic operation)
# class Point:
#     def __init__(self, x, y):  # Constructor
#         self.x = x  # Instance Attributes
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __gt__(self, other):  # works with less than automatically
#         return self.x > other.x and self.y > other.y
#
#
# point = Point(1, 2)
# other = Point(1, 2)
# print(point == other)
# print(point > other)


# # Making Custom Containers
# class TagCloud:
#     def __init__(self):
#         self.__tags = {}  # __ makes it private
#
#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
#
#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)
#
#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count
#
#     def __len__(self):
#         return len(self.__tags)
#
#     def __iter__(self):
#         return iter(self.__tags)
#
#
# # cloud = TagCloud()
# # cloud["Python"]  # get item
# # cloud["Python"] = 10  # set item
# # len(cloud)  # gets length of item
# # for i in cloud:  # Using the iter magic method
# #     print(i)
# #
# # cloud.add("Python")
# # cloud.add("python")
# # cloud.add("Python")
# # print(cloud.__tags)

# # Accessing private
# cloud = TagCloud()
# print(cloud.__dict__)
# print(cloud._TagCloud__tags)


# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#
# user = Person("Jack", "Sparrow")
# print(user)
