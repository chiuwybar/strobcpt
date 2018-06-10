#2-4 players for this game
def setup_game():
 players= 2
 while True:
    try:
          print("how many players are in the game?")
          players= int(input())
          if players > 4 or players < 2:
            print("must be lower than 5 or higher than 1")
          else:
            break
#names and players
    except ValueError:
        print ("must be a number")
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
 'return' (new_position)
#animations
font = font.render.SysFont("Comic Sans MS", 40)
screen_title = (str(title), (RED))
screen.blit(screen_title, [ 175, 300 ]
clock.tick(50)/
pygame.quit()
#matthew is dumbo
#test
