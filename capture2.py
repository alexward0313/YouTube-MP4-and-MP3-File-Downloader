from tkinter import *
from tkinter import filedialog
import time
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube


#select filepath function
def select_filepath():
    #allows user to select a path from the file explorer
    path = filedialog.askdirectory()
    pathl.config(text = path)

def downloadmp4():
    #get the link
    get_link = linkf.get()
    #get selected path
    get_path = pathl.cget("text")
    #download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download(get_path)
    screen.title("Download is Complete!")

def downloadmp3():
    #get the link
    get_link = linkf.get()
    #get selected path
    get_path = pathl.cget("text")
    #download audio of video
    mp3_video = YouTube(get_link).streams.filter(only_audio=True).first().download(get_path)
    screen.title("Download is Complete!")


#setting up the gui
screen = Tk()
#title of application is Mnemosyne after the Roman God of Memory
title = screen.title("Mnemosyne")
#this is setting the gui parameters 
canvas = Canvas(screen, width = 500, height=500)
canvas.pack()





#entry box
linkf = Entry(screen, width = 50)
#entry label
linkl = Label(screen, text = "Please enter Video Link: ", font = ("Ariel", 15))

#select file path label
pathl = Label(screen, text = "Select Download Path", font = ("Ariel", 15))
#select file entry button
pathb = Button(screen, text = "Select", width = 30, command = select_filepath)
#pathl placement
canvas.create_window(250, 140, window = pathl)
#pathb placement
canvas.create_window(250, 190, window = pathb)


canvas.create_window(250, 50, window = linkl, )
#entry label placement
canvas.create_window(250, 90, window = linkf)
#entry box placement

#downloadmp4 button
downloadmp4_button = Button(screen, text = "Download MP4 File", command = downloadmp4, width = 30)
#downloadmp4 button placement
canvas.create_window(250, 260, window = downloadmp4_button)

#downloadmp3 button
downloadmp3_button = Button(screen, text = "Download MP3 File", command = downloadmp3, width = 30)
#downloadmp3 button placement
canvas.create_window(250, 320, window = downloadmp3_button)



#instructions
inst1 = Label(screen, text = "1. Copy Link to Video and Enter into Video Link Entry Box", font = ("Ariel", 10))
inst2 = Label(screen, text = "2. Select the Download Path for Video", font = ("Ariel", 10))
inst3 = Label(screen, text = "3. Press Download and Enjoy!", font = ("Ariel", 10))

#instructions placement
canvas.create_window(250, 380, window = inst1)
canvas.create_window(250, 420, window = inst2)
canvas.create_window(250, 460, window = inst3)

orr = Label(screen, text = "or", font = ("Ariel", 10))
canvas.create_window(250, 290, window = orr)


screen.mainloop()
