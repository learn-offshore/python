# # String Concatenation
# # print('pankaj' + 'kumar')

# # String Methods (lower, upper, title, capitalize, strip, replace, split, join, isalpha, isdigit, isalnum, len)

# # name = "haseeb" #hasee#
# # name1 = name.replace('e', '#')
# # print(name1)

# # # name[5] = '#' 
# # # print(name)

# # # print(name.capitalize())
# print(name.title())

# # characters = ['h', 'a', 's', 'e', 'e', 'b']
# # # characters[5] = '#'
# # # print(characters)
# # # print(characters[2])
# # name = " ".join(characters)

# # # print(name)

# # para = """Line1
# # Line2
# # Line3"""



# # String multiplication for repetition
name = "haseeb" #hasee#

age = 18

gender = "male"
print(len(name))
# print(name * 3)

characters = ['h', 'a', 's', 'e', 'e', 'b']

#             #    0    1    2    3    4    5 #positive indexing
#             #   -6   -5   -4   -3   -2   -1 #negative indexing
# # len -> 6
# length = len(characters)
# # print(length)

# print(characters[length - 1])

# # print(len(characters))


# # print(characters[-1])

# # Indexation
print(characters[5])
print(f'characters[5]: {characters[5]}')


# # Slicing
# print(name[1:5])

# f String
print(f'Hey {name}. {name} is {age} years old.')

# # Dot Notation

name = "haseeb" #hasee#
age = 18

user = {name: 'Haseeb', age: '18'}
print(user[name])