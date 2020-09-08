

import os
from datetime import datetime
import csv



class Highscore:

    def show(self,fileName):

        if (os.path.exists(fileName) == False):
            print("Error, no highscores found")
        
        else:

            f = open(fileName,"r")
            table = f.readlines()
            table.sort

            for x in table:
                print(x)
            
            f.close

    def add(self,fileName,userInput,mistakes):

        now = datetime.now()

        f = open(fileName,"a+")
        f.write("mistakes: " + str(mistakes) + "\t" +  userInput  + "\t" + now.strftime("%a %d %b %Y %I:%M:%S ") + "\r" )
        f.close


     