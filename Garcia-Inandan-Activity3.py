print("1. Eggs")
print("2. Pancakes")
print("3. Waffles")
print("4. OatMeal")
MainChoice = int(input("Choose a breakfast item #: "))
if(MainChoice == 1):
    Meal = "Eggs"
    print("You've Choosen eggs")
elif (MainChoice == 2):
    Meal = "Pancakes"
    print("You've Choosen pankcakes")
elif (MainChoice == 3):
    Meal = "Waffles"
    print("You've Choosen waffles")
else:
    print("You've Choosen Oatmeal")

if (MainChoice <= 4):
    print("1. Wheat Toast")
    print("2. Sour Dough")
    print("3. Rye Toast")
    print("4. White Bread")
Bread = int(input("Choose a type of bread: "))

if (Bread == 1):
    print("You chose " + Meal + "  with wheat toast.")
elif (Bread == 2):
    print("You chose " + Meal + "  with sour dough.")
elif (Bread == 3):
    print("You chose " + Meal + "  with rye toast.")
elif (Bread == 4):
    print("You chose " + Meal + "  with pancakes.")
else:
    print("We have eggs, but not that kind of bread.")

if ((MainChoice >= 1) or (MainChoice <= 3)):
    print("1. Syrup")
    print("2. Strawberries")
    print("3. Powdered Sugar")
Topping = int(input("Choose a topping: "))
if (Topping == 1):
    print ("You chose " + Meal + " with and syrup and Bread.")
elif (Topping == 2):
    print ("You chose " + Meal + " with and strawberries Bread.")
elif (Topping == 3):
    print ("You chose " + Meal + " with and powdered sugar Bread.")
else:
    print ("We have " + Meal + ", but not that topping Bread.")

if (MainChoice == 4):
    print("You chose oatmeal.")

else:
    print("Thank You for coming by and Eating with us!")
