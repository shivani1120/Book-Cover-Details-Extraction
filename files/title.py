from abc import ABC, abstractmethod
import cv2
from numpy import double, equal
import pytesseract
from pytesseract import Output


class Title(ABC):
    @abstractmethod
    def get_title(self, path):
        pass

class title_getter:

    def get_title(self, path):
        img = cv2.imread(path)
        # to store the maximum height of text
        maxHeight = 0
        
        # to store the title of the book
        title = ""

        # rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        # results = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME, pandas_config = Dict)
        results = pytesseract.image_to_data(img, output_type=Output.DICT)

        
        

        # find the maximum height
        for i in range(0, len(results["text"])):
            
            # get the height of text
            h = results["height"][i]
            w = results["width"][i]
            # get the text
            text = results["text"][i]
            # get confidence levele of text
            conf = double(results["conf"][i])
            area = h*w
            # consider text only having posiitive confidence level
            if conf > 0:
                # reject if text is empty or contain only spaces
                if text.isalpha() and h > maxHeight:
                    # update the maximum height
                    maxHeight = h
        

        #  to get all the words in a title
        for i in range(0, len(results["text"])):
            
            # get height
            h = results["height"][i]
            w = results["width"][i]
            
            # get text
            text = results["text"][i]
            # get confidence level
            conf = double(results["conf"][i])
            
            # filter out negative confidence text localizations
            if conf > 0:
                # multiply by 0.9 because all the text in the title are not of the same height
                
                if text != "" and text != " " and  h >= 0.8 * maxHeight:
                    title= title + text
                    title  =  title + " "

        return title



