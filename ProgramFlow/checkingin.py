## Declare and/or initialized variable here
parrot = "Norwegian Blue"
used_letters = [] # this will store each character that was entered by user

letter = input("Enter character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
