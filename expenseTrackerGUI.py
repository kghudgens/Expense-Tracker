from tkinter import *
import csv
import expenseTracker


def write_to_csv(dictionary):
    """Write to a csv file with all information concerning expenses"""

    header = ["Expense", "Price"]
    dictionary
    with open("Tracked_Expenses.csv", "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(i for i in header)
        for key in dictionary.keys():
            f.write("%s, $%s\n" % (key, dictionary[key]))


# Create window
root = Tk()
root.geometry("300x300")

# Create menu
menu = Menu(root)
menu.add_command(label="Expense CSV ", command=write_to_csv())
# Create title and other labels


# Create entry place for initial statements

# Place widgets
menu.grid(row=0, column=0)

root.mainloop()
