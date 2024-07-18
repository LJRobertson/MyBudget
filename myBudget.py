"""

Author:  Lindsey Robertson
Date written: 07/13/24
Assignment:   Final Project
Short Desc:   This program is a budget tracker, allowing a user to track how much they have spent for the month. 


"""
from tkinter import *
from tkinter.filedialog import *

#create root widget
root = Tk()
#root.geometry('500x400')

#the following section was done following the tutorial video for frames to get the project started. The final project will include panels within the frame and the frame attributes will be changed.
#create a window
    #can add a text attribute if desired, padding here is inside of frame
masterFrame = LabelFrame(root, padx = 50, pady = 50)
#padding here is outside the frame
masterFrame.pack()

#update window dimensions to frame
# root.update_idletasks()
# #update frame demensions
# masterFrame.update_idletasks()


#create a top frame
topFrame = Frame(masterFrame, width = 475, height = 40, bg = "green")
#grid to frame
topFrame.grid(row = 1, column = 0)

#center the topFrame
# window_width = root.winfo_width()
# frame_width = topFrame.winfo_width()
# x = (window_width - frame_width) // 2
# topFrame.place(x=x, y = 1)

#create a label widget
mainLabel = Label(topFrame, text = "My Budget")
#gridding the label widget to the screen
mainLabel.grid(padx = 50, pady=50, row = 1, column = 0, columnspan=2)

#create left column within master frame
leftFrame = Frame(masterFrame, width = 250, height = 400, bg = "blue")
#grid left frame
leftFrame.grid(row =2, column = 0)
#leftFrame.pack()

#create right column within master frame
rightFrame = Frame(masterFrame, width = 250, height = 400, bg = "pink")
#grid right frame
rightFrame.grid(row = 2, column = 2)
#rightFrame.pack()

#align these frames
# window_width = root.winfo_width()
# x = window_width// 2
# leftFrame.place(masterFrame, x=1, y = 1)
# rightFrame.place(x = x+1, y = 1)

#buttons
#open file button

#Open file
def openFile():
    """Opens a text file and extracts account data before closing the file."""
    f = askopenfile(mode = 'r', filetypes =[('Text Files', '*.txt')])
    if f is not None:
        transactions = f.read()
    else :
        print("Please select a text file.")
    f.close

#open button
openButton = Button(masterFrame, text = "Open File", command = openFile)
#grid to frame 
openButton.grid(row = 0, column = 2)

#Quit Program  
def quitProgram():
    """Closes the application."""
    root.destroy()

#quit program
quitButton = Button(masterFrame, text = "Quit", command = quitProgram)
#grid to frame
quitButton.grid(row = 0, column = 3)





#event loop to run program
root.mainloop()

# def main():
#     myBudget().mainloop()

# if __name__ == "__main__" :
#     main()
