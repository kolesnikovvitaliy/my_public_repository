# объявление функции
def is_valid_password(password):
    flag = True
    a = password.split(':')
    if len(a) != 3:
        return False
    if a[0] != a[0][::-1]:
        return False
    if int(a[1]) == 1:
        return False
    d = 2
    while int(a[1]) % d != 0:
        d += 1
    if d != int(a[1]):
        return False

    if int(a[2]) % 2 != 0:
        return False
    return flag
        

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))






# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
