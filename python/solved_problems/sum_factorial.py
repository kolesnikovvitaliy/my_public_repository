# from math import factorial
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += factorial(i)
# print(s)
n = int(input())           
s = 0                    
factorial = 1                
for i in range(1, n + 1):    
    for j in range(1, i + 1):  
        factorial *= j       
    s += factorial       
    factorial = 1            
print(s)