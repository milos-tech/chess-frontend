import os
import json
import requests

from .constants import SERVER_URL

class Player:
    ENDPOINT = "/player/"

    def __init__(self, player_name, playerId=None) -> None:
        self.playerId = playerId
        self.player_name = player_name

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'player_name': self.player_name}
        headers = {}

        if not self.id: # save to the backend with a POST request
            response = requests.request("POST", url, headers=headers, data=payload, files=files)

            data = json.loads(response.text)
            self.playerId = data['playerId']
        else: # update a particular subject
            url += str(self.playerId)
            response = requests.request("PATCH", url, headers=headers, data=payload, files=files)


    def read(playerId=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += playerId if playerId else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if playerId:
            game = __class__(**response)
            return game
        else:
            games = []

            for result in response:
                game = __class__(**result)
                games.append(game)
            
            return games

    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.playerId = None
        except Exception as e:
            raise e