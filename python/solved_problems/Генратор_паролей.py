# генератор с обязательным наличием в пароле выбираемых групп символов 
# и их пропорциональным (в зависимости от длины пароля) содержанием в нем
import random

def gen_psw(d_psw, lens, chars):
    for _ in range(d_psw):
        password = []
        for _ in range(lens//len(chars)+1):
            for i in range(len(chars)):
                if len(password) != lens:
                    password.append(random.choice(chars[i]))
        random.shuffle(password)
        print(*password, sep = '')

chars = []

d_psw = int(input('Какое количество паролей вам требуется сгенерировать ? -->'))
lens = int(input('Требуемая длина пароля (минимальная = 6) ? -->'))
if lens < 6:
    lens = 6
if input('Включать ли цифры ? (y/no) -->').lower() == 'y':
    chars.append("23456789")
if input('Включать ли прописные буквы ? y/no) -->').lower() == 'y':
    chars.append("ABCDEFGHIJKMNPQRSTUVWXYZ")
if input('Включать ли строчные буквы ? y/no) -->').lower() == 'y':
    chars.append("abcdefghjkmnpqrstuvwxyz")
if input('Включать ли символы "!#$%&*+-=?@^_" ? y/no) -->').lower() == 'y':
    chars.append("!#$%&*+-=?@^_")
if input('Исключать ли неоднозначные символы "il1Lo0O" ? y/no) -->').lower() == 'n':
    chars.append('il1Lo0O')
gen_psw(d_psw, lens, chars)