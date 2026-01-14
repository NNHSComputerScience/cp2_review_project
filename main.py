"""
Partner 1:
Partner 2:
Title: Programming 1 Review Project
Description: This menu-based program simulates the function of a cash register for a fast food restaurant.
"""
#####################################
###   VARIABLES   ###################
#####################################
menu = """
MENU:   B Burger, $3.30+        E End Order
        F Side, $1.00+          C Clear current order
        S Soft Drink, $0.50+    D Display current order
        M Value meal            R Report of Sales
        X Delete item           Z End program
"""
# a list of items in current customer's order; should be cleared after each completed order
order = []
costs = []
# 2D(nested) list of all customer orders; add completed customer order lists to this list
all_orders = []
# float value with current customer's order total
total = 0.0
# stores user's menu choice as a string
choice = "A"
# the name of your restaurant; rename it if you wish
store_name = "Good Burger"

#####################################
###   MAIN  PROGRAM #################
#####################################
print(
  f"Welcome to {store_name}, home of the Good Burger. Can I take your order?")
while choice != "z":
  print(menu)
  choice = input("Choose a menu option: ").lower()
  # keanu and abe
  if choice == "b":
    total += 3.30
    inputError = True
    while (inputError == True):
      cheeseChosen = input("Would that be a cheeseburger? (y/n)").lower()
      if cheeseChosen == "y":
        print("Cheeseburger selected.")
        total += 0.50
        inputError = False
        order.append("Cheeseburger ($3.80)")
      elif cheeseChosen == "n":
        print("Regular Burger Selected")
        inputError = False
        order.append("Burger ($3.30)")
  elif choice == "f":
    inputError = True
    while (inputError == True):
      sideChoice = input("""
        Would that be fries or a side?
        F Fries (+$1.00)
        OR Onion Rings (+$1.50)
        """).lower()
      if sideChoice == "f":
        total += 1.00
        order.append("Fries ($1.00)")
        print("Fries Selected")
        inputError = False
      elif sideChoice == "or":
        total += 1.50
        order.append("Onion Rings ($1.50)")
        print("Onion Rings Selected")
        inputError = False
  elif choice == "s":
    inputError = True
    while (inputError == True):
      sizeDrinkChoice = input("""
        L Large Drink (+$1)
        M Medium Drink (+$0.75)
        S Small Drink (+$0.5)""").lower()
      if sizeDrinkChoice == "l":
        total += 1.00
        order.append("Large Drink ($1.00)")
        print("Large Drink Selected")
        inputError = False
      elif sizeDrinkChoice == "m":
        total += 0.75
        print("Medium Drink Selected")
        order.append("Medium Drink ($0.75)")
        inputError = False
      elif sizeDrinkChoice == "s":
        total += 0.5
        print("Small Drink Selected")
        order.append("Large Drink ($1.00)")
        inputError = False
  elif choice == "m":
    pass
  # Robbie and Abdullah
  elif choice == "x":
    selection = input("\n\nType the menu item you would like to remove an item from your order, or press enter to remove the last selected item: ").title()
    if selection == "":
      itemToRemove = order.pop()
      total -= costs.pop()
      print(f"\n{itemToRemove} has been removed from your order. Your total is ${total}.\n\n")
    elif selection != "" and selection in order:
      index = order.index(selection)
      itemToRemove = order.pop(index)
      total -= costs.pop(index)
      print(f"\n{itemToRemove} has been removed from your order. Your total is ${total}.\n\n")
    else:
      print("That's not a valid input.\n")
  elif choice == "e":
    pass
  elif choice == "c":
    selection = ""
    while selection != "y" and selection != "n":
      selection = input("\nAre you sure you want to clear your order? (Y/N): ").lower()
      if selection == "y":
        order.clear()
        print("\nOrder cleared!\n\n")
      elif selection == "n":
        print("\nCancelled.\n\n")
      else:
        print("\nThat's not a valid input.")
  elif choice == "d":
    print("\nCurrent order:\n")
    for listItem in order:
      print("\t-" + listItem)
    print(f"\nYour total cost thus far is ${total}\n")
  elif choice == "r":
    pass
  elif choice == "z":
    input("\nPress enter to exit the cash register.")
  else:
    input("\nInvalid input. Press enter to try again.")

print(f"\nThanks for visiting {store_name}!  Please come again!")
