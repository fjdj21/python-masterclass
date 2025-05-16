"""
Write a small program to ask for a {name} and {age}

When both values have been entered:
- check if the person is the right age to go on an 18-30 holiday
- They must be over 18 and under 31

If they are, welcome them to the holiday, otherwise:
- print a (polite) message refusing them entry.

Our program expect valid input. We'll see how to handle invalid numbers, later in the course
"""

#Variables, initializers
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# check if eligible for 18-30 holiday
if 18 <= age < 31: # is age between 18 - 30
    print(f"Hi {name}, you are eligible to go on an 18-30 holiday. \nWelcome and Enjoy your stay")
else:
    if age < 18: # 17 and under
        print(f"Sorry {name}, you are still a minor please comeback in {18 - age} years so you'll get to enjoy this holiday")
    else: # 31 and above
        print(f"Sorry {name}, this event is for people that are under 31. We hope you find another amazing holiday")
