from data_class.article import Article


class JobSearch(Article):
    def __init__(self, filename):
        super().__init__(filename)
    

job_search = JobSearch("./info/job_search.pdf").display_pdf_article