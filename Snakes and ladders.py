def setup_game():
    players=2
    while True:
        try:
            print ("how many players are in the game")
            players = int(input())
            if players > 4 or < 2:
                print ("must be lower than 5 or lower than 2")
            else:
                break
            except ValueError:
                print ("must be a number")
            names= {}

    for i in range (1, players+1):
        While True:
    name= input ("What is the name of player{}").format (i)
    if not name in names:



