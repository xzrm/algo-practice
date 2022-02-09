def biggerIsGreater(w):
    if len(set(w)) == 1:
        return "no answer"
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    if i <= 0:
        return "no answer"

    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1

    chars = list(w)
    chars[i - 1], chars[j] = chars[j], chars[i - 1]
    w = chars[:i] + list(reversed(chars[i:]))
    return "".join(w)


print(biggerIsGreater("dkhc"))
