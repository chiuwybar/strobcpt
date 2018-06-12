import random
import logging
logging.basicConfig(filename='snakes_ladders.log',level=logging.DEBUG)
"""
-setup game requires
-number of players
-postion of players
-Dice function

"""
logging.info('Start of program')
def setup_game():
 players= 2
 while True:
    try:
          print("how many players are in the game?")
          players= int(input())
          if players > 4 or players < 2:
              print("must be lower than 5 or higher than 1")
          else:
              #the right number of players had been defined...
              logging.info("number of players created equals " + str(players))
              print("number of players created equals " + str(players))
              #assign a name to each player

              #list of all the players in the game that stores the names
              player_array= []
              position_array= []
              #0 is the start of the range. players is the end of a range
              for i in range(0, players):
                  while True:
                      print("i = " + str (i))
                      name = input("What is the name of player " + str(i) + "?")
                      #checks to see if name has already be chosen. If it has been chosen, pick a new one.
                      if not name in player_array:
                          player_array.append(name)
                          position_array.append(0)
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

 for count in range(len(player_array)):

     print ("im at count = " + str (count))
     #lists player number and names
     print ("Player " + str(count) + " " + player_array[count])
     print ("Player " + str(count) +" is at" + " " + str(position_array[count]))

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

print("player rolled " + str(roll_dice()))