from typing import List

numbers = [1, 3, 4, 5, 10, 11]


def add_num_to_list(numbers: List[int]) -> List[int]:
    if len(numbers) % 5 == 0:
        print("returning")
        return numbers
    val = numbers[-1] + 1
    print(f"adding {val}")
    numbers.append(val)
    return add_num_to_list(numbers)


def recursive_sum(number: int) -> int:
    if number <= 1:
        return number
    return number + recursive_sum(number - 1)
