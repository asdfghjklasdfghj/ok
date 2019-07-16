import random
answer = input("Press enter to roll the dice ")

if answer == "":
    print("What kind of dice would you like to roll?")
    print("six sided?")
    print("twenty sided?")
    choice = input()
    if choice == "6":
        print(random.randint(1, 6))
    elif choice == "20":
        print(random.randint(1, 20))
    else:
        print("Can't do that")
       
    
        
    
