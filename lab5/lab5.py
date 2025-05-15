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