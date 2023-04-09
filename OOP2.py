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




#print(cook_book['Омлет'])

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




# for key, val in cook_book.items():
#     for i in val:
#         print ('{} : {}'.format(key,i))
#     print(cook_book['Омлет'])    


# def product():
#     name_product=cook_book['product']
#     return name_product
# def measure():
#     measure_product=cook_book['measure']
#     return measure_product
# def amount():
#     amount_product=cook_book['amount']
#     return amount_product
# print(product(), measure(), amount())        





# def one_dish(product, measure):
#     for dish in cook_book:
#         print(dish, cook_book['Омлет']['product'])
# one_dish(['Омлет'], ['measure'])
# one_dish={}
# j=0
# for i in cook_book:
#     if j==0:
#         one_dish[Омлет]=(i['product'])
#     else:
#         one_dish.append(i['product'])
#     j+=1
# print(one_dish)        



#def get_shop_list_by_dishes(dish, person_count):
# def get_shop_list_by_dishes(cook_book, value):   
    
#     for k, v in cook_book.items():
#         if v == value:
#             return k
# print(get_shop_list_by_dishes(cook_book['Омлет'], cook_book.values))            
# #get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)