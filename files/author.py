from abc import ABC, abstractmethod
import spacy


class author_getter:
    def get_author(self):
        nlp = spacy.load('en_core_web_sm')
        
        file1 = open('recognized.txt', 'r')
        Lines = file1.readlines()
        authors = ""
        for line in Lines:
            
            doc = nlp(line)

            # Identify the authors
            for ent in doc.ents :
                if(ent.label_ == 'PERSON'):
                    authors = authors + ent.text 
                    authors = authors + " "

        # Return persons
        return authors