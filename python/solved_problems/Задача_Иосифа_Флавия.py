n, k = int(input()), int(input())
a = 0
for i in range(1, n + 1):
    a = (a + k) % i
print(a + 1)