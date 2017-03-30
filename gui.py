import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumrequests import Firefox
import time
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from threading import Thread
import threading
import copy
from math import trunc

from tkinter import *
from tkinter import ttk

# Just to demonstrate
fileList = range(10)

step = trunc(100/len(fileList))

def MAIN():
    for fileName in fileList:
        # The sleeping represents a time consuming process
        # such as reading a file.
        sleep(1)
        print(fileName)
        # Update the progressbar
        progress.step(step)
        progress.update()

    top.destroy()

top = Tk()
top.geometry("1000x500")
def start_button():
	progress = ttk.Progressbar(top, length=500)
	progress.pack()
	progress.after(1, MAIN)
    progress.step(step)
    progress.update()
	#start scrapy
	print("start")

L1 = Label(top, text = "How many people")
L1.place(x=100, y=100)
E1 = Entry(top, bd = 5)
E1.place(x=500, y=100)
L2 = Label(top, text = "How many thread")
L2.place(x=100, y=300)
E2 = Entry(top, bd = 5)
E2.place(x=500, y=300)
B = Button(top, text = "Start Scrapy", command = start_button)
B.place(x=500, y=400)


# Launch the loop once the window is loaded


top.mainloop()
