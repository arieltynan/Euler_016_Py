#Power digit sum

tot = 2**1000

digits = [int(dig) for dig in str(tot)]

ans = 0
for i in digits:
    ans = ans + i

print(ans)