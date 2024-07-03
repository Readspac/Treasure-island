class treasure_island:
    def __init__(self):
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
         _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_____ /
        *******************************************************************************
        ''')
        print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
        self.r_l = input("You're at a cross road. Where do you want to go?\n      Type \"left\" or \"right\"\n")
        if self.r_l == "left":
            self.option_w_s = input("You've come to a lake. There is an island in the middle of the lake.\n  Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
            if self.option_w_s == "swim":
                print("You get attacked by an angry trout. Game Over.")
            elif self.option_w_s == "wait":
                rgb_doors = input("You arrive at the island unharmed. There is a house with 3 doors.\n  One red, one yellow and one blue. Which colour do you chose?\n")
                if rgb_doors == "red":
                    print("It's a room full of fire. Game Over.")
                elif rgb_doors == "blue":
                    print("You enter a room of beasts. Game Over.")
                elif rgb_doors == "yellow":
                    print("You found the treasure! You Win!")


        elif self.r_l == "right":
            print("You fell into a hole. Game Over")

ti = treasure_island()
print(ti)

