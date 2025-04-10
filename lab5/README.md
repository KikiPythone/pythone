# Задание
Написать код, который являлся бы генератором простых чисел. Затем он бы Просуммировал возвращаемые числа. К генератору должна быть применена хотя бы одна из функций : map, reduce, filter. 

Описание 
я создала код, используя функцию, которая проверяет на простое число,затем поставила лимит 101,и все полученные простые числа сложила в новом списке , благодаря функции reduce
Решение
```python
from functools import reduce

# Функция для проверки простоты числа
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(limit):
    for number in range(2, limit+1):
        if is_prime(number):
            yield number
            # return number

limit = 100  # Задаем предел (можно изменить)
primes = list(prime_generator(limit))

# Используем функцию reduce для суммирования всех простых чисел
total_sum = reduce(lambda x, y: x + y, primes)
print("Сумма всех простых чисел до", limit, "равна:", total_sum)
x=prime_generator(limit)
print(next(x))
print(next(x))
print(next(x))
def add(n,limit):
    return n+limit
total_sum = reduce(add, primes)
print("Сумма всех простых чисел до", limit, "равна:", total_sum)
```
Скриншот
![Alt text](image.png)
Шпаргалка по Github

## Используемые источники:
https://clck.ru/MfEMS
https://skillbox.ru/media/code/mnozhestva-v-python-vvodnyy-gayd-dlya-nachinayushchikh/
https://github.com/cyberspacedk/Git-commands

# Шпаргалка по работе с командами git
git clone https://github.com/Agmongui/python/tree/main/lab01
git add 10_store.py
git status
git push
git commit -m "Name of commit" 
