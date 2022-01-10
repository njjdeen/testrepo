'''

Puzzle file for the advanced modules section

The goal of this module is to unzip a directory with a bunch of random text files.
In one of the text files a phone number is hidden. find the phone number.

'''

#extract instructions first

import zipfile
import os
import re

# first unzip zip file and change working directory to unzipped files
zipobj = zipfile.ZipFile("C:\\Users\\Devoteam\\Documents\\Pythoncourse\\Complete-Python-3-Bootcamp-master\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions.zip", "r")

zipobj.extractall("extracted instructions")

os.chdir("C:\\Users\\Devoteam\\Documents\\Pythoncourse\\Complete-Python-3-Bootcamp-master\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\extracted_content")


#search every text file within each directory

directory_names = ['one', 'two', 'three', 'four', 'five']

for name in directory_names:
    directory = os.getcwd() + "\\" + name
    #print(directory)
    for filename in os.listdir(directory):
        f = open(directory+ "\\" + filename,'r')
        pattern = r'\d{3}-\d{3}-\d{4}'
        
        #search for pattern in every line of current textfile
        
        for line in f:
            for match in re.findall(pattern, line):
                
                print(f"Phone number found: {match}")
                print("\n")
                print(f"phone number was found in {directory}\\{filename}")
            
            