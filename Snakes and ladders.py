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


              player_array= []

              for i in range(0, players):
                  while True:
                      print("i = " + str (i))
                      name = input("What is the name of player " + str(i) + "?")
                      if not name in player_array:
                          player_array.append(name)
                          break
                      else:
                          print("cant have duplicate names")
                    #'return'(names)

              # get out of while loop
              break

#names and players
    except ValueError:
        print ("must be a number")
 #lists player # and player name
 for count in range(len(player_array)):
     print ("Player " + str(count) + " " + player_array[count])

"""
names = {}
for i in range (1, players +1):
    while True:
        name = input ("What is the name of player{}").format (i)
        if not name in names:
            names(name) = 0
            break
else:
   print("cant have duplicate names")
'return' (names)

#screen display

#screen caption

title = 'snakes and ladders'

#If you land on a snake square you would slide down the snake to bottom square
#If you land on a ladder square you would climb up the ladder to top square
def move_player( player,  current_position):
 snake_squares = {16: 5, 34: 29, 64: 38 , 77: 4,  93: 24}
 ladder_squares = {4: 19, 22: 48, 30: 72, 51: 81, 61: 88}
#roll dice
roll= ('roll_dice')
new_position= ('current_position' + roll)
print ("{} rolled a {1} and is now currently on {2}")
if new_position in 'snake_squares':
 print ("player has slid down snake and is now on square {}")
elif new_position in 'ladder_squares':
 print ("player has climbed up ladder and is now on square{}")
else:


"""


# execution
setup_game()