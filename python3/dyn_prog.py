def lis(A):
    L = [1] * len(A)
    print(f"{L=}")

    for i in range(1, len(L)):
        subproblems = []
        for k in range(i):
            print(f"{A[k]=}  {A[i]=}")
            if A[k] < A[i]:
                subproblems.append(L[k])
        L[i] = 1 + max(subproblems, default=0)
    return max(L, default=0)
