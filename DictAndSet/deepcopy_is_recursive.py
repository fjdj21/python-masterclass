from z_debuggers import banner, ruler
from custom_deepcopy_challenge import my_deepcopy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")
original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")
print("Original Copy", original)
print("Copy - 1", copy_1)
print("Copy - 2", copy_2)
