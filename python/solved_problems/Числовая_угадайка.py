import random


def is_valid(x: str, k = 100):
    if x.isdigit():
        if 1 <= int(x) <= k:
            return True
    else:
        return False


def play():
    while True:
        k = input('Укажите диапазон в котором я буду загадывать число от 1 до ')
        if is_valid(k):
            break
        else:
            print('А может быть все-таки введем целое число ?')
            continue
    counter = 0
    n = random.randint(1, int(k))
    print(f'Я загадал число в диапазоне от 1 до {k}')
    while True:
        x = input(f'Введите целое число от 1 до {k}: ')
        if is_valid(x, int(k)):
            x = int(x)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {k}?')
            continue
        if x < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
            continue
        if x > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
            continue
        if x == n:
            counter += 1
            print(f'Вы угадали c {counter} раз, поздравляем!')
            break
    return


print('Добро пожаловать в числовую угадайку')
answer = 'y'
while answer == 'y':
    play()
    answer = input('Играем ещё ? (y - да, n - нет): ')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')