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
  if choice == "b":
    pass
  elif choice == "m":
    pass
  elif choice == "x":
    pass
  elif choice == "e":
    pass
  elif choice == "c":
    pass
  elif choice == "d":
    pass
  elif choice == "r":
    pass
  elif choice == "z":
    input("\nPress enter to exit the cash register.")
  else:
    input("\nInvalid input. Press enter to try again.")

print(f"\nThanks for visiting {store_name}!  Please come again!")