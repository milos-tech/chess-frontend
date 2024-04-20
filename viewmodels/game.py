from models.game import Game

def get_all_game(return_objects=False):
    """
    Set return_objects to True if you want to return a 
    model instance instead of JSON
    """
    objects = Game.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in objects
        ]
        return list_of_objects
    
    return objects

def get_game_with_id(gameId, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    obj = Game.read(gameId)

    return obj if return_object else obj.toJSON()

def save_game(results, gameId=None, uploaded_files=None, return_object=False):
    if gameId != None:
        game = get_game_with_id(gameId, return_object=True)
        game.results = (
            results
        )
    else:
        game = Game(
            results=results
        )

    game.save()

    return game if return_object else game.toJSON()
    
def delete_game(gameId):
    game = get_game_with_id(gameId)
    game.delete()

    return game.toJSON()