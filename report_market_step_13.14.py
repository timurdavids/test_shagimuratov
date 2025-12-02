#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 19:29:36 2025

@author: stimur
"""

'''
Итоговое задание №5
Используя полученные в этом блоке знания вам необходимо написать программу.

Представьте, что Вы работаете Data Engineer и ваша задача — разработать скрипт на Python, который выполняет анализ данных по покупкам в магазине. У вас есть набор данных о покупках, и вам нужно провести различные аналитические операции, чтобы предоставить отчет.

Есть вот такой вот список покупок.
item — название товара,
category — категория товара,
price — цена за единицу товара,
quantity — количество единиц, купленных за один раз.


purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

                  
Вам нужно реализовать несколько функций для анализа данных:

total_revenue(purchases): Рассчитайте и верните общую выручку (цена * количество для всех записей).
items_by_category(purchases): Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
expensive_purchases(purchases, min_price): Выведите все покупки, где цена товара больше или равна min_price.
average_price_by_category(purchases): Рассчитайте среднюю цену товаров по каждой категории.
most_frequent_category(purchases): Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
Ваш скрипт должен выводить отчёт по каждому из следующих пунктов:

Формат вывода должен соответствовать шаблону вида

Общая выручка: 21.0
Товары по категориям: {'fruit': ['apple', 'banana'], 'dairy': ['milk'], 'bakery': ['bread']}
Покупки дороже 1.0: [{'item': 'apple', 'category': 'fruit', 'price': 1.2, 'quantity': 10}, {'item': 'milk', 'category': 'dairy', 'price': 1.5, 'quantity': 2}, {'item': 'bread', 'category': 'bakery', 'price': 2.0, 'quantity': 3}]
Средняя цена по категориям: {'fruit': 0.85, 'dairy': 1.5, 'bakery': 2.0}
Категория с наибольшим количеством проданных товаров: fruit

В  ответе укажите ссылку на ваш git-репозиторий.
'''
import pandas as pd

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

'''
df = pd.DataFrame(purchases)
print(df)
'''

def total_revenue(purchases): 
    # Рассчитывает и возвращает общую выручку (цена * количество для всех записей).
    df = pd.DataFrame(purchases)
    res = sum(df['price'] * df['quantity'])
    print(f'Общая выручка: {res}')


'''
df = pd.DataFrame(purchases)
grouped = df.groupby('category')['item'].unique()
    
'''

def items_by_category(purchases): 
    # Возвращает словарь: ключ — категория, значение — список уникальных товаров в этой категории.
    
    df = pd.DataFrame(purchases)
    grouped = df.groupby('category')['item'].unique()
    # преобразуем numpy arrays в списки для удобства вывода
    return print('Товары по категориям: ', {cat: list(items) for cat, items in grouped.items()})


def expensive_purchases(purchases, min_price): 
    # Выводит все покупки, где цена товара больше или равна min_price.
    df = pd.DataFrame(purchases)
    return print(f'Покупки дороже {min_price}: {df[df['price'] >= min_price].to_dict(orient='records')}')
    
    
def average_price_by_category(purchases): 
    # Рассчитывает среднюю цену товаров по каждой категории.
    df = pd.DataFrame(purchases)
    avg = df.groupby('category')['price'].mean().round(2)
    return print(f'Средняя цена по категориям: {avg.to_dict()}')

def most_frequent_category(purchases):
    # Находит и возвращает категорию, в которой куплено больше всего единиц товаров 
    # (учитывайте поле quantity)
    df = pd.DataFrame(purchases)
    qty = df.groupby('category')['quantity'].sum()
    if qty.empty:
        return None
    return print(f'Категория с наибольшим количеством проданных товаров: {qty.idxmax()}')


# Вывод сформированного отчёта:
total_revenue(purchases)
items_by_category(purchases)

# min_price = float(input('Введите минимальную цену для товара: '))
# expensive_purchases(purchases, min_price) 

expensive_purchases(purchases, 1.3)
average_price_by_category(purchases)
most_frequent_category(purchases)

