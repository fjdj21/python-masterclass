def string_manipulation(s):
    s = s.replace('a', 'b') # output: bbcbbc
    s = s.replace('b', 'c') # output: cccccc
    s = s.replace('c', 'a') # output: aaaaaa
    return s

s = "abcabc"
print(string_manipulation(s))
