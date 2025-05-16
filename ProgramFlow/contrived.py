numbers = [1, 45, 32, 12, 60, 40]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print(f"The numbers: {number} are unacceptable")
        continue #skip after printing the value in iteration, reset the loop
else:
    print(f"All those numbers: {number} are fine")
