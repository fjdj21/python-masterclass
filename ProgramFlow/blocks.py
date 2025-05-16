# for i in range(1,13):
#     print("No. {:>2} square is {:>3} and cubed is {:<4}".format(i, i ** 2, i ** 3))
# print("*" * 80)

## Declare your variables here:
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

## challenge:
## Create a function that will store {name} and {age}
## We will use this function in the condition

## Add functions here
def get_user_info():
    while True:
        name = input("Please enter your name: ").strip()
        if not name.isdigit():
            break
        print("You entered a digit, please enter your name.")

    # Get age
    while True:
        age_input = input("Hi {}, how old are you?: ".format(name)).strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Invalid age. Please enter a numeric value.")

    return name, age

## Call the function and store the returned values
name, age = get_user_info()

## Add conditional flow here
if age == 900:
    print(f"{age}?! aren't you an immortal being {name}?")
elif age >= 18:
    print("Your age is {}, You are old enough to vote! {} :)".format(age,name))
    print("Please put an X in the box")
else:
    print(f"Your age is {age}, please comeback after {18 - age} years {name}")
