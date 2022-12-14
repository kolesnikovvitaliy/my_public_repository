total = 0
for n in range(1, 100):
    for k in range(1, 100):
        for m in range(1, 100):
            if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
                total += 1
                print('n =', n, 'k =', k, 'm =', m)
print('Общее количество натуральных решений =', total)