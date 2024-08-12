import webbrowser
from dotenv import load_dotenv
import os


class Study:
    load_dotenv()

    url_for_more_info = os.getenv("STUDY_URL_INFO")

    @classmethod
    def get_study_info(cls):
        """Redirects for more info, new tab in browser"""
        webbrowser.open_new(cls.url_for_more_info)
