import webbrowser


class Study:
    url_for_more_info = "https://study.gov.pl/"
    
    @classmethod
    def get_study_info(cls):
        webbrowser.open_new(cls.url_for_more_info)
    
    