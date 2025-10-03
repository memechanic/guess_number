from random import randint

target = randint(1, 100)

print('Угадай число от 1 до 100!')

while True:
    guess = int(input('Введите число: '))

    if guess < target: print('Число больше чем ваше!')
    elif guess > target: print('Число меньше чем ваше!')
    else:
        print('Вы угадали число!')
        break