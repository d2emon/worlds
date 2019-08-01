def look_room(player):
    return player.look()


def go_direction(player, direction_id):
    return player.go(direction_id - 2)
