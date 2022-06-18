from abc import ABC, abstractmethod
import re

    
class isbn_getter:

    def get_isbn(self):
    
        with open('recognized.txt','r') as f:
            for line in f:
                for word in line.split():
                    if word == "ISBN" or word == "isbn":
                        before_keyword, word, after_keyword = line.partition(word)
                        # print("isbn:" , after_keyword)
                        return after_keyword
        