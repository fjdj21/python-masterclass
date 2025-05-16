# for index, character in enumerate("abcdefgh"):
#     print(index, character)

for t in enumerate("abcdefgh"):
    print(t)

"""
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
(5, 'f')
(6, 'g')
(7, 'h')
"""

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

"""
unpacked the 't' tuple to index and character
0 a
1 b
2 c
3 d
4 e
5 f
6 g
7 h
"""

index, character = (0, 'a')
print(index)
print(character)

"""
0
a
"""
