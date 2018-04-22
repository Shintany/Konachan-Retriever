import tkinter as tk
from tkinter import ttk
from tools import *
from Retriever import *
import threading
import time
import PIL
 
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg=args)

        ####### FRAME COLOR #######

        self.mainFrame_color = 'gray26'
        self.progression_color = 'gray14'
        self.entry_color = 'gray80'

        ##### LOAD HEADER IMAGE #######

        self.header_image = PIL.ImageTk.PhotoImage(file=r'image/Konachan_Retriever_header.gif')
        canvas = tk.Canvas(parent, width=640, height = 180,bg=self.mainFrame_color)
        canvas.pack(side='top')
        canvas.create_image(310,0, anchor = 'n',image=self.header_image)

        ####### STRING VARS #######

        self.tagList = []
        self.nb_images_wished = 0
        self.progressBarList = []
        self.labelList = []

        ####### INITIALIZING #######

        self.mainFrame = Main(self, self.mainFrame_color)
        self.progressionFrame = Progression(self, self.progression_color)
        self.status = StatusBar(self, 'Initializing...', self.mainFrame_color, 'w')
        self.status.pack(side='bottom', fill='x')

        tagsStr = tk.StringVar(self.mainFrame, value='long_hair,green_eyes,pantsu')
        nbStr = tk.StringVar(self.mainFrame, value='10')

        ######## MAIN FRAME ########

        # self.tmpHeader = Space(self.mainFrame, 'blue', 640, 180)
        topSpace = Space(self.mainFrame, self.mainFrame_color, 640, 1) #Top space
        leftSpace = Space(self.mainFrame, self.mainFrame_color, 40, 50) #left space
        self.tagsLabel = Label(self.mainFrame, 'Tags', self.mainFrame_color)
        self.tagsEntry = Entry(self.mainFrame, self.entry_color, tagsStr)
        middleSpace = Space(self.mainFrame, self.mainFrame_color, 30, 50) #middle space
        self.nbLabel = Label(self.mainFrame, 'Number', self.mainFrame_color)
        self.nbEntry = Entry(self.mainFrame, self.entry_color, nbStr)
        self.startButton = Button(self.mainFrame, 'Start', self.run, self.mainFrame_color)
        bottomSpace = Space(self.mainFrame, self.mainFrame_color, 640, 15)
        bottomSpace2 = Space(self.mainFrame, self.mainFrame_color, 640, 15)

            ## MAIN FRAME PACKING ##

        # self.tmpHeader.pack(side='top')
        topSpace.pack(side='top')
        leftSpace.pack(side='left')
        self.mainFrame.pack(side='top', fill='both')
        bottomSpace.pack(side='bottom')
        self.startButton.pack(side='bottom')
        bottomSpace2.pack(side='bottom')
        self.tagsLabel.pack(side='left')
        self.tagsEntry.pack(side='left')
        middleSpace.pack(side='left')
        self.nbLabel.pack(side='left')
        self.nbEntry.pack(side='left')
    
        ######## PROGRESSION FRAME ########

        self.progressionHeaderLabel = Label(self.progressionFrame, 'PROGRESSION', self.progression_color)
        Space(self.progressionFrame, self.progression_color, 640, 1).pack(side='bottom', fill='y')

            ## PROGRESSION FRAME PACKING ##

        self.progressionFrame.pack(side='top', fill='both')
        self.progressionHeaderLabel.pack(side='top')
        self.status.config(text='Fill Tags and Number, then click on the Start button')

        ######## TAGS LABEL FRAME ########
        self.tagsLabelFrame = tk.Frame(self.progressionFrame, bg=self.progression_color,width= 150, padx=10)
        self.tagsLabelFrame.pack(side='left', fill='y')

    def run(self):
        
        self.tagList.clear()
        self.labelList.clear()

        self.status.config(text='Processing...')
        tag_str = self.tagsEntry.get()
        nb_str = self.nbEntry.get()

        # RETRIEVE INFORMATIONS
        self.tagList = tag_str.split(',')
        self.nb_images_wished = int(nb_str)

        # DEBUG TO CHECK IF THE PROGRAM GOT THE RIGHT DATA
        print ('You asked for :', self.nb_images_wished, 'images')
        print ('With the tags : ')
        for i in range (0, len(self.tagList)):
            print ('\t-> ' + self.tagList[i])
            self.labelList.append(Label(self.tagsLabelFrame, self.tagList[i], self.progression_color))
            self.labelList[i].pack(side='top')
            self.progressBarList.append(ttk.Progressbar(self.progressionFrame, length=300, value=0, max=100))
            self.progressBarList[i].pack(side='top')
            # if i != (len(self.tagList) - 1):
            #     Space(self.progressionFrame, self.progression_color, 640, 10).pack(side='top')
        
        Retriever(self.tagList, self.nb_images_wished, self.progressBarList, self.labelList).start()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Konachan Retriever')
    root.update_idletasks()
    dim = '640x480'
    root.geometry(dim)
    root.resizable(False, False)
    MainApplication(root, 'gray26').pack(side='top', fill='both',expand=True)
    root.mainloop()
