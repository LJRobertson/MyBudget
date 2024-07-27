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
from tkinter import messagebox

class MyBudget:
    def __init__(self, root):
        self.root = root
        self.root.title("My Budget")

        #create a window
        self.masterFrame = LabelFrame(self.root, padx = 25, pady = 25)
        #add to grid
        self.masterFrame.pack()

        #create a top frame
        self.topFrame = Frame(self.masterFrame, width = 475, height = 25, bg = "green")
        #grid to frame
        self.topFrame.grid(row = 1, columnspan= 5)

        #open image
        self.cashImage = Image.open("C:\\Users\\Lindsey Robertson\\Documents\\Ivy Tech\\Intro to Sofware Dev\\MyBudget\\cash.png")
        #resize image
        resizedCashImage = self.cashImage.resize((250, 88))
        self.newCashImage = ImageTk.PhotoImage(resizedCashImage)
        #display image using label 
        imageLabel = Label(self.topFrame, image = self.newCashImage, text = "cash image") 
        #Grid to frame
        imageLabel.grid(row = 0, columnspan= 4)

        #create a label widget
        self.mainLabel = Label(self.topFrame, text = "My Budget", font = ("Arial",16,'bold'), padx = 10, fg = "green")
        #gridding the label widget to the screen 
        self.mainLabel.grid(padx = 58, pady=5, row = 1, columnspan=4)

        #create left column within master frame
        self.leftFrame = Frame(self.masterFrame)
        #grid left frame
        self.leftFrame.grid(row =2, column= 0)
        #leftFrame.pack()

        #transaction discription box left frame
        self.transDescriptionBox = Text(self.leftFrame, height = 20, width = 25, padx = 1, pady = 10, state = "disabled")
        self.transDescriptionBox.pack()

        #create right column within master frame
        self.rightFrame = Frame(self.masterFrame)
        #grid right frame
        self.rightFrame.grid(row = 2, column = 1)

        #transaction Amount box right frame
        self.transAmountBox = Text(self.rightFrame, height = 20, width = 25, padx = 1, pady = 10, state = "disabled")
        self.transAmountBox.pack()

        #create BOTTOM FRAME
        self.bottomFrame = Frame(self.masterFrame, background= "green")
        #grid to frame
        self.bottomFrame.grid(row = 3, columnspan=4)
        #Transaction total in bottom frame
        self.transTotalLabel = Label(self.bottomFrame, text = "Transaction Total:")
        #add to frame
        self.transTotalLabel.grid(row = 1, column=0, padx = 10, pady = 5)
        #transaction total output box
        self.transTotalBox = Label(self.bottomFrame, text = "$ 0.00")
        #add to frame
        self.transTotalBox.grid(row = 1, column=1, padx = 10)

        
        #BUTTONS
        # #open button
        openButton = Button(self.masterFrame, text = "Open File", command = self.open_file)
        #add hover color change
        openButton.bind('<Enter>', self.on_enter)
        openButton.bind('<Leave>', self.on_leave)
        #grid to frame 
        openButton.grid(row = 0, column = 0, sticky = "NSEW")

        #Transaction Button
        transactionButton = Button(self.masterFrame, text = "Add Transaction", command = self.add_transaction_window)
        transactionButton.grid(row =0, column = 1, sticky ="NSEW")
        #change button color on hover
        transactionButton.bind('<Enter>', self.on_enter)
        transactionButton.bind('<Leave>', self.on_leave)


        #quit program button -- ADD HOVER AND
        quitButton = Button(self.masterFrame, text = "Quit", command = self.quit_program)
        #bind to hover methods
        quitButton.bind('<Enter>', self.on_enter)
        quitButton.bind('<Leave>', self.on_leave)
        #grid to frame
        quitButton.grid(row = 0, column = 2, sticky = "NSEW")

    def on_enter(self, button):
        """Changes a button color on hover."""
        button.widget.config(background='lightblue', foreground= "white")
    #change button color back
    def on_leave(self, button):
        """Changes a button color back to normal after a hover."""
        button.widget.config(background= 'SystemButtonFace', foreground= 'black')
            
        #Open file
    def open_file(self):
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
                descriptAndAmount =transaction.split(",")
                description, amount = descriptAndAmount
                #add the description to the desctiption box and move to a new line
                self.transDescriptionBox.insert(END, description.strip(" "))
                self.transDescriptionBox.insert(END, '\n')
                #add amount to Amount box and move to a new line
                self.transAmountBox.insert(END, amount.strip(" "))
                self.transAmountBox.insert(END, '\n')

        #disable text boxes again
        self.transDescriptionBox.config(state = "disabled")
        self.transAmountBox.config(state = "disabled")
        self.f.close()

        #update the total
        self.update_total()
    
    def update_total(self):
         """Updates the transaction total."""
         #get the total of the transactions
         total = 0
         #get the transaction dollar amounts from the amount box
         amounts = self.transAmountBox.get(1.0, END)
         for amount in amounts.splitlines():
              #remove any whitespace
              amount = amount.strip()
              try:
                total += float(amount)
              except:
                #if blank lines are encountered, ignore them
                  continue
         #convert total to sting and ensure two decimal places
         totalString = "{:.2f}".format(total)
         #write total to box
         self.transTotalBox.config(text = "$ " + totalString)
         
    def add_transaction_window(self):
        """Opens a new window to add transaction information."""
        #create Window
        self.add_transaction_window = Toplevel(self.root)
        #title window 
        self.add_transaction_window.title("Add Transaction")
        #create a frame to hold the widgets
        self.transactionFrame = Frame(self.add_transaction_window, padx = 25, pady = 25)
        #add frame to grid
        self.transactionFrame.pack()

        #create Add Transaction Label
        self.add_transactionLabel = Label(self.transactionFrame, text = "Add Transaction", font = 'bold')
        #grid to frame
        self.add_transactionLabel.grid(row = 0, columnspan=2)

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
        self.submitButton = Button(self.transactionFrame, text= "Submit", command = self.add_transaction)
        self.submitButton.grid(row = 3, column =0)
        #add hover color change
        self.submitButton.bind('<Enter>', self.on_enter)
        self.submitButton.bind('<Leave>', self.on_leave)


        #cancel button
        self.cancelButton = Button(self.transactionFrame, text = "Cancel", command = self.add_transaction_window.destroy)
        self.cancelButton.grid(row = 3, column = 1 )
        #add hover color change
        self.cancelButton.bind('<Enter>', self.on_enter)
        self.cancelButton.bind('<Leave>', self.on_leave)


        #open image
        self.pigImage = Image.open("C:\\Users\\Lindsey Robertson\\Documents\\Ivy Tech\\Intro to Sofware Dev\\MyBudget\\goldenpig.jpg")
        #resize image
        self.resizedPigImage = self.pigImage.resize((200, 80))
        self.newPigImage = ImageTk.PhotoImage(self.resizedPigImage)
        #display image using label 
        self.pigImageLabel = Label(self.transactionFrame, image = self.newPigImage, text = "golden piggy bank") 
        #Grid to frame
        self.pigImageLabel.grid(row=5, columnspan = 2)
    
    def add_transaction(self):
         """Adds entered transaction information to the list on the main screen."""
         #validate entries

         if self.validate_user_entry() == True:
            #get transaction description
            enteredDescription = self.transactionDescription.get()
            #get transaction amount
            enteredAmount = self.transactionAmountEntry.get()
            #enable the transaction boxes
            self.transDescriptionBox.config(state = "normal")
            self.transAmountBox.config(state = "normal")

            #add transaction information
            self.transDescriptionBox.insert(END, enteredDescription)
            self.transDescriptionBox.insert(END, '\n')
            self.transAmountBox.insert(END, enteredAmount)
            self.transAmountBox.insert(END, '\n')

            #disable the transaction boxes
            self.transDescriptionBox.config(state = "disabled")
            self.transAmountBox.config(state = "disabled")

            #update transaction total
            self.update_total()

            #close the window after entering transaction
            self.add_transaction_window.destroy()

    def validate_user_entry(self):
        """Validates that description entered by user is not blank."""
        enteredDescription = self.transactionDescription.get()
        enteredAmount = self.transactionAmountEntry.get()
        if enteredDescription == "":
            messagebox.showerror('Error', "Error: Entry cannot be blank.")
            return False
        elif enteredAmount == "":
            messagebox.showerror('Error', "Error: Amount cannot be blank.")
        elif enteredAmount.isalpha():
            messagebox.showerror('Error', "Error: Amount must be numeric.")
        else:
            return True

    #Quit Program  
    def quit_program(self):
        """Closes the application."""
        self.root.destroy()

#event loop to run program
def main():
    root=Tk()
    app = MyBudget(root)
    root.mainloop()

if __name__ == "__main__":
    main()
