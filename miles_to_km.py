'''
    This is a tkinter app for converting miles to kilometer.
'''

import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def clear_error():
    output_result_val.set("")  # Clear the error message

def convert():
    # Check if the input is numerical
    try:
        reqVal = float(entry_int.get())
    except ValueError:
        output_result_val.set("Error: Please enter a numerical value!")
        entry.delete(0, tk.END)  # Clear the entry textbox
        window.after(10000, clear_error)  # Schedule clearing error message after 10 seconds
        return
    # Perform conversion
    res_ouput = reqVal * 1.61
    output_result_val.set("Converted Distance: {:.2f} km".format(res_ouput))

# window main frame
window = ttk.Window(themename='journal')
window.title('Distance Converter') # title of window box
window.geometry('900x600') # widthxheight

# input frame
title_label = ttk.Label(master=window, text='Convert Distance (miles to km)', font='Calibari 24 bold') # Heading/Label of the main frame
title_label.pack()

input_frame = ttk.Frame(master=window) # input frame
entry_int = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame,  text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=30)

# output frame
output_result_val = tk.StringVar()
output_result_label = ttk.Label(master=window, text='', font='Calibari 12', textvariable=output_result_val)

output_result_label.pack(pady=10)

# run
window.mainloop()