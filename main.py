# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# # # Everything that is indented after if/else statements is a block of code.
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if 45 <= age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     elif age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

# # # Condition regardless of previous if statement; same level of indentation.
#     wants_photo = input("Do you want a photo taken? Y or N: ")
#     if wants_photo == "Y":
#         bill += 3
#     else:
#         print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# # # Comparison Operators

# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# ==  Equal to
# !=  Not equal to

# =   Assigning value
# ==  Checking equality

# / # / # EXERCISE # / # / #

# number = int(input("Choose a number! "))

# # # Modulo (%) checks the remainder of a number.
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# / # / # EXERCISE # / # / /#

# height = float(input("What is your height in m? "))
# weight = int(input("What is your weight in kg? "))
# bmi = (weight / (height ** 2))
# format_bmi = "{:.2f}".format((weight / (height ** 2)))

# if bmi <= 18.5:
#     print(f"Your BMI is {format_bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {format_bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {format_bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {format_bmi}, you are obese.")
# else:
#     print(f"Your BMI is {format_bmi}, you are clinically obese.")

# / # / # / # / # / #

# / # / # EXERCISE # / # / #

# year = int(input("Enter year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

# / # / # / # / # / #

# / # / # EXERCISE # / # / #

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
# else:
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")

# / # / # / # / # / #

# / # / # EXERCISE # / # / #

# print("The Love Calculator is calculating your score...")
# name1 = input("What is your name? ").upper()
# name2 = input("What is their name? ").upper()

# combined_names = (name1 + name2).lower()

# t = combined_names.count("t")
# r = combined_names.count("r")
# u = combined_names.count("u")
# e = combined_names.count("e")
# first_digit = str(t + r + u + e)

# l1 = combined_names.count("l")
# o = combined_names.count("o")
# v = combined_names.count("v")
# e = combined_names.count("e")
# second_digit = str(l1 + o + v + e)

# love_score = int(first_digit + second_digit)

# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif 40 < love_score < 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")

# / # / # / # / # / #

# / # / # PROJECT OF DAY 3 # / # / #

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

turn = input("You're in front of a devious-looking fork on the road. Where do you want to go? Left or Right?\n").lower()
if turn == "left":
    action = input("You're now in front of an evil-looking river. What do you want to do? Wait or Swin?\n").lower()
    if action == "wait":
        door = input("You now have witnessed the apparition of three magical doors... "
                     "Choose! Red, Yellow or Blue?\n").lower()
        if door == "red":
            print("Burn eternally in damned flames!\nGAME OVER")
        elif door == "blue":
            print("Get eaten by ferocious beasts!\nGAME OVER")
        elif door == "yellow":
            print("You did it! You crazy son of a bitch, you did it!\nYOU WIN!")
        else:
            print("GAME OVER!")
    else:
        print("You were attacked by giant piranhas!\nGAME OVER")
else:
    print("You fell into a spiked hole!\nGAME OVER")
