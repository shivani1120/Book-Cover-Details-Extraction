
from files.excel import Excel
from files.text import Text
import sys
import os


if(len(sys.argv)>3):
    print("More than expected arguments")
    sys.exit()
elif (len(sys.argv)<3):
    print("Less than expected arguments")
    sys.exit()

# store flag tells whether to process a single input file or a directory
flag = sys.argv[1] 

# store path of file
path = sys.argv[2] 


if(not os.path.exists(path)):
    print("File does not exist")
    sys.exit()
elif (flag=="0" and os.path.isdir(path)==False and path.lower().endswith(('.png','.jpeg','.jpg'))==False):
    print("Invalid file format")
    sys.exit()
elif (flag=="0" and os.path.isdir(path)==True):
    print("Expected a file path")
    sys.exit()
elif flag=="1" and os.path.isdir(path)==False:
    print("Expected a folder path")
    sys.exit()


info = Text().get_data(path,flag)
xlsx = Excel()
xlsx.write_in_excel(info)

