import csv

# Created empty lists to store all of the items and costs
items = []
cost_of_items = []
total = ""


def write_to_csv(dictionary):
    """Write to a csv file with all information concerning expenses"""

    header = ["Expense", "Price"]
    dictionary
    with open("Tracked_Expenses.csv", "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(i for i in header)
        for key in dictionary.keys():
            f.write("%s, $%s\n" % (key, dictionary[key]))


def inform_user():
    """Let user know what they are spending their money on"""

    print("In total you spent $" + str(total) + ".")
    pass


def get_total_expenses(dictionary):
    """Get the price of all expenses """
    global total
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
        user_item = input("What was the expense you paid for? ")
        if user_item == "q":
            break

        user_item_cost = input("How much did the expense cost you? ")
        if user_item_cost == "q":
            break

        # Checks to see if input for user item cost is number
        if user_item_cost.isdigit():
            user_item_cost = int(user_item_cost)
            add_to_list(user_item, user_item_cost)
        else:
            print("Please use numbers for the how much did it cost you prompt")

        continue


get_user_input()
all_expenses = make_dictionary()
write_to_csv(all_expenses)