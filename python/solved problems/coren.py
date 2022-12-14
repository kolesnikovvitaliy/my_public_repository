n = int(input())
s = 0
a = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)
if s >= 9:  
    while s // 10 == 0: 
        a += s % 10
        s //= 10 
        a += s
    print("a", a)
else:
    print("s", s)
