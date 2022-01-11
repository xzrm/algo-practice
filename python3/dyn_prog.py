def lis(A):
    L = [1]*len(A)
    print(f'{L=}')

    for i in range(1, len(L)):
        print(f'{i=}')
        print(f'{list(range(i))=}')
        print(f'przed {L=}')
        subproblems = []
        for k in range(i):
            print(f'{A[k]=}  {A[i]=}')
            if A[k] < A[i]:
                subproblems.append(L[k])
        #subproblems = [L[k] for k in range(i) if A[k] < A[i]]
        print(f'{subproblems=}')
        L[i] = 1 + max(subproblems, default=0)
        print(f'{L[i]}')
        
        print(f'po {L=}')
        print('-' * 10)
    return max(L, default=0)


