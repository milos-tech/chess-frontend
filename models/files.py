import os
import json
import requests

from .constants import SERVER_URL

class File:
    ENDPOINT = "/files/"

    def __init__(self, id=None, path=None, game=None) -> None:
        self.id = id
        self.path = path
        self.game = game

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'player': self.player,
        'results': self.results}
        files=[
        ('files',('Nguh Prince ID recto.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID recto.jpg','rb'),'image/jpeg')),
        ('files',('Nguh Prince ID verso.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID verso.jpg','rb'),'image/jpeg'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        data = json.loads(response.text)
        self.id = data['id']

    def read(id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += id if id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if id:
            game = __class__(**response)
            return game
        else:
            games = []

            for result in response:
                game = __class__(**result)
                games.append(game)
            
            return games

    @property
    def filename(self):
        return os.path.basename(self.path) if self.path else ''