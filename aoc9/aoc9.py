def get_score(players, rolls):
    current= 0
    players_list = range(1, 1+players)
    i = 0
    current_player = 1
    while i < rolls:
        if (current_player % players == 0):
            print("player: %s" % (players))
        else:
            print("player: %s" % (current_player % players))
        i += 1
        current_player += 1
    return
