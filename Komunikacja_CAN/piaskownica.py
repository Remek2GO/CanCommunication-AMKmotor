#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

#root window
root =tk.Tk()
root.geometry("240x300")
root.title('Logowanie')
root.resizable(True,True)

now_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(now_value.get())

def value_changed(event):
    current_value.configure(text=get_current_value())

#configure the grid
root.columnconfigure(0, weight='1')
root.columnconfigure(1, weight='3')

#Name
label_name = ttk.Label(root, text="Name:", background='green')
label_name.grid(column='0', row='0', sticky='n', padx='10', pady='5')

entry_name = ttk.Entry(root)
entry_name.grid(column='1', row='0', sticky='n', padx='5', pady='5')

#Password
label_password = ttk.Label(root, text='Password:')
label_password.grid(column='0', row='1', sticky='n', padx='10', pady='5')

entry_password = ttk.Entry(root, show='*')
entry_password.grid(column='1', row='1', sticky='n', padx='5', pady='5')

#Slider
slider = ttk.Scale(root, from_='5', to_='2000', orient='horizontal', command=value_changed, variable=now_value)
slider.grid(column='1', row='2', sticky='we')

current_value_label = ttk.Label(root, text='Slider:')
current_value_label.grid(column='0', row='2', sticky='n')

#Show box
current_value = ttk.Label(root, text=get_current_value())
current_value.grid(column='0', row='3', sticky='s')

#Button
button_login = ttk.Button(root, text='Login')
button_login.grid(column='1', row='3', sticky='n')



root.mainloop()

