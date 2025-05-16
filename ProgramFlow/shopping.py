shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

# for item in shopping_list:
#     if item != 'spam': # this is one approach
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break # if the current item is equal to spam, restart the for loop using the next value

    print("Buy " + item)
