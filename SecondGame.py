# Настройки
a = 1
b = 100
print(f'Я загадал число от {a} до {b}...')


# Определим свою функцию, которая напечатает правила
def print_rules1():
    rules = '''Если ты угадешь, игра закончится,
если мое число меньше, увидишь "<",
а если больше, то ">".'''
    print()
    print(rules)
    print()


# Даем время на подумать
import time

time.sleep(1)
print('Готов?')
time.sleep(1)
print('Тогда поехали!')
time.sleep(1)
print_rules1()
time.sleep(1)

# Поехали
import random

lucky_number = random.randint(a, b)
print(lucky_number)

counter = 1

while True:
    chance = input()
    if chance.isdigit():
        chance = int(chance)
        if chance not in range(a, b + 1):
            print('Не понял. На всякий случай напомню правила:')
            print(f'Я загадал число от {a} до {b}...')
            print_rules1()
            continue
        if chance == lucky_number:
            print(f'Bingo! Понадобилось {counter} попыток')
            break
        elif chance > lucky_number:
            print("<")
        elif chance < lucky_number:
            print(">")
        counter += 1
    else:
        print('Не понял. На всякий случай напомню правила:')
        print(f'Я загадал число от {a} до {b}...')
        print_rules1()
