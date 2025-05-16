for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    #<n1>:<n2> where:
    #n1 = replacement field
    #n2 = field width

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
    #<n1>:<n2>'<,>,^' where:
    #n1 = replacement field
    #n2 = field width
    #< = left align
    #> = right
    #^ = center

print()

print("Pi is approximately {0:12}".format(22/7)) #default decimal point = 15
print("Pi is approximately {0:12f}".format(22/7)) #f = floating default value, 6 digit decimal point
print("Pi is approximately {0:12.50f}".format(22/7)) # ignores the field width, and python indicates that the precision
# is important
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
########################{<rf>:<width><.precisionFloating>
# maximum floating precision are between 51 and 53 digits
print("Pi is approximately {0:<72.54f}".format(22/7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

pi = "{:6f}".format(22/7)
print("Pi has a length of {} and is approximately_{:9f}".format(len(pi), 22/7))
## 3.142857 = 8 digits, so 1 space is added from the left

""""""""""""""""""""""""""""""""""""""""""

# Challenge
# using the same pi
# we want the user to do the following:
# 1. accept a user input for: width that will be used in replacement field argument
# 2. accept a user input for: floating point precision that will be used in field argument
# 3. accept a user input for: <, >, ^ for alignment, otherwise if the value is not in this 3 just output ''
# Create 1 - 3 as a function
# we want the output to be
# Pi has the length of {} and with {} padding spaces, we will use the replacement field method


# Get number from user for width and precision
def get_number(name):
    while True:
        input_number = input(f"Please enter a {name}: ").strip()
        if input_number.isdigit():
            number = int(input_number)
            if number != 0:
                return number
        print("Please enter a valid number aside from '0'")


# Get alignment from user
def get_alignment():
    alignments = ['<', '>', '^']
    while True:
        input_alignment = input("Please enter <, > or ^ for alignment: ").strip()
        if input_alignment in alignments:
            print("You chose:", input_alignment)
            return input_alignment
        else:
            print("Invalid input! Please enter '<', '>' or '^'")
            ##exit()


original_pi = 22/7
alignment = get_alignment()
width = get_number("width")
floating_precision = get_number("precision")

# Build the format for the replacement dynamically, then store the format string in formatted_pi
format_string = f"{{:{alignment}{width}.{floating_precision}f}}"
formatted_pi = format_string.format(original_pi)
print(format_string)
print(formatted_pi)

# get the total length of the formatted_pi
total_length = len(formatted_pi)
# count the padding spaces
padding_spaces = formatted_pi.count(" ")
print(f"Pi is approximately {formatted_pi}")
print(f"{formatted_pi} Pi has the total length of {total_length} and has the padding spaces of {padding_spaces}")
