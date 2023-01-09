
def Gooday():
    print("""
Welcome to the blue lagon restaurant.i am will be your guide for today.
 """)
    choices = input("""
    Are you ready, answer y to contiue  or q to quit
    """)
   
    quit_character = "q"
    while choices.lower != quit_character:
      choice = input("""
    What do you need help with for today,type  1,2,3 or 4
    1 Menu
    2 Specials 
    3 reservation
    4 take order
    """)
     
      if choice == quit_character:
        break
      elif choice == "1":
        menu()
      elif choice == "2":
        specials()
      elif choice == "3":
        make_reservration
      elif choice == "4":
        take_order()
        break
      else:
        print("choose type in a number from the choices listed")
def make_reservration():
  table = input("what table would you like to reserve a seat in?. Ther are are 3 avaible stables for today. 42, 44, and 53. choose: ")
  print("Your table is reserved for " + table)
  
  
def specials():
  print("Specials  of these week include ")
  print("""
  Menu Specials
  _________________________
  trio salad
  egg plant 
  salom
  brust 
   To order a special, add them in the oder  section
  """)
def take_order():
  name = input("Good day,  welcome to the blue lagon.Could i get yur name please: ")
  order = input("what would you like to order today " + name + " Choose from menu.")
  print("food will arrive soon " + order + " please be  patient")

def menu():
  print("menu inludes lunch, breafat and dinner")
  print("""
  Menu
  ====================
  Breakfast  
  pancakes 
  egg and bacon snadwich 
  waffles
   pecan pie 
 
 
  Lunch 
  Tilipia
 Cod
 French fries
 Honey walnut shrimp
   """)
  
  

Gooday()