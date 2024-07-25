"""

Author:  Lindsey Robertson
Date written: 07/13/24
Assignment:   Final Project
Short Desc:   This program is a budget tracker, allowing a user to track how much they have spent for the month. 


"""
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import PhotoImage
from PIL import ImageTk, Image

class MyBudget:
    def __init__(self, root):
        self.root = root
        self.root.title("My Budget")

        #create a window
        self.masterFrame = LabelFrame(self.root, padx = 25, pady = 25)

        #padding here is outside the frame
        self.masterFrame.pack()

        #create a top frame
        self.topFrame = Frame(self.masterFrame, width = 475, height = 25, bg = "green")
        #grid to frame
        self.topFrame.grid(row = 1, columnspan= 4)

        #open image
        self.cashImage = Image.open("C:\\Users\\Lindsey Robertson\\Documents\\Ivy Tech\\Intro to Sofware Dev\\MyBudget\\cash.png")

        #resize image
        resizedCashImage = self.cashImage.resize((200, 70))

        self.newCashImage = ImageTk.PhotoImage(resizedCashImage)

        #display image using label 
        imageLabel = Label(self.topFrame, image = self.newCashImage) 
        #Grid to frame
        #imageLabel.place(x=0, y=0) 
        imageLabel.grid(row = 0, columnspan= 4)

        #create a label widget
        self.mainLabel = Label(self.topFrame, text = "My Budget", font = 'bold')
        #gridding the label widget to the screen 
        self.mainLabel.grid(padx = 75, pady=5, row = 1, columnspan=4)
        #self.mainLabel.pack()

        #create left column within master frame
        self.leftFrame = Frame(self.masterFrame, width = 225, height = 375, bg = "blue")
        #grid left frame
        self.leftFrame.grid(row =2, column= 0)
        #leftFrame.pack()

        #transaction discription box left frame
        self.transDescriptionBox = Text(self.leftFrame, height = 20, width = 30, padx = 1, pady = 10, state = "disabled")
        self.transDescriptionBox.pack()

        #create right column within master frame
        self.rightFrame = Frame(self.masterFrame, width = 225, height = 375, bg = "pink")
        #grid right frame
        self.rightFrame.grid(row = 2, column = 1)
        #rightFrame.pack()

        #transaction Amount box right frame
        self.transAmountBox = Text(self.rightFrame, height = 20, width = 30, padx = 1, pady = 10, state = "disabled")
        self.transAmountBox.pack()


        #create bottom frame
        self.bottomFrame = Frame(self.masterFrame, background= "orange")
        #grid to frame
        self.bottomFrame.grid(row = 3, columnspan=4)
        #Transaction total in bottom frame
        self.transTotalLabel = Label(self.bottomFrame, text = "Transaction Total:")
        #add to frame
        self.transTotalLabel.grid(row = 0, column=0, padx = 10, pady = 10)
        #transaction total output box
        self.transTotalBox = Entry(self.bottomFrame, state = "readonly")
        #add to frame
        self.transTotalBox.grid(row = 0, column=1)

        #open button
        openButton = Button(self.masterFrame, text = "Open File", command = self.openFile)
        #grid to frame 
        openButton.grid(row = 0, column = 1, sticky = "NSEW")

        #Transaction Button
        transactionButton = Button(self.masterFrame, text = "Add Transaction", command = self.addTransaction)
        transactionButton.grid(row = 0, column =2, sticky ="NSEW")

        #quit program
        quitButton = Button(self.masterFrame, text = "Quit", command = self.quitProgram)
        #grid to frame
        quitButton.grid(row = 0, column = 3, sticky = "NSEW")


        #Transaction Display File
        #text

        #buttons
        #open file button
        #Open file
    def openFile(self):
        """Opens a text file and extracts account data before closing the file."""
        #Open the file for read and append. This creates an open window for user to select a txt file. Other file options are removed.
        self.f = askopenfile(mode = 'r', filetypes =[('Text Files', '*.txt')])
        #clear the text field from first character through end of field for both boxes
        self.transDescriptionBox.delete(1.0, END)
        self.transAmountBox.delete(1.0, END)
        #enable boxes
        self.transDescriptionBox.config(state ="normal")
        self.transAmountBox.config(state ="normal")

        #read the file
        transactionContent = self.f.read()
        transactions = transactionContent.splitlines()
        #go through file line by line
        for transaction in transactions:
                #split into a description and an amount
                descriptAndAmount =transaction.split(":")
                description, amount = descriptAndAmount
                #add the description to the desctiption box
                self.transDescriptionBox.insert(END, description.strip(), '\n')
                #add amount to Amount box
                self.transAmountBox.insert(END, amount.strip(), '\n')
        #disable text boxes again
        self.transDescriptionBox.config(state = "disabled")
        self.transAmountBox.config(state = "disabled")
        self.f.close()
        
            
    
    def addTransaction(self):
        """Opens a new window to add transaction information."""
        #create Window
        self.addTransactionWindow = Toplevel(self.root)
        #title window
        self.addTransactionWindow.title("Add Transaction")
        #create a frame to hold the widgets
        self.transactionFrame = Frame(self.addTransactionWindow, padx = 25, pady = 25)
        #add frame to grid
        self.transactionFrame.pack()

        #create Add Transaction Label
        self.addTransactionLabel = Label(self.transactionFrame, text = "Add Transaction", font = 'bold')
        #grid to frame
        self.addTransactionLabel.grid(row = 0, columnspan=2)

        #create transaction label
        self.transactionLabel = Label(self.transactionFrame, text = "Transaction Description: ")
        #add to grid
        self.transactionLabel.grid(row = 1, column = 0)

        #transaction description entry
        self.transactionDescription = Entry(self.transactionFrame, width = 20)
        self.transactionDescription.grid(row = 1, column = 1)

        #create amount label
        self.transactionAmountLabel = Label(self.transactionFrame, text = "Transaction Amount : $")
        #add to grid
        self.transactionAmountLabel.grid(row = 2, column = 0)

        #transaction amount entry
        self.transactionAmountEntry = Entry(self.transactionFrame, width = 20)
        #add to grid
        self.transactionAmountEntry.grid(row = 2, column = 1)

        #submit button
        self.submitButton = Button(self.transactionFrame, text= "Submit", pady=5)
        self.submitButton.grid(row = 3, columnspan =2)

        #open image
        self.pigImage = Image.open("C:\\Users\\Lindsey Robertson\\Documents\\Ivy Tech\\Intro to Sofware Dev\\MyBudget\\goldenpig.jpg")
        #resize image
        self.resizedPigImage = self.pigImage.resize((200, 80))
        self.newPigImage = ImageTk.PhotoImage(self.resizedPigImage)
        #display image using label 
        self.pigImageLabel = Label(self.transactionFrame, image = self.newPigImage) 
        #Grid to frame
        self.pigImageLabel.grid(row=5, columnspan = 2)


    #Quit Program  
    def quitProgram(self):
        """Closes the application."""
        self.root.destroy()

#event loop to run program
def main():
    root=Tk()
    app = MyBudget(root)
    root.mainloop()

if __name__ == "__main__":
    main()
