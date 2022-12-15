
for a in range(1, 33 + 1):
    for b in range(1, 33 + 1):
        for c in range(1, 33 + 1):
            for d in range(1, 33 + 1):
                if a != b and a != c and a != d and b != c and b != d and c != d:
                    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                            
                        print(a ** 3 + b ** 3, c ** 3 + d ** 3)
                