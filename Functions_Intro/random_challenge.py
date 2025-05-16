# text = "WELCOME"
#
# print(text.center(30, '='))

title = input("Enter a title: ")
width = int(input("Enter width: "))

print('*' * width)
print('*' + title.center(width - 2, ' ') + '*')
print('*' * width)
