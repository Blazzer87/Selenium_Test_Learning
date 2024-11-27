"""Задание:
Ввести массив целых чисел в диапазоне [-100,100]. Длина массива задается пользователем.
Найти минимальный элемент
"""


min_input = int(input('Введите МИНимальное значение массива (от -100 до 100 включительно): '))
while min_input > 100 or min_input < -100:
    print('Ошибка. Введите МИНимальное значение в диапазоне от -100 до 100 (включительно).')
    min_input = int(input('Ещё раз введите МИНимальное значение массива: '))


max_input = int(input('Введите МАКСимальное значение массива (от -100 до 100 включительно): '))
while max_input == min_input:
    print('МАКСимальное и МИНимальное значения не могут быть одинаковыми.')
    max_input = int(input('Ещё раз введите МАКСимальное значение массива: '))
while max_input > 100 or max_input < -100:
    print('Ошибка. Введите МАКСимальное значение в диапазоне от -100 до 100 (включительно).')
    max_input = int(input('Ещё раз введите МАКСимальное значение массива: '))

if max_input < min_input:
    x = -1
elif max_input > min_input:
    x = 1

user_range = range(min_input, max_input + x, x)
user_list = []

for z in user_range:
    user_list.append(z)

min_number = min(user_list)
print(f'Самое маленькое число в массиве = {min_number}')
exit()
