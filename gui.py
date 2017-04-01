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
total_data_size = 10
progressbar_length = 500
top = Tk()
top.geometry("1000x500")
#progress = ttk.Progressbar(top, mode ='determinate', length = progressbar_length, variable = counter_var)
#progress = ttk.Progressbar(top, length = progressbar_length, mode ='determinate', variable = counter_var, maximum = total_data_size)
#progress.place(x=100, y=450)

def process(progress):
	global my_counter, total_data_size, top, progressbar_length, counter_var
	#global progress
	#counter_var = IntVar()
	#progress = ttk.Progressbar(top, length = progressbar_length, mode ='determinate', variable = counter_var, maximum = total_data_size)
	#progress = ttk.Progressbar(top, length = 100)
	progress.place(x=100, y=50)
	for i in range(total_data_size):
		sleep(1)
		counter_var.set(my_counter)
		my_counter += 1
		print("update", my_counter)
		#progress.update()

def thread_start(progress):
	global my_counter, my_data_size, total_data_size, progressbar_length
	print(total_data_size)
	process(progress)
	#step = trunc(progressbar_length/data_size)
	# while my_counter < total_data_size:
	# 	sleep(1)
	# 	#progress.step(step)
	# 	#progress.step(my_counter)
	# 	progress.update()
	# 	#my_counter += 1
	print("Scrapy Done!")
	top.destroy()

def start_button():
	global my_data_size, my_total_thread, progressbar_length, my_counter, total_data_size, counter_var
	global progress, top
	#start scrapy
	my_data_size = int(E1.get())
	print(my_data_size)
	my_total_thread = int(E2.get())
	print(my_total_thread)
	total_data_size = my_data_size * 5
	# Launch the loop once the window is loaded
	progress = ttk.Progressbar(top, length = 100)
	progress["maximum"] = total_data_size
	progress.place(x=100, y=450)
	#thread_start()
	progress.after(1, thread_start(progress))


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


