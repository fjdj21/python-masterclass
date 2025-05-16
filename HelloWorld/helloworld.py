print('Hello World!') #Output: Hello World!

## print is a function
### there are also multiple built-in functions available in python
### we can also create our own function
## 'Hello World!' is an argument passed to print function.
## the print() function can also hold multiple arguments

print(1 + 2) #Output: 3
print(7 * 6) #Output: 42
print() #Output: <blank>
print("The end", "or is it?", "keep watching to learn more about Python", 3) #Output: The end or is it? keep watching to learn more about Python 3

# def add(x, y):
#     return x + y
# print(add(5, 2))

# def my_print(message):
#     return str(message)
#
# print(my_print("Hello World!"))

# def my_print(*messages):
#     output = " ".join(str(m) for m in messages)
#     return output
#
# result = my_print("Hello", "world", 123, ["abc"])
# print(result)

# fruits = ("apple", "banana", "cherry")
# for fruit in fruits:
#     print(fruit)

x = str(3.5)
print(x)

myMessages = ("Test", "test1")
x = "#".join(myMessages)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

a = "Hello, World!"
print(a[1])
