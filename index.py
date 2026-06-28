# to input anything from user
# myName = input('Name: ');
# print('Hello', myName);


#python condition --> and , or , not

# print(1 == 1 and 2 == 2); # true
# print(1 == 1 or 2 == 3); # true
# print(not(1 == 2)); # true
# print(not(1 == 1)); # false

#if else conditions
# if 1 == 2:
#     print('true')
# elif 2 == 2:
#     print('true tow');
# else:
#     print('false')

# x = [4, True, 'jhon']
# y = 'hi'
# x.append('hello') # add element to list
# y = y.replace('h', 'H') # replace character in string
# x.extend([1,2,3]) # add multiple element to list
# x.pop() # remove last element from list
# x.pop(0) # remove element at index 0
# y = x[:2] # slicing list also just with : sign we can copy hole list
# print(len(x), len(y), x[0], x, y)


# tuples --> immutable list (we cannot change it)
# x = (0, 1, 2, 3)
# print(x[0], len(x))


# loops --> for , while

# for i in range(1, 10, 1): #start, stop, step -> 
#     print(i)

# for i in [122, 22, 32, 4, 5]: # loop through list
#     print(i)


# while True:
#     name = input('Name: ')
#     if name == 'jhon':
#         print('Hello jhon')
#         break
#     else:
#         print('Try again')
#         continue

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# slice operator
# sliced = [start:stop:step] # default start = 0, stop = len(list), step = 1
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # sliced = x[0:5:3]
# sliced = x[0:5:1]
# print(sliced)

# sets --> unordered collection of unique elements
# x = set()
# s = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# s.add(6) # add element to set
# s.remove(3) # remove element from set

# print(4 in s) # check if element is in set
# print(len(s)) # length of set
# print(s.union(s2)) # union of two sets
# print(s.intersection(s2)) # intersection of two sets
# print(s.difference(s2)) # difference of two sets
# print(s)


# dictionaries --> key-value pairs
# x = {'name': 'jhon', 'age': 25, 'city': 'New York'}
# x['class'] = 'A' # add key-value pair
# x['numbers'] = [1,2,3,4,5] # add list as value
# print(x) # access value by key
# print(x.values()) # get all values
# print(x.keys()) # get all keys
# print(x.items()) # get all key-value pairs
# print('name' in x) # check if key is in dictionary
# del x['age'] # remove key-value pair
# for key, value in x.items(): # loop through dictionary
#     print(key, ':', value)



# comprehensions --> list, set, dictionary
# x = [x for x in range(5)]
# x = [[0 for x in range(5)] for y in range(3)]
# x = {x: x**2 for x in range(5)}
# x = {x for x in range(10) if x % 2 == 0}

# print(x)


# functions --> def , return
# def func():
#     print('Hello from function')
#     def inner_func(x = 2, y = 2):
#         print('Hello from inner function', x + y)
#     inner_func()

#     def myFunc(a, b):
#         return a + b, a - b, a * b, a / b
    
#     sum, diff, prod, quot = myFunc(10, 5)
#     print('Sum:', sum)
#     print('Difference:', diff)
#     print('Product:', prod)
#     print('Quotient:', quot)

# func()


# def anoFunc(x):
#     def nestedFunc():
#         return x
    
#     return nestedFunc

# x = anoFunc(10)
# print(x())


# def func(*args, **kwargs):
    
#     for arg in args:
#         print('arg:', arg)
    
#     for key, value in kwargs.items():
#         print('key:', key, 'value:', value)

# func(1, 2, 3, name='jhon', age=25)

# raise Exception('This is an exception')


#try except block
# try:
#     x = int(input('Enter a number: '))
#     y = int(input('Enter another number: '))
#     result = x / y
#     print('Result:', result)
# except ValueError:
#     print('Invalid input. Please enter numeric values.')
# except ZeroDivisionError:
#     print('Error: Division by zero is not allowed.')
# except Exception as e:
#     print('An unexpected error occurred:', str(e))
# finally:
#     print('Execution completed.')



# lambda functions --> anonymous functions

# lambda_func = lambda x, y: x + y
# result = lambda_func(5, 10)
# print('Result from lambda function:', result)



# map , filter , reduce
# x = [1, 2, 3, 4, 5]
# mp = map(lambda x: x + 2, x)
# mp = filter(lambda x: x % 2 == 0, x)

# print('Map result:', list(mp))




# fstrings --> formatted strings
# tim = 'world'
# x = f'hello, {6+8} {tim}'

# print(x)


# class and object oriented programming
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old.'
    
person1 = Person('Jhon', 25)
print(person1.greet())  


#python generics
from typing import TypeVar, Generic, List
T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # Output: 2
str_stack = Stack[str]()
str_stack.push('hello')
str_stack.push('world')
print(str_stack.pop())  # Output: world 