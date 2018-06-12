from tkinter import *
import tkinter.simpledialog

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
    def __init__(self,name):
        self.name = name
        self.current_position = 0
    def __str__(self):
       return "player " + self.name

    def get_current_position(self):
        return self.current_position

    def set_current_position(self,steps):
        self.current_position = self.current_position + steps
"""
-setup game requires
-number of players
-postion of players
-Dice function

"""

#numbweof=tkinter.simpledialog.askstring("number of players", "How many players are there?")
#print ("there are " + str(numbweof))
logging.info('Start of program')
def setup_game():
 #players= 2
 while True:
    try:

          #print("how many players are in the game?")
          #num_players= int(input("how many players are in the game?"))
          num_players= int(tkinter.simpledialog.askinteger("number of players", "How many players are there?"))
          if num_players > 4 or num_players < 2:
              print("must be lower than 5 or higher than 1")
          else:
              #the right number of players had been defined...
              logging.info("number of players created equals " + str(num_players))
              print("number of players created equals " + str(num_players))
              #assign a name to each player

              #list of all the players in the game that stores the names
              players= []
              position_array= []
              #0 is the start of the range. players is the end of a range
              for i in range(0, num_players):
                  while True:
                      print("i = " + str (i))
                     # name = input("What is the name of player " + str(i) + "?")
                     #Message box for interaction
                      name = tkinter.simpledialog.askstring("Name of player" + str(i), "What is your name")
                      #checks to see if name has already be chosen. If it has been chosen, pick a new one.
                      if not name in players:
                          players.append(Player(name))
                         # position_array.append(0)
                          #When you enter a name that's not on the list. means you're good
                          break
                      else:
                          print("cant have duplicate names")
                    #'return'(names)


              # When you choose players # between 2-4
              break

#names and players
    except ValueError:
        print ("must be a number")

#test to make sure number of players is correct
 for count in range(len(players)):

     #print ("im at count = " + str (count))
     #lists player number and names
     print ("Player " + str(count) + " " + str(players[count]))
    # print ("Player " + str(count) +" is at" + " " + str(position_array[count]))
     print("Player " + str(count) + " " + str(players[count])+" is at" + " " + str(players[count].get_current_position()))

"""
-fuction to roll dice
-returns number between 1-6
"""
def roll_dice():
    return random.randint(1,6)

"""
-move function
-current position
-next position
-number that was rolled
"""
# execution
setup_game()

#print("player rolled " + str(roll_dice()))


