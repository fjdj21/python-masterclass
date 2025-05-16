# number = "9,223;372:036 854,775;807"
# separators = ""
#
# for char in number:
#     if not char.isdigit():
#         separators += char
#
# print("Separators:", separators)
#
# def getSeparator():
#     number_input = input("Please enter a number with separator: ")
#     separators1 = ""
#     for char in number_input:
#         if not char.isdigit():
#             separators1 += char
#     return separators1
#
# print("Separators: ", getSeparator())

def getSeparator2():
    number_input = input("Please enter a number with separator: ")
    separators2 = ''.join([character for character in number_input if not character.isdigit()])

    if separators2:
        print("Separators found:", separators2)
    else:
        print("No separators found.")
    return separators2

getSeparator2()
