# imports
from tkinter import *
import tkinter as tk
import sys


global proceed


# main
def main():
    cal_gui = CalculatorGUI()
    w = cal_gui.createWindow()  # create window
    f1 = cal_gui.welcomeFrame(w)  # create welcome frame

    l1 = cal_gui.welcomeLabel(f1)  # display welcome text
    b1 = cal_gui.proceedBtn(f1)  # Proceed button
    b2 = cal_gui.exitBtn(f1, w)  # Exit button

    # check if widget exists 
    frameExists =  cal_gui.proceedFrame(w).winfo_exists()
    if frameExists == 1:
        pass
    else:
        sys.exit("No frame found")
    f2 = cal_gui.proceedFrame(w)

    w.mainloop()


# class - calculator
class Calculator:
    def __init__():
        pass


# class - calculator GUI
class CalculatorGUI:
    global proceed
    proceed = 0

    def __init__(self):
        ...

    def createWindow(self):
        self.myWindow = Tk()
        self.myWindow.title("My Calculator")
        self.myWindow.geometry("400x600")
        return self.myWindow
    
    def welcomeFrame(self, myWindow):
        self.wFrame = LabelFrame(myWindow, padx=15, pady=150, relief="flat")
        self.wFrame.pack(anchor=CENTER)
        return self.wFrame
    
    def proceedFrame(self, myWindow):
        self.wFrame.destroy()
        # create new frame (Frame 2)
        self.pFrame = LabelFrame(myWindow, text="Success!", padx=15, pady=30)
        self.pFrame.pack(anchor=CENTER)
        return self.pFrame
    
    def welcomeLabel(self, wFrame):
        self.myLabel = Label(wFrame, text="Welcome to Calculator", font=("Arial", 20))
        self.myLabel.grid(row=0, column=0, sticky="we", pady=15)
        return self.myLabel

    def proceedBtn(self, wFrame):
        self.myButton = Button(wFrame, text="Proceed", width=10, command=self.proceedFrame)
        self.myButton.grid(row=1, column=0, pady=5)
        return self.myButton

    def exitBtn(self, wFrame, myWindow):
        self.myButton = Button(wFrame, text="Exit", width=10, command=myWindow.quit)
        self.myButton.grid(row=2, column=0, pady=5)
        return self.myButton
    
    def createFields(self, pFrame):
        self.entry1 = Entry(pFrame)
        self.entry1.grid(row=0, column=1, sticky="E", padx=15)

        self.entry2 = Entry(pFrame)
        self.entry2.grid(row=1, column=1, sticky="E", padx=15)


if __name__ == "__main__":
    main()