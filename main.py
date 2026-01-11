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
user_inputs = []

#####################################
###   MAIN  PROGRAM #################
#####################################
print(f"Welcome to {store_name}, home of the Good Burger. Can I take your order?")
while choice != "z":
  print(menu)
  choice = input("Choose a menu option: ").lower()
  user_inputs.append(choice)
  # Devin & Evren
  if choice == "b":
    a = input("Make it a cheeseburger?(y/n) ").lower()
    if a == 'y':
      order.append("Cheeseburger")
      total += 3.8
    elif a == 'n':
      order.append("Burger")
      total += 3.30
    else:
      while True:
        print("Please retry")
        a = input("Make it a cheeseburger?(y/n) ").lower()
        if a == 'y':
          order.append("Cheeseburger")
          total += 3.8
          break
        elif a == 'n':
          order.append("Burger")
          total += 3.30
          break
        else:
          continue
  elif choice == "f":
    print('''
    Pick a side!
    1.\tFries
    2.\tOnion Rings\n
    ''')
    a = int(input("Pick a number above for side: "))
    if a == 1:
      order.append("Fries")
      total += 1
    elif a == 2:
      order.append("Onion Rings")
      total += 1.5
    else:
      while True:
        print("\nNot an option\n")
        print('''
        Pick a side!
        1.\tFries
        2.\tOnion Rings\n
        ''')
        a = int(input("Pick a number above for side: "))
        if a == 1:
          order.append("Fries")
          total += 1
          break
        elif a == 2:
          order.append("Onion Rings")
          total += 1.5
          break
        else:
          continue
  elif choice == "s":
    print('''
    Pick a size!
    1.\tSmall
    2.\tMedium
    3.\tLarge\n
    ''')
    a = int(input("Pick a number above for size: "))
    if a == 1:
      order.append("Small drink")
      total += .5
    elif a == 2:
      order.append("Medium drink")
      total += .75
    elif a == 3:
      order.append("Large drink")
      total += 1
    else:
      while True:
        print("Not an option!\n")
        print('''
        Pick a size!
        1.\tSmall
        2.\tMedium
        3.\tLarge\n
        ''')
        a = int(input("Pick a number above for size: "))
        if a == 1:
          order.append("Small drink")
          total += .5
          break
        elif a == 2:
          order.append("Medium drink")
          total += .75
          break
        elif a == 3:
          order.append("Large drink")
          total += 1
          break
        else:
          continue
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