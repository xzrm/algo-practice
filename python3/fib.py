import time


def fib(n):
    if n in {0, 1}:
        return n
    prev = 0
    fib_n = 1
    fib_o = 1
    for _ in range(2, n + 1):
        fib_n = prev + fib_o
        prev = fib_o
        fib_o = fib_n

    return fib_n


def fib_recur(n):
    if n in {0, 1}:
        return n

    return fib_recur(n - 1) + fib_recur(n - 2)


cache = {0: 0, 1: 1}


def fib_recur_cached(n):
    if n in cache:
        return cache[n]

    cache[n] = fib_recur_cached(n - 1) + fib_recur_cached(n - 2)
    return cache[n]


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if n < len(self.cache):
            return self.cache[n]

        v = self(n - 1) + self(n - 2)
        self.cache.append(v)

        return self.cache[n]


n = 40
# s = time.time()
# print([fib_recur(n) for n in range(n)])
# e = time.time()
# print(e - s)


s = time.time()
print([fib_recur_cached(n) for n in range(n)])
e = time.time()
print(e - s)


s = time.time()
f = Fibonacci()
print([f(n) for n in range(n)])
e = time.time()
print(e - s)
