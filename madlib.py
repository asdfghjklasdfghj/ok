import random

name = input("Please enter a name ")
place = input("Please enter a place ")
vehicle = input("Please enter the name of a vehicle ")
adverb = input("Please enter an adverb ")

decision = random.randint(1, 2)

if decision == 1:
    print(name + " went to hang out with their best friend at " + place + 
          ". While he was there, he won a " + adverb + " " + vehicle + "! "
          + name + " promtly went home to visit their mother and show her their new"
          + vehicle + " what a good day for " + name + "!")
else:
    print(name + " went to " + place + " and saw their best friend there! They we're talking when "
          + name + " saw a " + adverb + " " + vehicle + " While unsure of what was happening at first, "
          + name + " soon realized that it was a streetrace!")

