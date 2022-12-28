def pascal(num):
    m = []
    for i in range(num + 1):   
        row = [1]*(i+1)   
        for j in range(i+1):
            if j!=i and j!=0:
                row[j] = m[i-1][j-1]+m[i-1][j]
        print(*row)
        m.append(row)
        

n = int(input())
pascal(n)