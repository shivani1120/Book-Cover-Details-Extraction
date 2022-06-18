from abc import ABC, abstractmethod
import os
import cv2
import pytesseract
from files.excel import Excel
from files.isbn import isbn_getter 
from files.author import author_getter 
from files.publisher import publisher_getter
from files.title import title_getter




class text(ABC):
    @abstractmethod
    def  get_text(self,path):
        pass
    def get_info(self,path):
        pass
    def get_data(self,path,flag):
        pass


class Text :

    # to write content in a txt file
    def get_text(self, path):
        img = cv2.imread(path)
 
        # Preprocessing the image starts
        
        # Convert the image to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Performing OTSU threshold
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        
        # Specify structure shape and kernel size.
        # Kernel size increases or decreases the area
        # of the rectangle to be detected.
        # A smaller value like (10, 10) will detect
        # each word instead of a sentence.
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        
        # Applying dilation on the threshold image
        dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
        
        # Finding contours
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                        cv2.CHAIN_APPROX_NONE)
        
        # Creating a copy of image
        im2 = img.copy()
        
        # A text file is created and flushed
        file = open("recognized.txt", "w+")
        file.write("")
        file.close()
        
        # Looping through the identified contours
        # Then rectangular part is cropped and passed on
        # to pytesseract for extracting text from it
        # Extracted text is then written into the text file
        for cnt in contours:
            
            x, y, w, h = cv2.boundingRect(cnt)
            
            # Drawing a rectangle on copied image
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Cropping the text block for giving input to OCR
            cropped = im2[y:y + h, x:x + w]
            
            # Open the file in append mode
            file = open("recognized.txt", "a")
            
            # Apply OCR on the cropped image
            text = pytesseract.image_to_string(cropped)
            # print(text)
            # Appending the text into file
            file.write(text)
            file.write("\n")
            
            # Close the file
            file.close




    #  to get isbn ,authors and publishers from the txt file 
    def get_info(self, path):
        # To get title
        content = []
        self.get_text(path)
        title_finder = title_getter()
        content.append(title_finder.get_title(path))

        # To get publisher name
        publisher_finder = publisher_getter()
        content.append(publisher_finder.get_publisher())

        # To get author name
        author_finder = author_getter()
        content.append(author_finder.get_author())

        # To get isbn number
        isbn_finder = isbn_getter()
        content.append(isbn_finder.get_isbn())

        return content

    

    # get data from different type of filepath
    def get_data(self, path, flag):
        info = []

        if(flag=="0"):
            text = Text()
            info.append(text.get_info(path))

        else:
            dir_list = os.listdir(path)
            for file_path in dir_list:
                # file path
                file_path = path + "/" + file_path
                if(file_path.lower().endswith(('.png','.jpg','.jpeg'))):
                    text = Text()
                    # append the data extracted from given jpg into the list named info
                    info.append(text.get_info(file_path))

        
        print(info)
        return (info)








