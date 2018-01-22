#This is the long version. I was having trouble getting the riddles to print more than once, and I had help with making my intended goal. The short version was made by myself, and the long version was made with help and displays what I originally intended the code to do.
import random
#The player is trapped in a dragon's lair, and they were caught trying to steal some of the dragon's hoarded gold. The dragon wakes up and considers eating the player, but instead decides to entertain itself by asking the player riddles.
first_string ="Welcome. You are a petty thief, and you have learned that there is a chamber filled with gold and jewels inside the old castle on the hill.\n Seems too good to be true, but you decide to check it out.\nPress enter to continue whenever you see >>>."
# I set up the '>>>' so when the player sees that symbol, they hit enter. This saves me from having to remind the player to hit enter.
# I put all of the drawings in the same place so that I can reference them all at once.
castle=("""

            _   _   _                                               _   _   _
           | |_| |_| |                                             | |_| |_| |
           |         |                                             |         |
           |         |                                             |         |
           |         |                                             |         |
           |         |       __      __     __     __     __       |         |
           |          \_____|  |____|  |___|  |___|  |___|  |_____/          |
           |                                                                 |
           |                                                                 |
           |                                                                 |
           |                                                                 |
           |                          _____________                          |
           |                         /             \                         |
           |                        /               \                        |
           |                       /                 \                       |
           |                      /                   \                      |
           |                      |                   |                      |
           |                      |                   |                      |
           |                      |                   |                      |
           |                      |                   |                      |
           |______________________|___________________|______________________|""")

harp= ("""
           _____________________________
           | | | | | | | | | | | | | | ||
           | | | | | | | | | | | | | | | |      /|
           | | | | | | | | | | | | | | | ||    / ||
           | | | | | | | | | | | | | | | | |  /| | |       _
           | | | | | | | | | | | | | | | | ||/ | | ||      |
           | | | | | | | | | | | | | | | | | | | | | |     |
           | | | | | | | | | | | | | | | | | | | | | /   |-|
           | | | | | | | | | | | | | | | | | | | | |/
            || | | | | | | | | | | | | | | | | | | /   _
             | | | | | | | | | | | | | | | | | | |/   |
              || | | | | | | | | | | | | | | | | /  |-|
               | | | | | | | | | | | | | | | | |/
                || | | | | | | | | | | | | | | /
                 | | | | | | | | | | | | | | |/
                  || | | | | | | | | | | | | /
                   | | | | | | | | | | | | |/
                    ||_|_|_|_|_|_|_|_|_|_|_/""")


dragonmad= ("""||     ||
               ||_____||
               /       |   _____________          _
              /|0| |0| |  /  ________  /      ___||
             /         | /  /       / /      /____|
            |          \/  /       / /_____/ /
            |   v--v                    ____/
             \______|                  /
                    | _____________   /
                     | |            | |
                     |_|            |_|""")

dragon=("""
            ||     ||
            ||_____||
            /       |   _____________          _
           /|-| |-| |  /  ________  /      ___||
          /         | /  /       / /      /____|
         |          \/  /       / /_____/ /
         |    o                      ____/
          \______|                  /
                 | _____________   /
                 | |            | |
                 |_|            |_|
                                    """)


awakedragon=("""
                 ||    ||
                 ||____||
                /       |   _____________          _
               /|0| |0| |  /  ________  /      ___||
              /         | /  /       / /      /____|
             |          \/  /       / /_____/ /
             |    v                      ____/
              \______|                  /
                     | _____________   /
                     | |            | |
                     |_|            |_|""")

talkdragon=("""
                 ||    ||
                 ||____||
                /       |   _____________          _
               /|0| |0| |  /  ________  /      ___||
              /         | /  /       / /      /____|
             |          \/  /       / /_____/ /
             |    o                      ____/
              \______|                  /
                     | _____________   /
                     | |            | |
                     |_|            |_|""")
#I am going to define the player
#Defining the character's attributes
class character():
    def __init__(self):
        self.hearts=({2})
        self.correct=({0})
        self.wrong=({0})
        self.description_status=(f"\n<<<You currently have {self.hearts} more chances. You have gotten {self.correct} riddles right, and {self.wrong} wrong.>>>")
test=character()
#Starting the game >>>>>>
#printing commands fiilled with numbers and symbols are colors.
print("\033[2;30;31m \n")
print(first_string)
input()
print("\033[1;37;40m \n")
print(castle)
print("\033[1;33;40m \n")
print("You make it up to the old castle on the hill. Once inside, you find that the floors are covered in gold and jewels.\n However, one wrong move could land you in the dragon's path. \n >>> ")
input()
print("\033[1;32;40m \n")
print(dragon)
print("Oh, no! It's the dragon. However, it looks as if it is fast asleep. \n >>>")
input()
print("\033[1;36;40m \n")
print("The sound of your boots echoes through the hallways. You enter the great throne room, where the dragon is sleeping on a heap of gold.\n On the other side of the room, you see a magic harp playing music. \n >>>.")
input()
print("\033[1;30;40m")
print(harp)
print("The dragon stirs in its sleep and swishes its tail. It knocks over the harp! \n The harp stops playing and clatters across the floor. \n >>>.")
input()
print("\033[1;32;40m \n")
print(awakedragon)
print("The dragon woke up!\n>>>")
input()
print(talkdragon)
print("-Oi, wotcher little one!- \n Says the dragon in a cheerful aristocratic accent. \n -Best ya com\'up \'ere on sucha fine day! Ya look pretty tasty, mind if I take a wee bite?- >>>")
input()
print(awakedragon)
print("The dragon considers for a bit and then changes its mind. \n-Oi, never tha mind that. Entertain me instead. I hope ya like riddles- >>>")
input()
print("\033[1;37;40m \n")
print(test.description_status)
print("Enter the correct number for the answers listed\n")
#Initialising riddles that are chosen randomly
riddles = ["Hello","I sink in water but never drown, I catch prey on my barbed teeth, and I hunt all day yet never eat. \n What am I?","What question can you honestly never answer yes to?","There are ten stacks of 10 coins. Each coin weighs one ounce. \nYou know that one stack of coins is counterfeit, and the coins in that stack weigh 1.1 ounces instead. \nYou have a scale that can tell you the exact weight (in ounces) of whatever you put on it. \nWhat is the fewest number of weighings you can perform to find the counterfeit stack?", "You are in a race and overtake second place. What place are you in?", "When is 99 more than 100?","There are two sisters: one gives birth to the other and she, in turn, gives birth to the first. Who are the two sisters?", "A man is standing in front of a painting of a man when he says, \n'Brothers and sisters have I none, but this man's father is my father's son.' \nWho is in the painting?",  "A hunter leaves his cabin early in the morning and walks one mile due south. \nHere he sees a bear and starts chasing it for one mile due east before he is able to shoot the bear. \nAfter shooting the bear, he drags it one mile due north back to his cabin where he started that morning. \n What color is the bear?"]
#This is where I had the most help. I created all the if/else loops, but I was shown how to put it all in a working function.
def riddle():
    yay=0
    nou=2
    numby=random.randint(1,8)
    for x in range(10):
        numby=random.randint(0,7) + 1
        print(numby)
#Here is where I will put the multiple guess answers, and the user will input.
#There is one for each question available.
        if numby==1:
            print(riddles[1])
            print(f" 1: A fish \n 2: A Fishing hook \n 3: An anchor \n 4: A bowling ball) \n")
            if input()=="2":
                print("The dragon smiles a menacing grin. -Oi cheers, ya got one. Maybe\'s luck. Can ya do anotha?")
                yay=(yay+1)
                print(yay)
            else:
                print("The dragon looks at you, annoyed. -Guessen\', are ya? Maybe I\'m more hungry than bored.-")
                nou=(nou-1)
                print(nou)
        if numby==2:
            print(riddles[2])
            print(f" 1: Are you okay? \n 2: Are you dying? \n 3: Are you asleep? \n 4: Are you alive?")
            if input()=="3":
                print("The dragon smiles a menacing grin. -Oi cheers, ya got one. Maybe\'s luck. Can ya do anotha?")
                yay=(yay+1)
                print(yay)
            else:
                print("The dragon looks at you, annoyed. -Guessen\', are ya? Maybe I\'m more hungry than bored.-")
                nou=(nou+1)
                print(nou)
        if numby==3:
            print(riddles[3])
            print(f" 1: 1 \n 2: 3 \n 3: 5 \n 4: 10")
            if input()=="1":
                print("The dragon smiles a menacing grin. -Oi cheers, ya got one. Maybe\'s luck. Can ya do anotha?")
                yay=(yay+1)
                print(yay)
            else:
                print("The dragon looks at you, annoyed. -Guessen\', are ya? Maybe I\'m more hungry than bored.-")
                nou=(nou-1)
                print(nou)
        if numby==4:
            print(riddles[4])
            print(f" 1: first \n 4: Second \n 2: You are the only runner \n 3: Third")
            if input()=="4":
                print("The dragon smiles a menacing grin. -Oi cheers, ya got one. Maybe\'s luck. Can ya do anotha?")
                yay=(yay+1)
                print(yay)
            else:
                print("The dragon looks at you, annoyed. -Guessen\', are ya? Maybe I\'m more hungry than bored.-")
                nou=(nou-1)
                print(nou)
        if numby==5:
            print(riddles[5])
            print(f" 1: On a number line \n 2: When it is negative \n 3: On a microwave \n 4: Never")
            if input()=="3":
                print("The dragon smiles a menacing grin. -Oi cheers, ya got one. Maybe\'s luck. Can ya do anotha?")
                yay=(yay+1)
                print(yay)
            else:
                print("The dragon looks at you, annoyed. -Guessen\', are ya? Maybe I\'m more hungry than bored.-")
                nou=(nou-1)
                print(nou)
        if numby==6:
            print(riddles[6])
            print(f"1: Space and Time \n 2: Night and Day \n 4: Mother and Daughter \n 3: Happiness and Sadness")
            if input()=="2":
                print("The dragon smiles a menacing grin. -Oi cheers, ya got one. Maybe\'s luck. Can ya do anotha?")
                yay=(yay+1)
                print(yay)
            else:
                print("The dragon looks at you, annoyed. -Guessen\', are ya? Maybe I\'m more hungry than bored.-")
                nou=(nou-1)
                print(nou)
        if numby==7:
            print(riddles[7])
            print(f" 3: His father \n 4: Himself \n 1: His son \n 2: His uncle ")
            if input()=="4":
                print("The dragon smiles a menacing grin. -Oi cheers, ya got one. Maybe\'s luck. Can ya do anotha?")
                yay=(yay+1)
                print(yay)
            else:
                print("The dragon looks at you, annoyed. -Guessen\', are ya? Maybe I\'m more hungry than bored.-")
                nou=(nou-1)
                print(nou)
        if numby==8:
            print(riddles[8])
            print(f" 4: Black \n 2: White \n 3: Brown \n 1: The bear was imaginary")
            if input()=="2":
                print("The dragon smiles a menacing grin. -Oi cheers, ya got one. Maybe\'s luck. Can ya do anotha?")
                yay=(yay+1)
                print(yay)
            else:
                print("The dragon looks at you, annoyed. -Guessen\', are ya? Maybe I\'m more hungry than bored.-")
                nou=(nou-1)
                print(nou)
        print("Remaining:" + str(x))
    return(yay,nou)
status = riddle()
yay = status[0]
nou = status[1]
#These are the rewards/consequences for the more complex game, which give the players more chances.
if yay>3:
    print("You managed to get close enough to the harp to play a few chords. As if like magic, the harp begins to play itself. \n The dragon falls asleep. >>>")
    input()
    print(dragon)
    print("You escape! >>> ")
    input()
    print("\033[1;30;41m  \n")
#hopefully, the next 2 lines of code will cause python to crash, and the game will end.
    for x in range (100000):
        print("RUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUN")
else:
    riddle()
if nou<0:
    print(dragonmad)
    print("The dragon has had enough of your stupidity. \n-Oi, ya blimey git! Ya lost!- \n The dragon eats you!\nPress enter to exit >>>")
    input
    print("\033[1;30;41m  \n")
#hopefully, the next 2 lines of code will cause python to crash, and the game will end.
    for x in range (100000):
        print("SHUT DOWN    SHUT DOWN   SHUT DOWN   SHUT DOWN \nMAKE IT STOP    MAKE IT STOP    MAKE IT STOP    MAKE IT STOP")
else:
    riddle()
