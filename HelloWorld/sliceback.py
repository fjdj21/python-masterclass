letters = "abcdefghijklmnopqrstuvwxyz"
length = len(letters) - 1 # 25

# a_b_c_d_e_f_g_h_i_j_k _l _m _n _o _p _q _r _s _t _u _v _w _x _y _z
# 0_1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25

# a_ b_ c_ d_ e_ f_ g_ h_ i_ j_ k_ l_ m_ n_ o_ p_ q_ r_s_t_u_v_w_x_y_z
# 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

print("Length: " + str(length)) # 25
result = ""
for i, char in enumerate(letters):
    if i == length:
        result += char
    else:
        result += char + "_"

print(result)

backwards = letters[length::-1]
print(backwards)
backwards = letters[::-1]
print(backwards)
backwards = letters[25:-27:-1]
print(backwards)

#challenge:
"""
Create a slice that produces the characters 'qpo', 
    'edcba', 
    last 8 characters in reverse order 'zyxwvuts'
    
letters = "abcdefghijklmnopqrstuvwxyz"
length = len(letters) - 1 # 25

# a_b_c_d_e_f_g_h_i_j_k _l _m _n _o _p _q _r _s _t _u _v _w _x _y _z
# 0_1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25

# a_ b_ c_ d_ e_ f_ g_ h_ i_ j_ k_ l_ m_ n_ o_ p_ q_ r_s_t_u_v_w_x_y_z
# 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
"""

a_slice = letters[16:13:-1]
b_slice = letters[4::-1]
c_slice = letters[:-9:-1]
slices = a_slice + " " + b_slice + " " + c_slice

print(slices.split())

computer_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mouse mat']
# then
print(computer_parts[1]) #outputs monitor
print(computer_parts[1][0])
