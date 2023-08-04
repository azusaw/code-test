# A
s = input()
print("Yes" if s == 'ACE' or s == 'BDF' or s == 'CEG' or s == 'DFA' or s == 'EGB' or s == 'FAC' or s == 'GBD' else 'No')

# npC
n, m = list(map(int, input().split()))
al = tuple(map(int, input().split()))  # urite
bl = tuple(map(int, input().split()))  # kaite

al = sorted(al)
bl = sorted(bl)
tmp = 0
i = 0
p = 0

while True:
    if p != al[i]:
        p = al[i]
        tmp_a = sum(1 for a in al if a <= p)
        tmp_b = sum(1 for b in bl if b >= p)
        if tmp_a >= tmp_b != 0:
            tmp = p
            break
        if p > al[len(al) - 1]:
            break
    if i >= len(al) - 1:
        break
    i += 1
print(tmp if tmp != 0 else bl[len(bl) - 1] + 1)

# F
n, m = list(map(int, input().split()))
l0 = []
l1 = []
l2 = []
for i in range(n):
    a, b = list(map(int, input().split()))
    if a == 0:
        l0.append(b)
    elif a == 1:
        l1.append(b)
    elif a == 2:
        l2.append(b)

l0.sort(reverse=True)
l1.sort(reverse=True)
l2.sort(reverse=True)

h = 0
i = 0
j = 0
k = 0
s = 0
can = 0
l_l0 = len(l0)
l_l1 = len(l1)
l_l2 = len(l2)

while m > s:
    # choose normal item
    if l_l0 > 0 and i < l_l0 and (l_l1 == 0 or j >= l_l1 or l0[i] >= l1[j] or (m - s == 1 and can == 0)):
        h += l0[i]
        i += 1
        s += 1
        continue
    # choose can item
    elif l_l1 > 0 and j < l_l1 and can > 0:
        h += l1[j]
        can -= 1
        j += 1
        s += 1
        continue
    # choose can opener or...
    elif l_l2 > 0 and k < l_l2 and can == 0:
        # no more normal item
        if l_l0 == 0 or i >= l_l0:
            can += l2[k]
            k += 1
        # calculate which choice is better
        else:
            tmp_can = l2[k]
            tmp_l = l0[i:] + l1[j:j + tmp_can]
            tmp_l.sort(reverse=True)
            tmp_h_normal = sum(l1[i: i + m - s])
            tmp_h_can = sum(tmp_l[0: m - s - 1])
            if tmp_h_can > tmp_h_normal:
                can += tmp_can
                k += 1
            else:
                h += l0[i]
                i += 1
        s += 1
        continue
    break
print(h)
