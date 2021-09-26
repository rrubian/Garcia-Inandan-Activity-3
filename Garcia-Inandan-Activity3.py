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