# A
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
n = int(input())
print(pi[:n + 2])

# B
n = int(input())
ll = []
for i in range(n):
    c = int(input())
    cl = list(map(int, input().split()))
    ll.append((i + 1, cl, c))
x = int(input())
tl = [l for l in ll if x in l[1]]
tl.sort(key=lambda val: val[2])
al = [str(l[0]) for l in tl if l[2] == tl[0][2]]
print(len(al))
print(" ".join(al))

# C
n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))

ll = [[] for i in range(m)]
for i in range(n):
    ll[c[i] - 1].append(i)
for l in ll:
    t = l.pop(-1)
    l.insert(0, t)
ans = [i for i in range(n)]
for i, n in enumerate(c):
    idx = ll[n - 1].pop(0)
    ans[i] = s[idx]
print("".join(ans))

# D
n = int(input())
s = input()
q = int(input())

l = []
loi = 0
lo = ""
for i in range(q):
    t, x, c = map(str, input().split())
    l.append([t, x, c])
    if t != '1':
        loi = i
        lo = t

ns = '' + s
for i, (t, x, c) in enumerate(l):
    if i != loi and t != '1':
        continue
    if t == '1':
        ns = ns[:int(x) - 1] + c + ns[int(x):]
    elif t == '2':
        ns = ns.lower()
    elif t == '3':
        ns = ns.upper()
print(ns)
