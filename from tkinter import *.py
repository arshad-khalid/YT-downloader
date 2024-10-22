from tkinter import *
from tkinter import filedialog, messagebox, ttk
from pytube import YouTube
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading

# Create root window
root = Tk()
root.geometry('890x420')
root.title("YouTube Video Downloader")
root.config(bg="#313131")

# Global Variables
link = StringVar()
save_path = StringVar()
filename = StringVar()

# Function to handle downloading
def download_video():
    try:
        url = YouTube(str(link.get()))
        stream = url.streams.filter(res=resolution_var.get(), progressive=True).first()
        stream.download(save_path.get(), filename=filename.get() or stream.default_filename)
        messagebox.showinfo("Success", "Video Downloaded Successfully")
        progress_bar['value'] = 100
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to fetch video thumbnail
def fetch_thumbnail():
    try:
        url = YouTube(str(link.get()))
        response = requests.get(url.thumbnail_url)
        img_data = Image.open(BytesIO(response.content))
        img_data = img_data.resize((180, 120), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img_data)
        thumbnail_label.config(image=img)
        thumbnail_label.image = img
        download_button.config(state=NORMAL)  # Enable download button after fetching thumbnail
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to choose save directory
def browse_directory():
    folder_selected = filedialog.askdirectory()
    save_path.set(folder_selected)

# Function to handle multi-threading for download
def start_download():
    download_button.config(state=DISABLED)  # Disable button to prevent multiple clicks
    progress_bar['value'] = 0  # Reset progress bar
    threading.Thread(target=download_video).start()

# UI Components
Label(root, text='YouTube Video Downloader', font='arial 20 bold', bg="#313131").pack(pady=10)

Label(root, text='Paste Link Here:', font='arial 13 bold', bg="#313131").place(x=50, y=60)
Entry(root, width=50, textvariable=link).place(x=180, y=55)

Label(root, text='Save Location:', font='arial 13 bold', bg="#313131").place(x=50, y=100)
Entry(root, width=50, textvariable=save_path).place(x=180, y=105)
Button(root, text="Browse", command=browse_directory, bg="#313131", fg="black").place(x=560, y=102)

Label(root, text='File Name:', font='arial 13 bold', bg="#313131").place(x=50, y=140)
Entry(root, width=50, textvariable=filename).place(x=180, y=145)

# Video Resolution Option
Label(root, text='Resolution:', font='arial 13 bold', bg="#313131").place(x=50, y=180)
resolution_var = StringVar(value="720p")
resolution_options = ["1080p", "720p", "480p", "360p"]
OptionMenu(root, resolution_var, *resolution_options).place(x=184, y=185)

# Thumbnail Preview Label
thumbnail_label = Label(root, bg="#f5f5f5")
thumbnail_label.place(x=670, y=65, width=180, height=120)

# Fetch thumbnail button
Button(root, text="Fetch Thumbnail", command=fetch_thumbnail, bg="#313131", fg="black").place(x=693, y=200)

# Download Button
download_button = Button(root, text='Download', font='arial 15 bold', padx=2, command=start_download, state=DISABLED, bg="#32cd32", fg="black")
download_button.place(x=370, y=250)

# Progress Bar
progress_bar = ttk.Progressbar(root, length=500, mode='determinate')
progress_bar.place(x=170, y=300)

# Run the Tkinter event loop
root.mainloop()