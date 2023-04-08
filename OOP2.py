from pprint import pprint
with open ('OOP.txt', 'rt') as file:
    cook_book={}
    for dish in file:
        dish_name=dish.strip()
        amount_ingredients=int(file.readline().strip())
        ingredients=[]
        for _ in range(amount_ingredients):
            product, amount, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'product': product,
                'amount': amount
                'measure':measure
            })
        file.readline()
        cook_book[dish_name]=ingredients
    pprint(cook_book)        

def get_shop_list_by_dishes(dishes, person_count):
    get_shop_list_by_dishes{}


#get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)