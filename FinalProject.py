
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
#I am going to put a list of riddles that the dragon can pick from to ask the player.


#Defining the character's attributes
class character():
    def __init__(self):
        self.hearts=3
        self.correct=0
        self.wrong=0
        self.description_status=(f"\n<<<You currently have {self.hearts} more chances. You have gotten {self.correct} riddles right, and {self.wrong} wrong>>>")
test= character()
#Starting the game >>>>>>

print(first_string)
input()
print(castle)
print("You make it up to the old castle on the hill. Once inside, you find that the floors are covered in gold and jewels.\n However, one wrong move could land you in the dragon's path. \n >>> ")
input()
print(dragon)
print("Oh, no! It's the dragon. However, it looks as if it is fast asleep. \n >>>")
input()
print("The sound of your boots echoes through the hallways. You enter the great throne room, where the dragon is sleeping on a heap of gold.\n On the other side of the room, you see a magic harp playing music. \n >>>.")
input()
print(harp)
print("The dragon stirs in its sleep and swishes its tail. It knocks over the harp! \n The harp stops playing and clatters across the floor. \n >>>.")
input()
print(awakedragon)
print("The dragon woke up!\n>>>")
input()
print(talkdragon)
print("-Oi, wotcher little one!- \n Says the dragon in a cheerful aristocratic accent. \n -Best ya com\'up \'ere on sucha fine day! Ya look pretty tasty, mind if I take a wee bite?- >>>")
print(awakedragon)
print("The dragon considers for a bit and then changes its mind. -Oi, never tha mind that. Entertain me instead. I hope ya like riddles-")
print(test.description_status)





