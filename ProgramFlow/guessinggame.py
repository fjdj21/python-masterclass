# Declare variables here
answer = 5

# prints here
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first time")
else: #guess != answer
    if guess < answer:
        print("Please guess higher")
    else: # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")



# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# while True:
#     guess = int(input())
#     if guess < answer:
#         print("Please guess higher")
#     elif guess > answer:
#         print("Please guess lower")
#     else:
#         print("You got it first time")
#         break
