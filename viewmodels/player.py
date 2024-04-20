from models.player import Player

def get_all_player(return_objects=False):
    player = Player.read()

    if not return_objects:
        list_of_player = [
            player.toJSON() for player in players
        ]
        return list_of_players

    return subjects

def get_player_with_id(id, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    player = Player.read(id)
    return player if return_object else player.toJSON()

def save_player(player_name, playerId=None):
    if playerId != None:
        # get player with playerId
        player = get_player_with_id(playerId, return_object=True)
        player.player_name = player_name

    else:
        player = Player(player_name=player_name)
    
    player.save()

    return player.toJSON()

def delete_player(playerId):
    player = get_player_with_id(playerId, return_object=True)
    player.delete()

    return player.toJSON()
