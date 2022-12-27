n = int(input())
a1, a2, a3, a4 = 0, 0, 0, 0
for i in range(n):
    x, y = input().split()
    if int(x) > 0 and int(y) > 0:
        a1 += 1
    elif int(x) < 0 and int(y) > 0:
        a2 += 1
    elif int(x) < 0 and int(y) < 0:
        a3 += 1
    elif int(x) > 0 and int(y) < 0:
        a4 += 1
print("Первая четверть:", a1,'\n'"Вторая четверть:", a2,'\n'"Третья четверть:", a3,'\n'"Четвертая четверть:", a4)












# Первая четверть: 2
# Вторая четверть: 2
# Третья четверть: 1
# Четвертая четверть: 2
