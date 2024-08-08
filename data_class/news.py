import requests
import json


class News:
    API = "https://jsonplaceholder.typicode.com/comments/1"

    @classmethod
    def get_latest_news(cls):
        request = requests.get(cls.API)
        response = request.json()
        return json.dumps(response, indent=2)

    def need_help():
        pass