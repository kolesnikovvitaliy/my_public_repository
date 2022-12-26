eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = [" ", ",", ".", "!", "?"]




print("Введите фразу")
f = input()


def chru(f):
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j].isalpha():
                if f[i][j] == f[i][j].upper():
                    for m in range(26):
                        if f[i][j] == eng_upper_alphabet[m]:
                            print(eng_upper_alphabet[(m+len(f[i]))%26], end = '')
                            break
                elif f[i][j] ==f[i][j].lower():
                    for m in range(26):
                        if f[i][j] == eng_lower_alphabet[m]:
                           print(eng_lower_alphabet[(m+len(f[i]))%26], end = '')
                           break
        else:
            print(f[i][j], end='')

chru(f)