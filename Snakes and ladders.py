from tkinter import *
import tkinter.simpledialog
import tkinter as tk

#import tkMessageBox
import random
import logging
logging.basicConfig(filename='snakes_ladders.log',level=logging.DEBUG)


root = Tk()
#w = Label(root, text="My Program")
#name = tkinter
#name= tkinter.simpledialog.askstring("Name of player", "What is your name")
#print ("your name is " + name)
class Player:
    # This function is ALWAYS created everytime the Player object is created
    # sets the name based "name_parameter"
    # sets the initial position to all players at 0
    def __init__(self,name_parameter):
        self.name = name_parameter
        self.current_position = 0

    def __str__(self):
       return "player " + self.name
    # function to get the current position of the player
    def get_current_position(self):
        return self.current_position
    # Function to return name of the player to whoever calls it
    def get_name(self):
        return self.name
    # function to set the current position of the player (ex: gives position after they roll dice)
    def set_current_position(self,steps):
        self.current_position = self.current_position + steps
    # function to move the player based off the steps (number rolled)
    def move_player(self,steps):
        print("Current position of the player " + self.name + " is " + str(self.current_position))
        self.set_current_position(steps)
        print("New position of the player " + self.name + " is " + str(self.current_position))
        # Once someone reaches 100 or more. They have won the game and quit the program
        if(self.get_current_position()>=100):
            print("Congrats !!! player " + self.name + " WON !!!")
            quit()

    #checks if you land on the snake or ladder based off the position dictionary. (you move if you do land on a snake or ladder)
    def check_if_move_again(self, pos_dict):
        # if current position is one of the keys (in position dictionary) then move based off the key's value(ex: 64 is the key, -4 is the value[move back 4 steps})
        if(self.get_current_position() in pos_dict.keys()):
            movePos = pos_dict[self.get_current_position()]
            newPos = self.set_current_position(movePos)
            print("POSITION JUMP !!!!!! new position of the player  " + self.name + " is " + str(self.get_current_position()) )
# Dictionary that shows the position of the snakes and ladders
pos_dict = {4:10, 9:22, 17:-10, 20:18, 28:56, 40:19, 54:-20, 62:-44, 63:18, 64:-4, 71:20, 87:-63, 93:-20}

"""
-setup game requires
-number of players
-postion of players
-Dice function

"""

logging.info('Start of program')

#list of all the players in the game that stores the names
players= []
# function to setup the game
def setup_game():
 #players= 2
 while True:
    try:
          #global parameter to tell number of players
          global num_players
          num_players= int(tkinter.simpledialog.askinteger("number of players", "How many players are there?"))
          if num_players > 4 or num_players < 2:
              print("must be lower than 5 or higher than 1")
          else:
              #the right number of players had been defined...
              logging.info("number of players created equals " + str(num_players))
              print("number of players created equals " + str(num_players))


              #0 is the start of the range. players is the end of a range
              for i in range(0, num_players):
                  while True:
                      print("i = " + str (i))

                     #Message box for interaction
                      name = tkinter.simpledialog.askstring("Name of player" + str(i), "What is your name")
                      #checks to see if name has already be chosen. If it has been chosen, pick a new one.
                      if not name in players:
                          # assign a name to each player
                          players.append(Player(name))
                          #When you enter a name that's not on the list. means you're good
                          break
                      else:
                          print("cant have duplicate names")


              # When you choose players # between 2-4
              break

#names and players
    except ValueError:
        print ("must be a number")

#test to make sure number of players is correct
 for count in range(len(players)):


     #lists player number and names
     print ("Player " + str(count) + " " + str(players[count]))

     print("Player " + str(count) + " " + str(players[count])+" is at" + " " + str(players[count].get_current_position()))

"""
-fuction to roll dice
-returns number between 1-6
"""
def roll_dice(player_name):
    rolldice = random.randint(1,6)
    print (player_name + " rolled " + str(rolldice))
    return rolldice

"""
-move function
-current position
-next position
-number that was rolled
"""




# execution
setup_game()
# game now has players identified
# everyone is at position 0
# time to start ...
# game finishes when any one player reaches position >= 100
while True:
    for i in range (0, num_players):

       "copied from https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens"
        #keeps the window in one position
       window = Tk()

       window.title("ROLL DICE")
       w = 80  # width for the Tk root
       h = 80  # height for the Tk root

       # get screen width and height
       ws = window.winfo_screenwidth()  # width of the screen
       hs = window.winfo_screenheight()  # height of the screen

       # calculate x and y coordinates for the Tk root window
       x = (ws / 10) - (w / 10)
       y = (hs / 10) - (h / 10)

       # set the dimensions of the screen
       # and where it is placed
       window.geometry('%dx%d+%d+%d' % (w, h, x, y))


       def move_position():
           rolled = roll_dice(players[i].get_name())
           players[i].move_player(rolled)
           players[i].check_if_move_again(pos_dict)
           label.configure(text="button was clicked!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
           window.destroy()

       def clicked():
           label.configure(text="button was clicked ")
           window.destroy()


       label = Label(window, text=" ")
       label.grid(column=0, row=0)

       btn = Button(window, text=players[i].get_name() + " please roll" , command=move_position)
       btn.grid(column=1, row=0)
       window.mainloop()


'''
-game ends when player reaches 100 or more first
-track if your at snake(u go down)
-track if your at ladder(u go up)
'''
