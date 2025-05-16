# import
from collections import Counter

### Mini Challenge
# 1. Create a program wherein we will store each character inputted by a user
# 2. If the letter exists in the phrase "Norwegian Blue", store it in a list
# 3. Count how many times each character appears in the phrase (excluding spaces)
# 4. If the user enters the same character more times than it appears in the phrase,
#    prompt them: "⚠️ Character '{letter}' has already been used {x} time(s), which is the maximum in 'Norwegian Blue'."
# 5. Show remaining letters that the user still needs to input
# 6. Once all characters in "Norwegian Blue" (with correct count) are entered, end the program with a success message

parrot = "Norwegian Blue"
used_letters = []  # To store each character entered by user

# Convert parrot to lowercase for consistent comparison
# remove spaces for clean counting
parrot_lower = parrot.lower().replace(" ", "")  # outputs: norwegianblue
allowed_letters = Counter(parrot_lower)  # e.g., {'n': 2, 'o': 1, ...}
print(f"These are the counter for each letter in '{parrot_lower}': {allowed_letters}")
user_letter_counts = Counter()

def display_remaining_letters():
    remaining = {letter: allowed_letters[letter] - user_letter_counts.get(letter, 0)
                 for letter in allowed_letters if allowed_letters[letter] > user_letter_counts.get(letter, 0)}
    return ', '.join([f"{k}({v})" for k, v in sorted(remaining.items())])

while True:  # while this is True, execute the logic inside, otherwise exit
    # convert the user_input to lowercase e.g., A -> a
    # strip extra spacing entered by user e.g., ' A' -> 'a' considered the lower() method here
    user_input = input(f"\nEnter a letter from {parrot} (or type 'exit' to quit): ").lower().strip()

    # exit the while loop if user entered 'exit' or "", ''
    if user_input in ("exit", ""):
        break

    # Validate input: must be a single alphabetic character
    # len(user_input) != 1, validate that if user entered a character length that is not equal to 1 (e.g., ab)
    # not user_input.isalpha, validate that if user entered an alphabetic character convert it to false
    # e.g., a = false, 1 = true
    if len(user_input) != 1 or not user_input.isalpha():
        print(f"❌ Please enter a single alphabetic character only.")
        continue  # if this is true, restart the while loop

    # Check if letter is not in "Norwegian Blue"
    if user_input not in parrot_lower:  # e.g., z = true, restart while loop
        print(f"❌ '{user_input}' is not in the phrase '{parrot}'. Try again.")
        continue

    # Check if the letter has already been entered as many times as allowed
    if user_letter_counts[user_input] >= allowed_letters[user_input]:
        print(f"⚠️ Character '{user_input}' has already been used {user_letter_counts[user_input]} time(s), which is the maximum in '{parrot}'.")
        print(f"Used so far: {''.join(used_letters)}")
        print(f"📝 Remaining: {display_remaining_letters()}")
        continue

    # Add valid input to used letters and update the count
    used_letters.append(user_input)
    user_letter_counts[user_input] += 1
    print(f"✅ Good job! Stored: {''.join(used_letters)}")
    print(f"📝 Remaining: {display_remaining_letters()}")

    # Check if all required letters from parrot have been used the correct number of times
    if all(user_letter_counts[char] == allowed_letters[char] for char in allowed_letters):
        print(f"\n🎉 Congrats! You’ve entered all the letters in '{parrot}' correctly!")
        break

# Final output based on used letters
if not used_letters:
    print("You have not entered any letters from 'Norwegian Blue'")
else:
    print(f"\n✅ Program ended. Letters you entered from '{parrot}':", ''.join(used_letters))
