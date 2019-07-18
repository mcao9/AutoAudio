from tkinter import *
import tkinter as tk
import os
import signal
import subprocess

#p = subprocess.Popen(['head', 'README.txt'])
#command definitions
#record button functions, aka button
bool = 0

class App(tk.Frame): #class for making the window
    
    def __init__(self, master=None): #where info on what the window displays is defined
        super().__init__(master)
        
        self.pack() #where user input and instructions go

        #makes a control panel within the window. We will use this to hold the buttons
        controlPanel = LabelFrame(self, text = 'Control Panel') 
        controlPanel.config(bg='lightgreen', height = '250', width = '400') 
        controlPanel.pack(side = LEFT)
        self.create_controls_widgets(controlPanel)
        
        #makes an instructions panel within the window.
        instrPanel = LabelFrame(self, text = 'Instructions') 
        instrPanel.config(bg='pink', height = '250', width = '400') 
        instrPanel.pack(side = LEFT)
        self.create_instructions(instrPanel)
        
        #makes output panel
        outputPanel = LabelFrame(master, text = 'Output:') 
        outputPanel.config(bg='white', height = '250', width = '800') 
        outputPanel.pack()
        #scrollbar
        scrollbar = Scrollbar(outputPanel)
        scrollbar.pack( side = RIGHT, fill = Y )
        #output listed here
        mylist = Listbox(outputPanel, yscrollcommand = scrollbar.set )
        #mylist = Text(outputPanel, yscrollcommand = scrollbar.set )
        for line in range(100): #replace with music note output
           mylist.insert(END, "This is line number " + str(line))
        mylist.config(height = '350', width = '800')
        mylist.pack( side = LEFT, fill = BOTH )
        scrollbar.config( command = mylist.yview )
        
    def create_controls_widgets(self, panel): #where info displayed in control panel is defined
        #global e1
        #global e2
        #global e3
        #display status for recording/not recording
        label = Label(panel, text="Not Recording", font=("Helvetica", 12), fg="red")
        label.place(x=220, y=20, anchor="w")
        
        #Label of fileName entry field
        #Label(panel, text="Put Output Filename Here:").place(x=20, y=60, anchor="w")
        #e1 = Entry(panel)
        #e1.place(x=170, y=60, anchor="w")
        #Label(panel, text="Put the Song Name Here:").place(x=20, y=90, anchor="w")
        #e2 = Entry(panel)
        #e2.place(x=165, y=90, anchor="w")
        #Label(panel, text="Put the Song Writer's Name Here:").place(x=20, y=120, anchor="w")
        #e3 = Entry(panel)
        #e3.place(x=205, y=120, anchor="w")
        #default name
        #fileName = "NoteSheet"
        #authorName = "Author"
        #songName = "My Song 1"
        
        #buttons for control panel
        button = Button(panel, text="Start Recording", command = self.record)
        button.place(x=20, y=20, anchor="w")
        button2 = Button(panel, text="Stop Recording", command = self.stopR)
        button2.place(x=120, y=20, anchor="w")
        button3 = Button(panel, text="Quit AutoAudio", command = self.quit)
        button3.place(x=20, y=190, anchor="w")
        
    def create_instructions(self, panel): #the text that goes inside the instructions panel  
        instrText = Message(panel, text="Welcome to AutoAudio!\n\nThis program uses the LilyPond music engraving program to help YOU write your own sheet music!\nNo need to understand complex music theory!\nJust hit “Start Recording” and start singing, playing your favorite instrument, or just making sounds.\nWhen you’re done expressing yourself, press “Stop Recording” and your song will be written for you.\nJust run the resultant “NoteSheet.ly” file with LilyPond and open the PDF file written by the program to see it.\nNow anyone can be a music composer! Hit “Start” and have fun!\n\nInstall LilyPond: lilypond.org", font=("Helvetica", 8)) #replace with instructions text
        instrText.config(bg='pink', width = '350')
        instrText.place(x=20, y=0, anchor='nw')
       
    def record(self):
        global p
        global bool
        if bool == 0:
            #T.delete('1.0', END)
            #T.insert(END,"Recording")
            label = Label(self, text="    Recording   ", font=("Helvetica", 12), fg="green")
            label.place(x=222, y=36, anchor="w")
            temp = subprocess.call('cleaner.sh',shell = True)
            #time counter
            i = 0
            #test code
            #print(temp)
            #while temp isn't done, wait until it's done
            while temp != 0:
                i = i+1
                if i>5000:
                    temp.terminate()
                    break
            p = subprocess.Popen(['python', 'main.py'])
            #test code, use instead of subprocess if thing don't work
            #p = subprocess.Popen(['python', 'WindowManager.py'])
        bool = 1
        #print(fileName)
        
        
    #stop record button functions, aka button 2
    def stopR(self):
        global fileName
        global songName
        global authorName
        global bool
        if bool == 1:
            p.terminate()
            #T.delete('1.0', END)
            #T.insert(END,"Not Recording")
            label = Label(self, text="Not Recording", font=("Helvetica", 12), fg="red")
            label.place(x=222, y=36, anchor="w")
            #open("output.pdf")
            # if e1.get() != "":
                # fileName = e1.get()
            # if e2.get() != "":
                # songName = e2.get()
            # if e3.get() != "":
                # authorName = e3.get()
            #check if there was any recording done
            #pass filename into lilypond or freqAnalyzer
        bool = 0
		
    #quitting the program, aka button 3
    def quit(self):
        if bool == 1:
            if p != 0:
                p.terminate()
        exit()
        
    def getFName():
        global fileName
        return fileName

    def getAName():
        global authorName
        return authorName

    def getSName():
        global songName
        return songName
# create the application for the user to see
myapp = App()

myapp.master.title("AutoAudio")
myapp.master.geometry('800x600')

# start the program
myapp.mainloop()