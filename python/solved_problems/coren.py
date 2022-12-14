# n = int(input())
# s = 0
# a = 0
# b = 0
# while n > 0:
#     s += n % 10
#     n //= 10   
# if s <= 9:
#     print(s)
# elif s > 9:
#     while s > 0:
#         a += s % 10
#         s //= 10    
#     if a <= 9:
#         print(a)
#     else:
#         while a > 0:
#             b += a % 10
#             a //= 10    
#         print(b)      

n=int(input())      
while n > 9:                   
    s = 0    
    while (n > 0):
        s += n % 10      
        n = n // 10          
    n = s
print(n)