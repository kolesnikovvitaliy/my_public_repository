def print_digit_sum(num):
    c = 0
    while num > 0:
        c += num % 10
        num //= 10
    print(c)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)