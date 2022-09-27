#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

#root window
root =tk.Tk()
root.geometry("1400x750")
root.title('Obsługa silnika AMK - CAN BUS')
root.resizable(1, 1)

#configure the grid
root.columnconfigure(0, weight='1')
root.columnconfigure(1, weight='2')
root.columnconfigure(2, weight='1')
root.columnconfigure(3, weight='2')
root.columnconfigure(4, weight='1')
root.columnconfigure(5, weight='1')
root.columnconfigure(6, weight='2')
root.columnconfigure(7, weight='1')
root.columnconfigure(8, weight='2')

#Motor Labels
motor_1_label = ttk.Label(root, text='Motor 1',font=('Arial', 18))
motor_1_label.grid(column='1', row='0', sticky='e', pady='10')

motor_2_label = ttk.Label(root, text='Motor 2',font=('Arial', 18))
motor_2_label.grid(column='6', row='0', sticky='e', pady='10')

motor_3_label = ttk.Label(root, text='Motor 3',font=('Arial', 18))
motor_3_label.grid(column='1', row='15', sticky='e', pady='30')

motor_4_label = ttk.Label(root, text='Motor 4',font=('Arial', 18))
motor_4_label.grid(column='6', row='15', sticky='e', pady='30')

all_motors_label = ttk.Label(root, text='All Motors', font=('Arial', 18))
all_motors_label.grid(column='4', row='25', sticky='w', pady='20')

#MOTOR 1
#Motor 1 Left side
current_value_tv_1 = tk.DoubleVar()

target_torque_1_label = ttk.Label(root, text='Target Torque:') #Target Torque
target_torque_1_label.grid(column='0', row='1', sticky='e')
target_torque_1_slider = ttk.Scale(root, from_='0', to_='20000', variable=current_value_tv_1)
target_torque_1_slider.grid(column='1', row='1',sticky='we')

torque_limit_positiv_1_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Positiv
torque_limit_positiv_1_label.grid(column='0', row='2', sticky='e')
torque_limit_positiv_1_entry = ttk.Entry(root)
torque_limit_positiv_1_entry.grid(column='1', row='2', pady='5')

torque_limit_negativ_1_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Negativ
torque_limit_negativ_1_label.grid(column='0', row='3', sticky='e')
torque_limit_negativ_1_entry = ttk.Entry(root)
torque_limit_negativ_1_entry.grid(column='1', row='3',pady='5')

inverter_on_1_label = ttk.Label(root, text='Inverter ON:') #Inverter ON
inverter_on_1_label.grid(column='0', row='4', sticky='e')
inverter_on_1_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
inverter_on_1_button.grid(column='1', row='4')

hv_activation_1_label = ttk.Label(root, text='HV activation:') #HV activation
hv_activation_1_label.grid(column='0', row='5', sticky='e')
hv_activation_1_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
hv_activation_1_button.grid(column='1', row='5')

def button_command ():
    text="Zmiana"
    torque_limit_positiv_1_entry.insert(0,text)

remove_error_1_label = ttk.Label(root, text='Remove Error:') #Remove Error
remove_error_1_label.grid(column='0', row='6', sticky='e')
remove_error_1_button = ttk.Button(root, text='Remove', command=button_command)
remove_error_1_button.grid(column='1', row='6')

driver_enable_1_label = ttk.Label(root, text='Driver enbale:') #Driver enable
driver_enable_1_label.grid(column='0', row='7', sticky='e')
driver_enable_1_button = ttk.Checkbutton(root, onvalue=1, offvalue=0)
driver_enable_1_button.grid(column='1', row='7')
#driver_enable_1_button.state(["selected"])

#Motor 1 Right side
actual_velocity_1_label = ttk.Label(root, text='Actual Velocity:') #Actual Velocity
actual_velocity_1_label.grid(column='2', row='1',sticky='e')
actual_velocity_1_value = ttk.Label(root, text='xxx'+ ' rpm')
actual_velocity_1_value.grid(column='3', row='1')

torque_current_1_label = ttk.Label(root, text='Torque Current:') #Torque Current
torque_current_1_label.grid(column='2', row='2',sticky='e')
torque_current_1_value = ttk.Label(root, text='xxx')
torque_current_1_value.grid(column='3', row='2')

magnetizing_current_1_label = ttk.Label(root, text='Magnetizing Current:') #Magnetizing Current
magnetizing_current_1_label.grid(column='2', row='3',sticky='e')
magnetizing_current_1_value = ttk.Label(root, text='xxx')
magnetizing_current_1_value.grid(column='3', row='3')

temperature_motor_1_label = ttk.Label(root, text='Temperature of motor:') #Temperature of Motor
temperature_motor_1_label.grid(column='2', row='4',sticky='e')
temperature_motor_1_value = ttk.Label(root, text='xxx' + ' C')
temperature_motor_1_value.grid(column='3', row='4')

temperature_inverter_1_label = ttk.Label(root, text='Temperature of inverter:') #Temperature of Inverter
temperature_inverter_1_label.grid(column='2', row='5',sticky='e')
temperature_inverter_1_value = ttk.Label(root, text='xxx' + ' C')
temperature_inverter_1_value.grid(column='3', row='5')

temperature_igbt_1_label = ttk.Label(root, text='Temperature of IGBT:') #Temperature of IGBT
temperature_igbt_1_label.grid(column='2', row='6',sticky='e')
temperature_igbt_1_value = ttk.Label(root, text='xxx' + ' C')
temperature_igbt_1_value.grid(column='3', row='6')

error_info_1_label = ttk.Label(root, text='Error info:') #Error info
error_info_1_label.grid(column='2', row='7',sticky='e')
error_info_1_value = ttk.Label(root, text='xxx')
error_info_1_value.grid(column='3', row='7')

#MOTOR 2
#Motor 2 Left side
current_value_tv_2 = tk.DoubleVar()

target_torque_2_label = ttk.Label(root, text='Target Torque:') #Target Torque
target_torque_2_label.grid(column='5', row='1', sticky='e')
target_torque_2_slider = ttk.Scale(root, from_='0', to_='20000', variable=current_value_tv_2)
target_torque_2_slider.grid(column='6', row='1',sticky='we')

torque_limit_positiv_2_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Positiv
torque_limit_positiv_2_label.grid(column='5', row='2', sticky='e')
torque_limit_positiv_2_entry = ttk.Entry(root)
torque_limit_positiv_2_entry.grid(column='6', row='2', pady='5')

torque_limit_negativ_2_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Negativ
torque_limit_negativ_2_label.grid(column='5', row='3', sticky='e')
torque_limit_negativ_2_entry = ttk.Entry(root)
torque_limit_negativ_2_entry.grid(column='6', row='3',pady='5')

inverter_on_2_label = ttk.Label(root, text='Inverter ON:') #Inverter ON
inverter_on_2_label.grid(column='5', row='4', sticky='e')
inverter_on_2_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
inverter_on_2_button.grid(column='6', row='4')

hv_activation_2_label = ttk.Label(root, text='HV activation:') #HV activation
hv_activation_2_label.grid(column='5', row='5', sticky='e')
hv_activation_2_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
hv_activation_2_button.grid(column='6', row='5')

remove_error_2_label = ttk.Label(root, text='Remove Error:') #Remove Error
remove_error_2_label.grid(column='5', row='6', sticky='e')
remove_error_2_button = ttk.Button(root, text='Remove')
remove_error_2_button.grid(column='6', row='6')

driver_enable_2_label = ttk.Label(root, text='Driver enbale:') #Driver enable
driver_enable_2_label.grid(column='5', row='7', sticky='e')
driver_enable_2_button = ttk.Checkbutton(root, onvalue=1, offvalue=0)
driver_enable_2_button.grid(column='6', row='7')

#Motor 2 Right side
actual_velocity_2_label = ttk.Label(root, text='Actual Velocity:') #Actual Velocity
actual_velocity_2_label.grid(column='7', row='1',sticky='e')
actual_velocity_2_value = ttk.Label(root, text='xxx'+ ' rpm')
actual_velocity_2_value.grid(column='8', row='1')

torque_current_2_label = ttk.Label(root, text='Torque Current:') #Torque Current
torque_current_2_label.grid(column='7', row='2',sticky='e')
torque_current_2_value = ttk.Label(root, text='xxx')
torque_current_2_value.grid(column='8', row='2')

magnetizing_current_2_label = ttk.Label(root, text='Magnetizing Current:') #Magnetizing Current
magnetizing_current_2_label.grid(column='7', row='3',sticky='e')
magnetizing_current_2_value = ttk.Label(root, text='xxx')
magnetizing_current_2_value.grid(column='8', row='3')

temperature_motor_2_label = ttk.Label(root, text='Temperature of motor:') #Temperature of Motor
temperature_motor_2_label.grid(column='7', row='4',sticky='e')
temperature_motor_2_value = ttk.Label(root, text='xxx' + ' C')
temperature_motor_2_value.grid(column='8', row='4')

temperature_inverter_2_label = ttk.Label(root, text='Temperature of inverter:') #Temperature of Inverter
temperature_inverter_2_label.grid(column='7', row='5',sticky='e')
temperature_inverter_2_value = ttk.Label(root, text='xxx' + ' C')
temperature_inverter_2_value.grid(column='8', row='5')

temperature_igbt_2_label = ttk.Label(root, text='Temperature of IGBT:') #Temperature of IGBT
temperature_igbt_2_label.grid(column='7', row='6',sticky='e')
temperature_igbt_2_value = ttk.Label(root, text='xxx' + ' C')
temperature_igbt_2_value.grid(column='8', row='6')

error_info_2_label = ttk.Label(root, text='Error info:') #Error info
error_info_2_label.grid(column='7', row='7',sticky='e')
error_info_2_value = ttk.Label(root, text='xxx')
error_info_2_value.grid(column='8', row='7')

#MOTOR 3
#Motor 3 Left side
current_value_tv_3 = tk.DoubleVar()

target_torque_3_label = ttk.Label(root, text='Target Torque:') #Target Torque
target_torque_3_label.grid(column='0', row='16', sticky='e')
target_torque_3_slider = ttk.Scale(root, from_='0', to_='20000', variable=current_value_tv_3)
target_torque_3_slider.grid(column='1', row='16',sticky='we')

torque_limit_positiv_3_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Positiv
torque_limit_positiv_3_label.grid(column='0', row='17', sticky='e')
torque_limit_positiv_3_entry = ttk.Entry(root)
torque_limit_positiv_3_entry.grid(column='1', row='17', pady='5')

torque_limit_negativ_3_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Negativ
torque_limit_negativ_3_label.grid(column='0', row='18', sticky='e')
torque_limit_negativ_3_entry = ttk.Entry(root)
torque_limit_negativ_3_entry.grid(column='1', row='18',pady='5')

inverter_on_3_label = ttk.Label(root, text='Inverter ON:') #Inverter ON
inverter_on_3_label.grid(column='0', row='19', sticky='e')
inverter_on_3_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
inverter_on_3_button.grid(column='1', row='19')

hv_activation_3_label = ttk.Label(root, text='HV activation:') #HV activation
hv_activation_3_label.grid(column='0', row='20', sticky='e')
hv_activation_3_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
hv_activation_3_button.grid(column='1', row='20')

remove_error_3_label = ttk.Label(root, text='Remove Error:') #Remove Error
remove_error_3_label.grid(column='0', row='21', sticky='e')
remove_error_3_button = ttk.Button(root, text='Remove')
remove_error_3_button.grid(column='1', row='21')

driver_enable_3_label = ttk.Label(root, text='Driver enbale:') #Driver enable
driver_enable_3_label.grid(column='0', row='22', sticky='e')
driver_enable_3_button = ttk.Checkbutton(root, onvalue=1, offvalue=0)
driver_enable_3_button.grid(column='1', row='22')

#Motor 3 Right side
actual_velocity_3_label = ttk.Label(root, text='Actual Velocity:') #Actual Velocity
actual_velocity_3_label.grid(column='2', row='16',sticky='e')
actual_velocity_3_value = ttk.Label(root, text='xxx'+ ' rpm')
actual_velocity_3_value.grid(column='3', row='16')

torque_current_3_label = ttk.Label(root, text='Torque Current:') #Torque Current
torque_current_3_label.grid(column='2', row='17',sticky='e')
torque_current_3_value = ttk.Label(root, text='xxx')
torque_current_3_value.grid(column='3', row='17')

magnetizing_current_3_label = ttk.Label(root, text='Magnetizing Current:') #Magnetizing Current
magnetizing_current_3_label.grid(column='2', row='18',sticky='e')
magnetizing_current_3_value = ttk.Label(root, text='xxx')
magnetizing_current_3_value.grid(column='3', row='18')

temperature_motor_3_label = ttk.Label(root, text='Temperature of motor:') #Temperature of Motor
temperature_motor_3_label.grid(column='2', row='19',sticky='e')
temperature_motor_3_value = ttk.Label(root, text='xxx' + ' C')
temperature_motor_3_value.grid(column='3', row='19')

temperature_inverter_3_label = ttk.Label(root, text='Temperature of inverter:') #Temperature of Inverter
temperature_inverter_3_label.grid(column='2', row='20',sticky='e')
temperature_inverter_3_value = ttk.Label(root, text='xxx' + ' C')
temperature_inverter_3_value.grid(column='3', row='20')

temperature_igbt_3_label = ttk.Label(root, text='Temperature of IGBT:') #Temperature of IGBT
temperature_igbt_3_label.grid(column='2', row='21',sticky='e')
temperature_igbt_3_value = ttk.Label(root, text='xxx' + ' C')
temperature_igbt_3_value.grid(column='3', row='21')

error_info_3_label = ttk.Label(root, text='Error info:') #Error info
error_info_3_label.grid(column='2', row='22',sticky='e')
error_info_3_value = ttk.Label(root, text='xxx')
error_info_3_value.grid(column='3', row='22')

#MOTOR 4
#Motor 4 Left side
current_value_tv_4 = tk.DoubleVar()

target_torque_4_label = ttk.Label(root, text='Target Torque:') #Target Torque
target_torque_4_label.grid(column='5', row='16', sticky='e')
target_torque_4_slider = ttk.Scale(root, from_='0', to_='20000', variable=current_value_tv_4)
target_torque_4_slider.grid(column='6', row='16',sticky='we')

torque_limit_positiv_4_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Positiv
torque_limit_positiv_4_label.grid(column='5', row='17', sticky='e')
torque_limit_positiv_4_entry = ttk.Entry(root)
torque_limit_positiv_4_entry.grid(column='6', row='17', pady='5')

torque_limit_negativ_4_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Negativ
torque_limit_negativ_4_label.grid(column='5', row='18', sticky='e')
torque_limit_negativ_4_entry = ttk.Entry(root)
torque_limit_negativ_4_entry.grid(column='6', row='18',pady='5')

inverter_on_4_label = ttk.Label(root, text='Inverter ON:') #Inverter ON
inverter_on_4_label.grid(column='5', row='19', sticky='e')
inverter_on_4_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
inverter_on_4_button.grid(column='6', row='19')

hv_activation_4_label = ttk.Label(root, text='HV activation:') #HV activation
hv_activation_4_label.grid(column='5', row='20', sticky='e')
hv_activation_4_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
hv_activation_4_button.grid(column='6', row='20')

remove_error_4_label = ttk.Label(root, text='Remove Error:') #Remove Error
remove_error_4_label.grid(column='5', row='21', sticky='e')
remove_error_4_button = ttk.Button(root, text='Remove')
remove_error_4_button.grid(column='6', row='21')

driver_enable_4_label = ttk.Label(root, text='Driver enbale:') #Driver enable
driver_enable_4_label.grid(column='5', row='22', sticky='e')
driver_enable_4_button = ttk.Checkbutton(root, onvalue=1, offvalue=0)
driver_enable_4_button.grid(column='6', row='22')

#Motor 4 Right side
actual_velocity_4_label = ttk.Label(root, text='Actual Velocity:') #Actual Velocity
actual_velocity_4_label.grid(column='7', row='16',sticky='e')
actual_velocity_4_value = ttk.Label(root, text='xxx'+ ' rpm')
actual_velocity_4_value.grid(column='8', row='16')

torque_current_4_label = ttk.Label(root, text='Torque Current:') #Torque Current
torque_current_4_label.grid(column='7', row='17',sticky='e')
torque_current_4_value = ttk.Label(root, text='xxx')
torque_current_4_value.grid(column='8', row='17')

magnetizing_current_4_label = ttk.Label(root, text='Magnetizing Current:') #Magnetizing Current
magnetizing_current_4_label.grid(column='7', row='18',sticky='e')
magnetizing_current_4_value = ttk.Label(root, text='xxx')
magnetizing_current_4_value.grid(column='8', row='18')

temperature_motor_4_label = ttk.Label(root, text='Temperature of motor:') #Temperature of Motor
temperature_motor_4_label.grid(column='7', row='19',sticky='e')
temperature_motor_4_value = ttk.Label(root, text='xxx' + ' C')
temperature_motor_4_value.grid(column='8', row='19')

temperature_inverter_4_label = ttk.Label(root, text='Temperature of inverter:') #Temperature of Inverter
temperature_inverter_4_label.grid(column='7', row='20',sticky='e')
temperature_inverter_4_value = ttk.Label(root, text='xxx' + ' C')
temperature_inverter_4_value.grid(column='8', row='20')

temperature_igbt_4_label = ttk.Label(root, text='Temperature of IGBT:') #Temperature of IGBT
temperature_igbt_4_label.grid(column='7', row='21',sticky='e')
temperature_igbt_4_value = ttk.Label(root, text='xxx' + ' C')
temperature_igbt_4_value.grid(column='8', row='21')

error_info_4_label = ttk.Label(root, text='Error info:') #Error info
error_info_4_label.grid(column='7', row='22',sticky='e')
error_info_4_value = ttk.Label(root, text='xxx')
error_info_4_value.grid(column='8', row='22')

#ALL MOTORS
#All Motors Left

current_value_tv_all = tk.DoubleVar()

target_torque_all_label = ttk.Label(root, text='Target Torque:') # Target Torque
target_torque_all_label.grid(column='2', row='26',sticky='e')
target_torque_all_slider = ttk.Scale(root, from_='0', to_='20000', variable=current_value_tv_all)
target_torque_all_slider.grid(column='3', row='26', sticky='we', pady='10')

torque_limit_positiv_all_label = ttk.Label(root, text='Torque Limit Positiv:') #Torque Limit Positive
torque_limit_positiv_all_label.grid(column='2', row='27',sticky='e')
torque_limit_positiv_all_entry = ttk.Entry(root)
torque_limit_positiv_all_entry.grid(column='3', row='27')

torque_limit_negative_all_label = ttk.Label(root, text='Torque Limit Negative:') #Torque Limit Negative
torque_limit_negative_all_label.grid(column='2', row='28',sticky='e', pady='10')
torque_limit_negative_all_entry = ttk.Entry(root)
torque_limit_negative_all_entry.grid(column='3', row='28', pady='10')

#All Motor Right
hv_activation_all_label = ttk.Label(root, text='HV activation:') #HV activation
hv_activation_all_label.grid(column='5', row='26', sticky='e')
hv_activation_all_button = ttk.Checkbutton(root, onvalue=1, offvalue=0 )
hv_activation_all_button.grid(column='6', row='26')

remove_error_all_label = ttk.Label(root, text='Remove Error:') #Remove Error
remove_error_all_label.grid(column='5', row='27', sticky='e')
remove_error_all_button = ttk.Button(root, text='Remove')
remove_error_all_button.grid(column='6', row='27')

#STOP Button
stop_button = tk.Button(root, text='STOP', height=3, width=20, background='red')
stop_button.grid(column='7', row='30')

root.mainloop()