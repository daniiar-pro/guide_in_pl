import requests
from dotenv import load_dotenv
import os
from abc import ABC, abstractmethod
import textwrap


class ApiCall(ABC):
    """Abstract class that other classes can inherit"""

    @abstractmethod
    def make_api_call(self):
        pass


class News(ApiCall):
    load_dotenv()

    news_api_key = os.getenv("NEWS_API_KEY")

    API = (
        f"https://newsdata.io/api/1/latest?apikey={news_api_key}&q=example&language=en"
    )

    @staticmethod
    def make_api_call():
        """ "Makes an API call"""
        try:
            request = requests.get(News.API)
            response = request.json()
            print("Latest news around the world!\n")
            for article in response["results"]:
                title = article.get("title", "No Title Available")
                description = article.get("description", "No Description Available")

                if description is None:
                    description = "No Description Available"

                print(f"Title: {title}\n")
                News.format_description(description)
        except ValueError as e:
            print(f"Error parsing JSON response: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def format_description(text):
        """ "Formats data coming from an API"""
        wrapped_description = textwrap.fill(text, width=70)
        print(wrapped_description)
        print("\n" + "-" * 70 + "\n")

    @staticmethod
    def get_news():
        """ "Calls make_api_call() to run the program"""
        return News.make_api_call()
