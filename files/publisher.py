import spacy
from abc import ABC, abstractmethod

class publisher_getter:
    def get_publisher(self):
        nlp = spacy.load('en_core_web_sm')
        
        file1 = open('recognized.txt', 'r')
        Lines = file1.readlines()
        publishers = ""
        for line in Lines:
            # print(line)
            doc = nlp(line)

            # Identify the publishers
            for ent in doc.ents :
                if(ent.label_ == 'ORG'):
                    publishers = publishers + ent.text 
                    publishers = publishers + " "

        # Return publishers
        return publishers