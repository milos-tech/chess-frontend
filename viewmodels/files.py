from models.files import File

def get_all_files(return_objects=False):
    """
    Set return_objects to True if you want to return a 
    model instance instead of JSON
    """
    files = File.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in files
        ]
        return list_of_objects

    return files

def get_file_with_id(id, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    file = File.read(id)

    return file if return_object else file.toJSON()

def save_file(game, path, gameId=None, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    if gameId != None:
        file = get_file_with_id(gameId, return_object=True)
        file.game, file.path = game, path

    else:
        file = File(
            game=game, path=path
        )

    file.save()

    return file if return_object else file.toJSON()

def delete_file(id):
    file = get_file_with_id(id, return_object=True)
    file.delete()
    return file.toJSON()