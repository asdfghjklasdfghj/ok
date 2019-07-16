import random
answer = input("Press enter to roll the dice ")
again = 1

while again == 1:
    if answer == "":
        print("What is the largest number you'd like your dice to be able to roll?")
        number = input()
        print("You rolled a " + str(random.randint(1, int(number))))
        choice = input("Would you like to try again? Y/N: ")
        if choice == "Y":
            again = 1
        elif choice == "y":
            again = 1
        else:
            again = 2