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

from tkinter import *
from tkinter import ttk
#import tkFont

my_counter = 0
my_data_size = 1 #input
my_total_thread = 1 #input
total_data_size = 10
progressbar_length = 100

bg_ = "#a1dbcd" #http://wiki.tcl.tk/37701
fg_ = "azure"	#color scheme

#font = tkFont.Font()
top = Tk()
top.geometry("800x500")
top.configure(background = bg_)
top.title("Scrapy!")
counter_var = IntVar()

progress = ttk.Progressbar(top, length = progressbar_length)

def process():
	global my_counter, total_data_size, progressbar_length, counter_var
	for i in range(total_data_size):
		sleep(1)
		counter_var.set(my_counter)
		my_counter += 1
		print("update", my_counter)
		#progress.update()

def thread_start(progress):
	global my_counter, my_data_size, total_data_size, progressbar_length, counter_var
	global top
	print(total_data_size)
	#progress["length"] = progressbar_length/2
	#process(progress)
	#print(progressbar_length)
	step = int(progressbar_length/total_data_size)
	#step = int(100/total_data_size)
	#progress["length"] = progressbar_length * 2
	print(step)
	while my_counter < total_data_size:
		sleep(1)
		#progress.step(step)
		#progress.step(my_counter)
		#progress.update()
		#counter_var.set(my_counter)
		my_counter += 1
		print("update", my_counter)
	print("Scrapy Done!")
	top.destroy()

def start_button():
	global my_data_size, my_total_thread, progressbar_length, my_counter, total_data_size, counter_var
	global progress, top
	#start scrapy
	loading = Label(text="Loading.....", background="white")
	loading.place(x=300, y=400)
	my_data_size = int(E1.get())
	my_total_thread = int(E2.get())
	total_data_size = my_data_size * 5
	#progress["maximum"] = total_data_size
	# Launch the loop once the window is loaded
	#progress = ttk.Progressbar(top, length = progressbar_length)
	#progress = ttk.Progressbar(top, length = progressbar_length, mode ='determinate', variable = counter_var, maximum = total_data_size)
	progress.place(x=300, y=450)
	progress.start(100)
	thread_start(progress)
	#progress.after(1, thread_start(progress))


L1 = Label(top, text = "How long to scrapy: ", bg = bg_)
L1.config(font=('Helvetica', 36, 'bold'))
L1.place(x=250, y=80)
E1 = Entry(top, fg = bg_, bg = fg_)
E1.place(x=300, y=150)
L2 = Label(top, text = "How many thread: ", bg = bg_)
L2.config(font=('Helvetica', 36, 'bold'))
L2.place(x=250, y=200)
E2 = Entry(top, fg = bg_, bg = fg_)
E2.place(x=300, y=270)
B = Button(top, text = "Start Scrapy", command = start_button, fg = bg_, bg = bg_)
B.config(font=('Helvetica' , 12,'bold'))
B.place(x=340, y=350)
top.mainloop()


