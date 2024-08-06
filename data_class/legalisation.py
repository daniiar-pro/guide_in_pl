import textwrap

class Legalisation:
    
    filename = "./info/legal.txt"
    text_data = ""
    
    @classmethod
    def get_legalisation_info(cls):
        """"Reads data from file"""
        with open(cls.filename) as file:
            for line in file:
                cls.text_data += line
        cls.wrap_data()
        
    
    @classmethod
    def wrap_data(cls):
        """Formats text read from a file"""
        wrapper = textwrap.TextWrapper(width=50)
        word_list = wrapper.wrap(text=cls.text_data)
        
        for line in word_list:
            print(line)
            