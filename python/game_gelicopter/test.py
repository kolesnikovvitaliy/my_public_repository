
n = int(input())
for i in range(n):
    for j in range(i): 
        print("*", end="")
        print()
        for k in range(i - 1):
            print("*", end="")
            
    print()    
