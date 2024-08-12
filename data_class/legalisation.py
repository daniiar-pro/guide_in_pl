from data_class.article import Article


class Legalisation(Article):
    def __init__(self, filename):

        super().__init__(filename)


legalisation = Legalisation("./info/legal.csv").display_csv_article
