def selection_sort_rev(A):
    for i in reversed(range(len(A))):
        idx = find_max_idx(A[: i + 1])
        A[i], A[idx] = A[idx], A[i]
    print(A)


def selection_sort_recur(A, i=None):
    if i is None:
        i = len(A) - 1
    if i > 0:
        idx = find_max_idx(A[: i + 1])
        A[i], A[idx] = A[idx], A[i]
        selection_sort_recur(A, i - 1)
    return A


def selection_sort(A):
    for i in range(len(A)):
        idx = find_min_idx(A[i:])
        A[i], A[i + idx] = A[i + idx], A[i]

    print(A)


def find_max_idx(A):
    max_idx = 0
    for i in range(len(A)):
        if A[i] > A[max_idx]:
            max_idx = i

    return max_idx


def find_min_idx(A):
    idx = 0
    for i in range(len(A)):
        if A[i] < A[idx]:
            idx = i

    return idx


A = [7, 1, 5, 8, 2]
# print(find_max_idx(A))
# selection_sort(A)
print(selection_sort_recur(A))
