#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Исходный словарь магазинов с распродажами
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ]
}

# Новый словарь, куда будем записывать найденные минимумы
sweets = {}

# Перебираем продукты в магазине "Ашан"
for product in shops['ашан']:
    product_name = product['name']
    
    # Получаем список цен продукта во всех магазинах
    prices_by_shop = [(shop, item['price']) for shop, items in shops.items() for item in items if item['name'] == product_name]
    
    # Сортируем список по цене
    sorted_prices = sorted(prices_by_shop, key=lambda x: x[1])
    
    # Берем первые два наиболее дешевых варианта
    top_two_shops = sorted_prices[:2]
    
    # Записываем в итоговый словарь
    sweets[product_name] = top_two_shops

# Печать результатов
for sweet, data in sweets.items():
    print(f"{sweet}:")
    for entry in data:
        print(f"\tМагазин: {entry[0]}, Цена: {entry[1]} руб.")