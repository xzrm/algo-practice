def merge(L, R, A):
    i, j, k = 0, 0, 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

    print(f"{A=}")
    return A


# A = [0] * 2
# L = [5]
# R = [1]

# merge(L, R, A)


def merge_sort(A):
    if len(A) < 2:
        return A

    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]
    l = merge_sort(L)
    r = merge_sort(R)
    a = merge(l, r, A)
    return a


A = [3, 5, 9, 1, 1, 8, 2, 1]
print(merge_sort(A))
