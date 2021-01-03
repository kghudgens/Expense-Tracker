items = []
cost_of_items = []

def get_total_expenses(dictionary):
    total = 0

    cost_list = list(dictionary.values())

    for x in cost_list:
        total = int(x) + total
    
    return total

def add_to_list(item, cost):
    items.append(item)
    cost_of_items.append(cost)

    result = make_dictionary()
    print(result)

def make_dictionary():
    item_cost = dict(zip(items, cost_of_items))
    return item_cost

def get_user_input():
    while True:
        user_item = input("What did you buy? ")
        if user_item == 'q':
            break

        user_item_cost = input("How much did it cost you? ")
        if user_item_cost =='q':
            break
        
        add_to_list(user_item, user_item_cost)
        continue
        
    

get_user_input()
all_expenses = make_dictionary()
print(get_total_expenses(all_expenses))