from typing import List


b_r = {")": "(", "]": "["}


def find_idx_left(s: str) -> int:
    vals = [i for i in [s.find("("), s.find("[")] if i >= 0]
    return -1 if len(vals) == 0 else min(vals)


def find_idx_right(s: str) -> int:
    vals = [i for i in [s.rfind(")"), s.rfind("]")] if i >= 0]
    return -1 if len(vals) == 0 else max(vals)


def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    idx_l = find_idx_left(my_string)
    idx_r = find_idx_right(my_string)
    if idx_r < idx_l:
        return False

    if idx_l == -1 and idx_r == -1:
        return True

    l_1 = my_string[idx_l]
    l_2 = my_string[idx_r]

    if not all([i >= 0 for i in [idx_l, idx_r]]):
        return False

    if not l_1 == b_r[l_2]:
        return False

    s = my_string[idx_l + 1 : idx_r]
    print(s)

    return balanced_brackets(s)
