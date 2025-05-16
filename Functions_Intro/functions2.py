def multiply(x, y):
    result = x * y
    return int(result)


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """Approach 1"""
    # # iterate each character and filter if that char is an alnum()
    # s = ''.join(char for char in sentence if char.isalnum())
    #
    # return is_palindrome(s)

    """Approach 2"""
    # use a for loop to iterate each character in a sentence
    string = "" # initialize, this is where each character will be stored
    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string) # called is_palindrome(string)


# Test data:
#   - A man,    a plan,    a canal: Panama!
#   - babcvsda21

word = input("Please enter a word to check: ")
# Check if input is not a string (e.g., #@!, 123)
if palindrome_sentence(word):
    print(f"{word} is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
