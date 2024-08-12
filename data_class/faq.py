from data_class.article import Article

class FAQ(Article):
    """Displays FAQ"""
    def __init__(self, filename):
        super().__init__(filename)
    
faq = FAQ("./info/faq.csv").display_csv_article