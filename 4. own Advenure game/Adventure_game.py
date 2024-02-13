name = input("Type ur name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "Your are on a dirt road, it has come to an end and ou can go left or right. Which way tould u like to go?: ").lower()

if answer == "left":
    answer = input(
        "you come to a river. you can walk aroud it or u can swim accross? Type walk to walk around and swim to swim the river accross: ")

    if answer == "swim":
        print("Ypu swim accross and were eaten by alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?")

    if answer == "back":
        print("You go back to the main road.")
    elif answer == "cross":
        answer = input(
            "You cross a bridge and meet a stranger. Do you talk to them (yes/no)?: ")
        if answer == "yes":
            print("You talk to the stranger and You win !")
        elif answer == "no":
            print("You ignore to the stranger and You loose !")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")
else:
    print("Not a valid option. You lose")

print("Thank you for trying")
