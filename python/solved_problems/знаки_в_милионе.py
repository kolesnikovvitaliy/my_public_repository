n = input()
a = []
if len(n) <= 3:
    print(n)
else:
    a.append(n[:len(n) % 3])
    n = n[(len(n) % 3):]
    for i in range((len(n) // 3)):
        a.append(n[:3])
        n = n[3:]
    if a[0] == '':
        a.remove(a[0])
    print(*a, sep=",")



