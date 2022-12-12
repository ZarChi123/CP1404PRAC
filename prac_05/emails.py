# """Email Program"""
#
#
# def main():
#     """Create dictionary of emails-to-names."""
#     email_to_name = {}
#     email = input("Email: ")
#     while email != "":
#         name = get_name_from_email(email)
#         confirmation = input(f"Is your name {name}? (Y/n) ")
#         if confirmation.upper() != "Y" and confirmation != "":
#             name = input("Name: ")
#         email_to_name[email] = name
#         email = input("Email: ")
#
#     for email, name in email_to_name.items():
#         print(f"{name} ({email})")
#
#
# def get_name_from_email(email):
#     """Extract name from email address."""
#     prefix = email.split('@')[0]
#     parts = prefix.split('.')
#     name = " ".join(parts).title()
#     return name
#
#
# main()

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print([v + 1 for v in d.values() if v < 3])
#
# things = {1, 10, 20, 1, 10}
# things.add(20)
# print(len(things))

# d = {'a': 3, 'b': 2, 'c': 1}
# for k in sorted(list(d.keys())):
#     print(k, d[k], sep='', end='')

# a = {1, 2, 3, 4}
# b = {2, 4, 6}
# print(a - b)
# print(a ^ b)

# d = {'a': -1, 'b': 2, 'c': 3}
# d['d'] = 4
# print(d[-1])

# products=[["phone",340,False],["PC",1420.95,True],["Plant",24.5,True]]
# for product in products:
#     if product[2]:
#         print(product)

"""Classes and Objects"""
"""List comprehension"""
# products=[["phone",340,False],["PC",1420.95,True],["Plant",24.5,True]]
# product_list=[product for product in products if product[2]==True]
# print(product_list)

"""Print only products """
# products=[["phone",340,False],["PC",1420.95,True],["Plant",24.5,True]]
# product_list=[product[1] for product in products if product[2]==True]
# print(product_list)

"""Repr is used to change any datatype to string """
# things=[1,0.2,"hi",(1,"a"),{1:4}]
# for thing in things:
#     print("{:>8} is: {}".format(repr(thing),type(thing)))
# print("{} is: {}".format(repr(things), type(things)))
"""Class """

# class Student:
#     def __init__(self, first_name="", last_name="", student_id=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.id = student_id
#
#     def __str__(self):
#         return f"{self.first_name}{self.last_name}({self.id})"
#
#
# first_name = input("First name:")
# last_name = input("Last name:")
# student_id = int(input("ID:"))
# s1 = Student(first_name, last_name, student_id)
# print(s1.first_name, "has ID", s1.id)

"""class local variable =self"""


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"{self.name} ({self.age})"
#
#
# p1 = Person("Jane", 19)
# print(p1)
# people = [Person("Alexa",21), Person("Siri", 25)]
# print(people)
# def __repr__(self):
#     return f"{self.name}({self.age})"

"""KIVY"""
from kivy.app import App
from kivy.app import Widget
class HelloWorld(App):
    def build(self):
        self.root=Widget()
        return self.root
HelloWorld().run()