import json
import requests

from .player import Player
from .constants import SERVER_URL

class Game:
    ENDPOINT = "/game/"

    def __init__(self, results=None, gameId=None, **kwargs) -> None:
        self.gameId = gameId
        self.results = results
        self.files = kwargs['files'] if 'files' in kwargs else []

        if isinstance(player, dict):
            self.player = Player(**player)
        else:
            self.player = player

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'player': self.player,
        'results': self.results}
        files=[
        ('files',('Nguh Prince ID recto.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID recto.jpg','rb'),'image/jpeg')),
        ('files',('Nguh Prince ID verso.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID verso.jpg','rb'),'image/jpeg'))
        ]
        headers = {}

        if not self.gameId:
            response = requests.request("POST", url, headers=headers, data=payload, files=files)

            data = json.loads(response.text)
            self.gameId = data['gameId']
        else:
            url += str(self.id)
            response = requests.request("PATCH", url, headers=headers, data=payload, files=files)

    def read(gameId=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += gameId if gameId else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response:dict = json.loads(response.text)

        if gameId:
            game = __class__(**response)
            return game
        else:
            games = []

            for result in response:
                game = __class__(**result)
                games.append(game)
            
            return games

    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.gameId}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.gameId = None
        except Exception as e:
            raise e
        
    def toJSON(self, with_files=True):
        dictionary = {
            "gameId": self.gameId,
            "results": self.results,
        }

        return dictionary