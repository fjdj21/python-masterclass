# ✍️ Challenge #1: Filtering
# Task:
#
# From the list words = ["cat", "bat", "apple", "ant", "dog"],
# keep only the words that start with the letter "a".
#
# Write a list comprehension for that.

words = ["cat", "bat", "apple", "ant", "dog"]
filtered = [word for word in words if word.startswith("a")]

print(filtered)

# ✍️ Challenge #2: Conditional Expression
# Task:
#
# From the list numbers = [1, 2, 3, 4, 5],
# return a new list where odd numbers become 0, and even numbers stay the same.

numbers = [1, 2, 3, 4, 5]
replaceOddNumbers = [n if n % 2 == 0 else 0 for n in numbers]

print(replaceOddNumbers)

for n in numbers:
    print(f"{n} % 2 = {n % 2}")
