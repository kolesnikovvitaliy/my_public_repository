import random as rnd
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова",
           "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать",
           "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять",
           "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Назови свое имя: ')
print(f'Приветствую тебя, о {name}!')
again = 'y'
while again.lower() == 'y':
    print('Ты можешь задать свой вопрос:')
    _ = input()
    print(f'На это я могу ответить: {rnd.choice(answers)}...')
    again = input(f'Есть ли у тебя еще вопросы, о {name}? (y = да, n = нет): ')

print(f'Возвращайся если возникнут вопросы, уважаемый {name}!')