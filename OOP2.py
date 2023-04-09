# <iostream>
# <locale.h>
#coding=windows-1251
from pprint import pprint
with open ('OOP2.txt', 'r', encoding='utf-8') as file:
    cook_book={}
    for dish in file:
        dish_name=dish.strip()
        amount_ingredients=int(file.readline().strip())
        ingredients=[]
        for _ in range(amount_ingredients):
            product, amount, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'product' : product,
                'amount' : amount,
                'measure' : measure
            })
        file.readline()
        cook_book[dish_name]=ingredients
    pprint(cook_book)  






def get_shop_list_by_dishes(dishes, person_count):
    for_person={}
    list=[]
    for name, products in cook_book.items():
        if name in dishes:
            for prod in products:
                if prod['product'] in for_persons:
                    for_person[prod['product']]['quantity']+=int(prod['quantity'])*person_count
                else:
                    for_persons[prod['product']]=({prod['product'] : {'meassure' : prod['measure'], 'quantity' : prod['quantity']}})
    print(list)
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)                        




