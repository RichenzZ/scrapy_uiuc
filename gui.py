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

my_counter = 0
my_data_size = 1 #input
my_total_thread = 1 #input
progressbar_length = 100

top = Tk()
top.geometry("1000x500")
progress = ttk.Progressbar(top, length=progressbar_length)

def progress_fuction():
	global my_counter
	global my_data_size
	data_size = my_data_size * 10
	print("data_size = ", data_size)
	step = trunc(progressbar_length/data_size * 10)
	for i in range(data_size):
		sleep(1)
		progress.step(step)
		progress.update()
		my_counter += 1
	print("Scrapy Done!")
	top.destroy()

def start_button():
	global my_data_size
	global my_total_thread
	#start scrapy
	my_data_size = int(E1.get())
	print(my_data_size)
	my_total_thread = int(E2.get())
	print(my_total_thread)
	#progress = ttk.Progressbar(top, length=500)
	progress.place(x=100, y=450)

	# Launch the loop once the window is loaded
	progress.after(1, progress_fuction)
	#top.mainloop()

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
top.mainloop()


