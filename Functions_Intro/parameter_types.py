def func(p1, p2, *args, k, **kwargs):
    print(f"positional-or-keyword:....{p1}, {p2}")
    print(f"var-positional (*args):...{args}")
    print(f"keyword:..................{k}")
    print(f"var-keyword:..............{kwargs}")


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)
"""
positional-or-keyword:....1, 2
var-positional (*args):...(3, 4, 5, 9)
keyword:..................6
var-keyword:..............{'key1': 7, 'key2': 8}
"""
