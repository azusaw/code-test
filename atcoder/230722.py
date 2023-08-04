# A
n, p, q = list(map(int, input().split()))
d = list(map(int, input().split()))

min_p = q + min(d)
print(min_p if min_p < p else p)

# B
import sys

n, m = list(map(int, input().split()))
l = []
for i in range(n):
    s = list(map(int, input().split()))
    l.append([s[0], s[1], set(s[2:])])
for i in l:
    for j in l:
        if i == j:
            continue
        if i[0] >= j[0] and (i[2] & j[2] == i[2]):
            print("Yes")
            sys.exit(0)
print("No")

# C
n = int(input())
s = set()
for i in range(n):
    x = input()
    if x[::-1] in s:
        continue
    s.add(x)
print(len(s))

# D
import math

n, t, m = list(map(int, input().split()))
for i in range(m):
    a, b = list(map(int, input().split()))

mn = list(n // t for i in range(t))
for i in range(n % t):
    mn[i] += 1

ans = 1
pmn = 0
for cmn in mn:
    print(mn)
    print(n - pmn, cmn)
    ans *= math.comb((n - pmn), cmn)
    pmn += cmn

print(ans / math.comb())
