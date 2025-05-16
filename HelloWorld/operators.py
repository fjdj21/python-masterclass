a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print()

# for i in range(1, a // b):
#     print(i)

print(a + b / 3 - 4 * 12)   # -35.0
# 12 + (3 / 3) - (4*12)
# 12 + 1 - 48
# 13 - 48 = -35.0

print(a + (b / 3) - (4 * 12)) # -35.0 since multiplication has higher precedence
print((((a + b) / 3) - 4) * 12) # if we want this to be multiple left to right, we insert each expression in a parenthesis first
print(((a + b) /3 - 4) * 12)

# or we can try to do this first left to right
c = a + b # 12 + 3 = 15
d = c / 3 # 15 / 3 = 5
e = d - 4 # 5 - 4 = 1
print(e * 12) # 1 * 12 = 12

print()

print(a / (b * a) / b)
