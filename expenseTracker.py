items = []
cost_of_items = []


def inform_user():
    """Let user know what they are spending their money on"""
    pass


def get_total_expenses(dictionary):
    """Get the price of all expenses """

    total = 0

    cost_list = list(dictionary.values())

    for x in cost_list:
        total = int(x) + total

    return total


def add_to_list(item, cost):
    """Adds user input to list"""

    items.append(item)
    cost_of_items.append(cost)

    make_dictionary()


def make_dictionary():
    """
    Added all items and cost to dictionary to make it associated with its price
    """

    item_cost = dict(zip(items, cost_of_items))
    return item_cost


def get_user_input():
    """Get users input their expenses"""

    while True:
        user_item = input("What did you buy? ")
        if user_item == "q":
            break

        user_item_cost = input("How much did it cost you? ")
        if user_item_cost == "q":
            break

        add_to_list(user_item, user_item_cost)
        continue


get_user_input()
all_expenses = make_dictionary()
print(get_total_expenses(all_expenses))