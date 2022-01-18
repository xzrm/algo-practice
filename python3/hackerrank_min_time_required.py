import math


def calc_days(min_days, max_days, goal, machines):
    mid_days = (min_days + max_days) // 2

    if not min_days < max_days:
        return mid_days

    tot_prod = sum(mid_days // m for m in machines)

    if tot_prod >= goal:
        return calc_days(min_days, mid_days, goal, machines)
    else:
        return calc_days(mid_days + 1, max_days, goal, machines)


def minTime(machines, goal):
    machines, count = sorted(machines), len(machines)
    min_days = math.ceil(goal / count) * machines[0]
    max_days = math.ceil(goal / count) * machines[-1]

    return int(calc_days(min_days, max_days, goal, machines))
