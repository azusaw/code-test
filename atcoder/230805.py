# A
n = (int, input().split())
l = list(map(int, input().split()))
max_n = max(l)

print(0 if max_n == l[0] and l.count(max_n) == 1 else max_n - l[0] + 1)

# B
n, m = map(int, input().split())
l = set([i for i in range(1, n + 1)])
for i in range(m):
    a, b = map(int, input().split())
    l.discard(b)
print(-1 if len(l) != 1 else l.pop())

# C
n = int(input())
l = list(map(int, input().split()))
ans = 0
l.sort()
ave_q = sum(l) // n
ave_r = sum(l) % n
for i, x in enumerate(l):
    base = ave_q if i < (len(l) - ave_r) else ave_q + 1
    if x >= base:
        break
    ans += base - x
print(ans)

# D
n, k = map(int, input().split())
rl = []
for i in range(n):
    if i == k + 1 and len(rl) > 0:
        fi = rl.pop(0)
        rl.append(fi)
    if i < k + 1:
        t = [j if j <= k + 1 else j % (k + 1) for j in range(i + 1, i + 1 + k)]
    else:
        t = [k + j for j in range(k - 1)] + [i + 1]
    t.sort()
    print("? " + ' '.join([str(n) for n in t]))
    res = int(input())
    if res == -1:
        exit()
    rl.append(res)

if len(rl) != n:
    print("-1")
    exit()

if k + 1 == n:
    fi = rl.pop(0)
    rl.append(fi)

al = []
base = sum(rl[:k + 1])
for i, r in enumerate(rl):
    if i < k + 1:
        al.append((base % 2 - r) % 2)
        continue
    elif i == k + 1:
        base = sum(al[len(al) - k + 1:])
    al.append((base - r) % 2)
print("! " + ' '.join([str(a) for a in al]))
