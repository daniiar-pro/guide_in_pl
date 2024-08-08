import textwrap
from pypdf import PdfReader


class Article:

    file_extensions = (".txt", ".pdf", ".csv")

    def __init__(self, filename, format_width):
        self.filename = filename
        self.format_width = format_width
        self.text_data = ""

    def display_text_article(self):

        with open(self.filename) as file:
            for line in file:
                self.text_data += line
                self.format_article()

    def format_article(self):
        wrapper = textwrap.TextWrapper(width=self.format_width)
        word_list = wrapper.wrap(text=self.text_data)

        for line in word_list:
            print(line)

    def display_pdf_article(self):
        reader = PdfReader(self.filename)
        page = reader.pages[0]
        self.text_data += page.extract_text()
        self.format_article()
