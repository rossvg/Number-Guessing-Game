'''
Number Guessing Game Program                                        July 21, 2020
Ross Vrana-Godwin

Purpose:
    First program created after basic tutorial. Begin to understand how the random library works,
    how to accept user input, and some small implementation of class and if/else statements. 

July 22, 2020
Implementing high score feature use .txt file read and writes

'''
#......................................BEGIN...............................................................

import random # Import random library
from HighscoreTable import Highscore



def main():

    global mistakes
    mistakes = 0 # Global variable keeping track of game mistakes. Resets with every iteration of main()

    n = Number() #instantiate new Number object

    rNum = n.genRandom() #Generate this games random number.

    n.intro() #print intro message and asks if user wants to see scoring table

    # This while loop compares the user guess to the random number. It will run until the user gets
    # the random number correctly
    while( n.compare(n.getInput(), rNum) == False): # the compare function will return true when both numbers match
        mistakes = mistakes + 1 # every time the loop iterates, it means the user has failes, increasing mistakes by 1
        print("") # CR for visual clarity in terminal
    
    # upon exiting while loop, print mistakes along with win message
    print("Mistakes: " + str(mistakes))

    n.addScore()
    
    # this method determines if the user wishes to play again or not
    n.playAgain()
    









class Number: # this class handles the bulk of the program, including user input, num gerneration, and play again feature
    
    # this method prints a welcome message to the game
    def intro(self):

        yn = input("Welcome! View scores? (y/n): ")

        if (yn == "y"):
            Highscore().show(fileName = ("scores"))
            print("Please guess a number between 0 and 20")

        elif (yn == "n"):
            print("Please guess a number between 0 and 20")


        else:
            print("Invalid Input")
            self.intro
        

    #this method asks the user for an input. It then checks if it is a valid number. Only a valid number will be returned
    def getInput(self):
        
        i = True # neccesarry for loop defintion? must be a way to eliminate
        while i == True: # loops until valid number is recieved

            userNum = input("Guess: ") # ask for number and store user number in userNum
            
            if (userNum.isdigit() == False): #if number is not a digit return false
                print("Not a number. Try again") # run the loop again asking for new input
                
            elif (int(userNum) < 0 or int(userNum) > 20):
                print("Not in range. Try again")
                
            else: # number passes number and range tests and deemed valid (may be other tests, but just this for now)
                i = False #break the loop
            
        return userNum # returns valid integer only
        
            

    def genRandom(self): # this method generates a random number between 1 and 20
        rNum = random.randrange(0,21,1)
        return rNum

    def compare(self, userNum, randNum): # method compares two numbers, and gives information about the difference
        

        if (int(userNum) > randNum):
            print("Too high, try again")
            return False
            
        
        elif (int(userNum) < randNum):
            print("Too low, try again")
            return False
        
        else:
            print("You win!")
            return True


    def playAgain(self):
        yn =  input("Play again? (y/n): ")

        if (yn == "y"):
            main()

        elif (yn == "n"):
            return

        else:
            print("Invalid Input")
            self.playAgain()
    
    def addScore(self):
        name = input("Please enter your name for the scoreboard: \r")
        Highscore().add("scores",mistakes = mistakes,userInput = name)
        Highscore().show("scores")
    




if __name__ == "__main__":
  main()