# # Original list
# original = ['b', 'a', 'c']
#
# # --- Using .sort() ---
# print("Before .sort():")
# for idx, val in enumerate(original):
#     print(f"Index {idx}: {val}")
#
# sort_list = original.copy()
# sort_list.sort()  # This sorts the copy, not the original list
# # original.sort()  # Uncomment this if you want to sort the original list
#
# print("\nAfter .sort():")
# for idx, val in enumerate(sort_list):  # Now sorting the copy (sort_list)
#     print(f"Index {idx}: {val}")
#
# # --- Using sorted() ---
# sorted_list = sorted(original)  # new sorted list
#
# print("\nOriginal list unchanged:")
# for idx, val in enumerate(original):
#     print(f"Index {idx}: {val}")
#
# print("\nNew list from sorted():")
# for idx, val in enumerate(sorted_list):
#     print(f"Index {idx}: {val}")

# Original list
original = ['b', 'a', 'c']
abc = 'abcd'

# --- Using sorted() while retaining original indexes ---
indexed = enumerate(original)  # [(0, 'b'), (1, 'a'), (2, 'c')]
print(indexed)

indexed = list(abc)
print(indexed)

indexed = list(enumerate(original))  # [(0, 'b'), (1, 'a'), (2, 'c')]
print(indexed)

# Sort by the value (not by the index)
sorted_indexed = sorted(indexed, key=lambda x: x[1])

print("\nSorted list with original indexes:")
for idx, val in sorted_indexed:
    print(f"Original Index {idx}: {val}")
