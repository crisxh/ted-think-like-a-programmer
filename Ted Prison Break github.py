from time import sleep
import random

##100 lock positions and 1 of them is randomly the right one for each lock. 
lock_positions= [*range(0, 101)]

unlock=random.randint(0,101)

##hedge gets more discouraged the longer it goes without finding the right one.
hedge_red_low= ["GREEN oh wait...no still RED","nooo", "why do there have to be so many positions??","ugh","Drat, That's not it", "Not it.", "Nope", "That's wrong", "It's red", "Maybe the next one will be green", "we'll get there eventually", "we'll get out of here soon", "Don't you worry, I've got this!", "I'm getting dizzy"]
hedge_red_medium=["F.A.I.L first attemt at learning","I'm getting tired","ugh I'll keep trying", "who invented this thing anyways?"]
hedge_red_high=["This is getting ridiculous","Maybe we'll never get out of here","Maybe I missed the right one...?", "Please let it be this next one..."]
green =["Nice!", "We did it!", "On to the next one", "We make a great team!","Awesome!",  "Can't wait to get out of here!", "YES", "BOOM!", "Kachink!"]

encourage_hedge =["You can do it!", "Good try!", "You almost have it!","Keep going!", "Don't give up now!","We'll get it!","I bet it was close!","C'mon you've got it!","You were made for this!","Go get'em killer!","You'll get it next time"]
##Checking each lock position to see which one is the right one. 

print(f"welcome to this little story from TED's think like a programmer series.")
sleep(3)
print("The story is that you and a little robot named Hedge are trapped in a prison in a tolitarian dystopian society.")
sleep(3)
print("You and him are trying to escape, but the door has 100 possible combinations how will you possibly escape?")
sleep(3.5)
print("For each door Hedge will try each combination until the door opens to get you through")
sleep(3)
print("Ready?")
sleep(2)
prompt=input("press enter to begin the story")

print("Hedge: OK! Let's do this! I'll start trying to break the lock and the first number is...")
sleep(2)
for i in lock_positions:
    if i!=unlock:
        print("Hedge: The number I tried is",i)
        sleep(0.5)
        print("Door:INCORRECT LOCK NUMBER")
        sleep(0.5)

        if i%5==0:
            if i<=33:
                print("hedge:",random.choice(hedge_red_low))
            elif i>33<66:
                print ("hedge:",random.choice(hedge_red_medium))
            elif i>66:
                print("hedge:",random.choice(hedge_red_high))
            prompt=input("press enter to encourage Hedge")
            print("you:",random.choice(encourage_hedge))
            sleep(1)
            
    
    elif i == unlock:
        print(i, "GREEN")
        sleep(0.6)
        print("hedge:",random.choice(green))
        print("you:",random.choice(green))
        break