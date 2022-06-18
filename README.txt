Submitter name: Shivani kumari

Roll No.: 2019csb1120

Course: CS305 Software Engineering

Assignment: 3

1. What does this program do?
It is an application which extracts the metadata from book cover pages.
It extracts book tittle, author name, publisher name and isbn number from the book cover page.
The cover pages are scanned images of book cover.
I have used pytesseract to extract text from the image. For better results , I have preprocessed the image using opencv.
It takes the path of file and flag . Flag indicates wheather the given path is a file path or folder path.

2. A description of how this program works (i.e. its logic)
First it extracts filepath and flag from the command line
Then it calls get_data function from test class and pass path of folder and flag as parameters.
get_data function extracts all the info for the book cover  and return the info
Now in the main , we write all the information to excel sheet by using the excel class and its write_in_excel method.


3. How to compile and run this program?
commands needed to brefore running the program
pip3 install pytesseract
pip3 install opencv-python

Solid Principles used 
Each class that I have implemented is responsible for handling its own functionality.
Each class is open for extension and close for modification.
Low level class closely related to hardware and High level class has been made.

Run the main program 
python3 main.py flag path
flag = 0  if path given is a file path
flag = 1  if path given is a folder path


To run the test cases, first install 
pip3 install pytest
python3 -m pytest test_main.py


for coverage report
# python3 -m coverage run --source=./files/ -m pytest test_main.py
# python3 -m coverage report -i




