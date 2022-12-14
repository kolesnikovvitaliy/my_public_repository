total = 0
for a in range(1, 151):
    a5 = a ** 5
    for b in range(a, 151):
        b5 = b ** 5
        for c in range(b, 151):
            c5 = c ** 5
            for d in range(c, 151):
                d5 = d ** 5
                s = a5+b5+c5+d5
                for e in range(d, 151):
                    e5 = e ** 5                    
                    if s < e5: 
                        break
                    if s == e5:
                        total += 1
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
                        print(a+b+c+d+e)
print('Общее количество натуральных решений =', total)


