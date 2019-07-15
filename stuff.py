import random

def main():
    randnum = random.randint(1, 20)
    tries = 5
    while(tries>0):
        guess = int(input("Guess a number between 1 and 20: "))
        if (randnum == guess):
            print("You got it right")
            break
        else:    
            print("Try again")
            tries = tries - 1
            
            if guess > randnum:
                print("You're answer is too high")
                print("You have " + str(tries) + " guesses left")
            else:
                print("You're answer is too low")
                print("You have " + str(tries) + " guesses left")
    if(tries == 0):
        print("You lost the answer was " + str(randnum))
         
if __name__ == "__main__":
    main()