a, b = int(input()), int(input())
s1 = 0
s2 = 0
for i in range(a, b + 1):
    z = 0
    for j in range(1, i + 1):
        if i % j == 0:
            z += j
            if z >= s1:
                s1 = z
                s2 = j
print(s2, s1)
