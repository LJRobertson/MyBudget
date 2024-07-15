"""

Author:  Lindsey Robertson
Date written: 07/13/24
Assignment:   Final Project
Short Desc:   This program is a budget tracker, allowing a user to track how much they have spent for the month. 


"""
from tkinter import *

#create root widget
root = Tk()

#the following section was done following the tutorial video for frames to get the project started. The final project will include panels within the frame and the frame attributes will be changed.
#create a window
    #can add a text attribute if desired, padding here is inside of frame
mainFrame = LabelFrame(root, padx = 50, pady = 50)
#padding here is outside the frame
mainFrame.pack(padx = 100, pady = 100)
#create a label widget
mainLabel = Label(mainFrame, text = "My Budget")
#gridding the label widget to the screen
mainLabel.grid(row = 0, column = 0)


#event loop to run program
root.mainloop()

# def main():
#     myBudget().mainloop()

# if __name__ == "__main__" :
#     main()
