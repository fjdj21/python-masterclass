# for each i:
# - start at 0
# - in steps of 2
# - up to but not including 10
### if no start value is provided, the default value of start is set to 0
### if a step value will be provided, a start value must be provided (e.g., 0, 10, 2 | 10, 0, -2)
for i in range (10, 0, -2):
    print(f'i is now {i}')

age = int(input("How old are you? "))

if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

    print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")
