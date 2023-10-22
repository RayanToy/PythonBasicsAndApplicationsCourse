'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com.

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе. Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:

http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:

http://numbersapi.com/999/math?json=true

Пример входного файла:

31
999
1024
502
﻿Пример выходного файла:

Interesting
Boring
Interesting
Boring
'''

import requests
with open('dataset_24476_3.txt') as file:
    lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
for line in lines:
    res = requests.get(f'http://numbersapi.com/{line}/math?json=true')
    data = res.json()
    if not data['found']:
        print('Boring')
    else:
        print('Interesting')
