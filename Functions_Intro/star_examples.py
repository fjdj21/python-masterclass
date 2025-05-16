from z_debuggers import ruler, banner

numbers = (0, 1, 2, 3, 4, 5) # this is a tuple

print(numbers, sep=";") # you are printing out the tuple
print(*numbers, sep=";") # you are unpacking the tuple numbers
print(0, 1, 2, 3, 4, 5, sep=";") #

ruler()

def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)
test_star(1)
print()
test_star()
