'''
    This is a tkinter app for downloading youtube videos in highest resolution available. It uses the pytube library to download and play the video. The user can enter youtube video url.
'''
import tkinter as tk
import ttkbootstrap as ttk
from pytube import YouTube
import validators
import os

def clear_error():
    output_result_val.set("")  # Clear the error message

def animate_waiting_message(dot_count):
    if waiting_message_flag:
        output_result_val.set("Fetching video" + "." * dot_count)
        window.after(500, animate_waiting_message, (dot_count + 1) % 4)

waiting_message_flag = True  # Flag to control the waiting message animation

def stop_animation():
    global waiting_message_flag
    waiting_message_flag = False

def on_entry_click(event):
    if entry.get() == 'Enter or Paste YouTube video URL':
        entry.delete(0, "end")  # delete all the text in the entry
        entry_style.configure('Placeholder.TEntry', foreground='black')  # Change text color to black

def download_video():
    global waiting_message_flag
    try:
        link = entry_url.get()
        # Validate the URL
        if not validators.url(link):
            raise ValueError
    except ValueError:
        output_result_val.set("Error: Please enter a valid YouTube video URL!")
        entry.delete(0, tk.END)  # Clear the entry textbox
        window.after(5000, clear_error)  # Schedule clearing error message after 5 seconds
        return

    # Show "Fetching video..." message
    output_result_val.set("Fetching video...")
    window.update()

    # Perform conversion
    video = YouTube(link)
    streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    highest_resolution = streams.first().resolution
    video_title = video.title
    video_resolution = video.streams.get_highest_resolution()

    # Show "Downloading..." message
    output_result_val.set("Downloading...")
    window.update()

    # Check if the folder exists, if not, create it
    folder_name = 'YouTube Videos'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Start waiting message animation
    waiting_message_flag = True
    animate_waiting_message(0)

    # Download the video to the folder
    video_resolution.download(output_path=folder_name)

    # Stop waiting message animation
    stop_animation()

    # Display video information
    output_result_val.set("Video Title: {}\nVideo Resolution: {}\n\nVideo Downloaded Successfully...".format(video_title, highest_resolution))

# window main frame
window = ttk.Window(themename='journal')
window.title('YouTube Video Downloader') # title of window box
window.geometry('1360x300') # widthxheight

# Entry style
entry_style = ttk.Style()
entry_style.configure('Placeholder.TEntry', foreground='grey')  # Placeholder text color

# Input frame
title_label = ttk.Label(master=window, text='YouTube Video Downloader [in highest video quality available (720p Max)]', font='Calibari 24 bold') # Heading/Label of the main frame
title_label.pack()

input_frame = ttk.Frame(master=window) # Input frame
entry_url = tk.StringVar()

entry = ttk.Entry(master=input_frame, textvariable=entry_url, width=50, style='Placeholder.TEntry')
entry.insert(0, 'Enter or Paste YouTube video URL')
entry.bind('<Button-1>', on_entry_click)  # Bind on_entry_click function to Button-1 event
button = ttk.Button(master=input_frame,  text='Download', command=download_video)

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=30)

# Output frame
output_result_val = tk.StringVar()
output_result_label = ttk.Label(master=window, text='', font='Calibari 12', textvariable=output_result_val)

output_result_label.pack(pady=10)

# Run
window.mainloop()