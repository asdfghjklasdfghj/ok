import random

def main():
    randnum = random.randint(1, 10)
    tries = 5
    while(tries>0):
        guess = int(input("Guess a number between 1 and 10: "))
        if (randnum == guess):
            print("You got it right")
            break
        else:    
            print("Try again")
            tries = tries - 1
            print("You have " + str(tries) + " left")
            if guess > randnum:
                print("You're answer is too high")jmnjmnkljkljj
            else:
                print("You're answer is too low")
    if(tries == 0):
        print("You lost the answer was " + str(randnum))
         
if __name__ == "__main__":
    main()