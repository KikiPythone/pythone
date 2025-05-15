#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Список членов семьи
my_family = ["Мама", "Я", "Папа"]

# Список списков с ростом членов семьи
my_family_height = [
    ["Мама", 160],  # рост мамы
    ["Я", 160],     # мой рост
    ["Папа", 170]   # рост папы
]

# Извлекаем рост отца (он третий элемент списка)
father_height = my_family_height[2][1]

# Вычисляем общую высоту всех членов семьи
total_family_height = sum([height for _, height in my_family_height])

# Выводим результаты
print(f'Рост отца - {father_height} см')
print(f'Общий рост моей семьи - {total_family_height} см')