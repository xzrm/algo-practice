def largest_rect(vals):
    upper_lim = len(vals)
    max_val = 0
    for i in range(upper_lim):
        curr_val = vals[i]
        d = []
        for j in range(i, 0, -1):
            if vals[j - 1] >= curr_val:
                d.append(vals[j - 1])
            else:
                break
        u = []
        for k in range(i, upper_lim):
            if vals[k] >= curr_val:
                u.append(vals[k])
            else:
                break
        tot = d + u
        max_val = max(max_val, len(tot) * vals[i])
    return max_val


vals = "8979 4570 6436 5083 7780 3269 5400 7579 2324 2116"
# vals = "6320 6020 6098 1332 7263 672 9472 28338 3401 9494"
# vals = "3 2 5 6 1 4 4"
vals = [int(i) for i in vals.split(" ")]
print(vals)
largest_rect(vals)
