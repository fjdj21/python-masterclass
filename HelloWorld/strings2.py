parrot = "Norwegian Blue"
# N o r w e g i a n _  B  l  u  e
# 0 1 2 3 4 5 6 7 8 9  10 11 12 13
# 4 3 2 1 0 9 8 7 6 5  4  3  2  1  in negative
# 0 in negative if -0 is called
print(parrot)

##challenge: output "we win" downwards, but use positive indexing
print(parrot[3]) # w index into the string [3]
print(parrot[4]) # e
print(parrot[9]) # _ <space>
print(parrot[3]) # w
print(parrot[6]) # i
print(parrot[8]) # n

print()

##challenge: output "we win" downwards, but use negative indexing
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
##challenge: still output "we win" but subtract it using the length of parrot which is 14
print(parrot[3 - len(parrot)]) # where len(parrot) = 14
print(parrot[4 - len(parrot)])
print(parrot[9 - len(parrot)])
print(parrot[3 - len(parrot)])
print(parrot[6 - len(parrot)])
print(parrot[8 - len(parrot)])

print()

# N o r w e g i a n _  B  l  u  e
# 0 1 2 3 4 5 6 7 8 9  10 11 12 13
# 4 3 2 1 0 9 8 7 6 5  4  3  2  1  in negative
# 0 in negative if -0 is called

print(parrot[0:6]) # Norweg | slice starting at index 0 and stop before index 6
print(parrot[3:5]) # we
print(parrot[0:9]) # Norwegian
# or we can print it by default without the 0, not providing a start value
print(parrot[:9])
print(parrot[:len(parrot)])
print(parrot[:len(parrot):2]) # N r e i n B u
print(parrot[2:3] + parrot [3:4]) # rw | basically concatenating the indexed characters
print(parrot[:6] + parrot[6:]) # N o r w e g + i a n _  B  l  u  e

letters = "abcdefghijklmnopqrstuvwxyz"


print()
print("Advanced String Slicing")
# N o r w e g i a n _  B  l  u  e
# 0 1 2 3 4 5 6 7 8 9  10 11 12 13
# 4 3 2 1 0 9 8 7 6 5  4  3  2  1  in negative
# 0 in negative if -0 is called
print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl
print(parrot[-4:9])    # Bl

print()
print("String slicing with step")
# N o r w e g i a n _  B  l  u  e
# 0 1 2 3 4 5 6 7 8 9  10 11 12 13
# 4 3 2 1 0 9 8 7 6 5  4  3  2  1  in negative
# 0 in negative if -0 is called
print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print([int(val) for val in values])

words = ["I", "love", "dogs"]
sentence = ' '.join(words).split()
print(sentence)
