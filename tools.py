import tkinter as tk
from tkinter import ttk
import threading
import time
from PIL import ImageTk, Image
import os
import sys
import csv

class Main(tk.Frame):
    def __init__(self, parent, color):
        tk.Frame.__init__(self, parent, bg=color)
        self.parent = parent
        self.color = color

class StatusBar(tk.Label):
    def __init__(self, parent, _text, _color, _anchor):
        self.text = _text
        tk.Label.__init__(self, parent, text=_text, bd=1, bg=_color,relief='sunken', anchor=_anchor)
    
class Label(tk.Label):
    def __init__(self, parent, _text, _bg='None',_font='None'):
        tk.Label.__init__(self, parent, text=_text, bg=_bg, font=_font, padx=10)
        self.parent = parent

class Entry(tk.Entry):
    def __init__(self, parent, _bg, _string):
        tk.Entry.__init__(self, parent, textvariable=_string, bg=_bg)
        
class Space(tk.Frame):
    def __init__(self, parent, _bg,_width, _height):
        tk.Frame.__init__(self, parent, bg=_bg, width=_width, height=_height)
        self.parent = parent

class Button(tk.Button):
    def __init__(self, parent, _text, _command, _bg):
        tk.Button.__init__(self, parent, text=_text, command=_command, bg=_bg)

class Progression(tk.Frame):
    def __init__(self, parent, color):
        tk.Frame.__init__(self, parent, bg=color)
        self.parent = parent
        self.color = color

def create_directory(_path):
    if not os.path.exists(_path):
        #print ('Creating directory...')
        os.makedirs(_path)
        csv_file = open(_path + 'database.csv', 'w')
        csv_file.close()
        return 0
    else:
        #print ('Directory already exist!')
        list = os.listdir(_path) # dir is your directory path
        number_files = len(list)
        return number_files

def already_dl(_link, _database_path):
    database = open(_database_path, 'r')
    readCSV = csv.reader(database, delimiter='\n')
    for row in readCSV:
        if (row[0] == _link):
            #print ('Already downloaded...')
            database.close()
            return True
    database.close()
    return False