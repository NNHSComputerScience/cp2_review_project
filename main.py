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
print(f"Welcome to {store_name}, home of the Good Burger. Can I take your order?")
while choice != "z":
  print(menu)
  choice = input("Choose a menu option: ").lower()
  # Tyler Ke and Jayden Cheng
  if choice == "b":  
    while True:
      choice = input("Would you like to make it a cheeseburger for +$0.50? (y/n) ")
      if choice.lower() == "y":
        print("Adding cheeseburger...")
        order.append("cheeseburger")
        total += 3.80
        break
      elif choice.lower() == "n":
        print("Adding burger...")
        order.append("burger")
        total += 3.30
        break
      else:
        input("\nInvalid input. Press enter to try again.")
  elif choice == "f":
    while True:
      choice = input("Would you like to order onion rings ($1.50) or fries ($1.00)? (f/o) ")
      if choice.lower() == "f":
        print("Adding fries...")
        order.append("fries")
        total += 1.00
        break
      elif choice.lower() == "o":
        print("Adding onion rings...")
        order.append("onion rings")
        total += 1.50
        break
      else:
        input("\nInvalid input. Press enter to try again.")
  elif choice == "s":
    while True:
      choice = input("Would you like a small ($0.50), medium ($0.75), or large ($1.00)? (s/m/l) ")
      if choice.lower() == "s":
        print("Adding small drink...")
        order.append("small drink")
        total += 0.50
        break
      elif choice.lower() == "m":
        print("Adding medium drink...")
        order.append("medium drink")
        total += 0.75
        break
      elif choice.lower() == "l":
        print("Adding large drink...")
        order.append("large drink")
        total += 1.00
        break
      else:
        input("\nInvalid input. Press enter to try again.")
  elif choice == "m":
    pass
  elif choice == "x":
    if len(order) > 0:
      removed_item = order.pop() # removes last item
      total -= removed_item[1] # subtracts its price
      print(f"\nRemoved {removed_item[0]} from your order.")
    else:
      print("\nThere is no item to remove.")
  elif choice == "e":
    pass
  elif choice == "c":
    clear_order = input("Are you sure you want to clear your order?")
    if clear_order == "yes":
      order = []
      total = 0.0
    else:
      pass
  elif choice == "d":
    print("\nYour order is", order, "\nYour total is", total)
  elif choice == "r":
    pass
  elif choice == "z":
    input("\nPress enter to exit the cash register.")
  else:
    input("\nInvalid input. Press enter to try again.")

print(f"\nThanks for visiting {store_name}!  Please come again!")