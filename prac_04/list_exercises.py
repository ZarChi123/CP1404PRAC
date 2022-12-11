# numbers=[]
# for i in range(5):
#     number=int(input("Number:"))
#     numbers.append(number)
# print(f"The first number is",numbers[0])
# print("The last number is",numbers[-1])
# print("The smallest number is",min(numbers))
# print("The largest number is",max(numbers))
# print("The average number is",sum(numbers)/len(numbers))
#
# """Woefully inadequate security checker"""
# usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
#              'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
#
# username=input("Enter username:")
# if username in usernames:
#     print("Access granted")
# else:
#     print("Access denied")

# values = [1, 2, 3, 2]
# values.remove(2)
# # print(values)
# before = [1, 4, 0, -1]
# after = before.sort()
# print(after[0])

# words = ["aye", "bee", "sea"]
# print("/".join(words))

# words = ["aye", "bee", "sea", "bee"]
# words.remove("bee")
# print(words.pop())

# things = list("one two three")
# print("{}-{}".format(*things))
#
# print("*".join([len(word) for word in "one*two*three".split('*')]))

# before = [1, 4, 0, -1]
# after = before.sort()
# print(after[0])

# def process(x, y=2, z=3):
#     return x + y + z
# words = ["aye", "bee", "sea"]
# print("/".join(words))

before = [1, 4, 0, -1]
after = before.sort()
print(after[0])