import os
from tkinter import *
from pytube import YouTube
from tkinter import messagebox as mb

root = Tk()
root.title("Youtube downloader")
root.geometry('500x400')
root.resizable(0, 0)

Default = os.path.abspath( os.path.dirname( __file__ ))

def video_download():
    url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    video = url.streams.first()# This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
    mp4_format = url.streams.filter(file_extension="mp4")
    high_resol_files = mp4_format.get_highest_resolution()
    #print(url.streams)
    #print(url.streaming_data)
    #print(url.streams.get_highest_resolution().resolution)
    high_resol_files.download(Default) # This is the method with the instruction to download the video.
    Label2 = Label(root, text='Video saved location:  ' + Default, font="calibri 10")
    Label2.place(x=40, y=260)
    Label3 = Label(root, text='Video resolution:  ' + url.streams.get_highest_resolution().resolution, font="calibri 10")
    Label3.place(x=40, y=240)
    label4 = Label(root, text='Video name: '+ url.title, font="calibri 10")
    label4.place(x=40, y=220)
    Label(root, text="Video downloaded", font="calibri 12").place(x=40, y=135) #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.

def audio_download():
    res = mb.askquestion('Confirm', 'Do you want to download Audio only')      
    if res == 'yes' :
        url = YouTube(str(link.get())) 
        audio_only = url.streams.filter(only_audio=True).first()
        down = audio_only.download(Default)
        Label6 = Label(root, text='Audio saved location:  ' + Default, font="calibri 10")
        Label6.place(x=40, y=300)
        label7 = Label(root, text='Audio name: '+ url.title, font="calibri 10")
        label7.place(x=40, y=320)
        Label5 = Label(root, text="Audio downloaded", font="calibri 12")
        Label5.place(x=320, y=135)
        base, ext = os.path.splitext(down)
        new_file = base + '.mp3'
        os.rename(down, new_file)
    else :
        root.destroy() 

Label(root, text="Youtube downloader", font='calibri 13 bold').pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste URL", font='calibri 14 bold').place(x=200, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=35, y=95)

video_icon = PhotoImage(file = r"File_Directory\video.png")
music_icon = PhotoImage(file = r"File_Directory\music.png")
Button1 = Button(root, text= ' Video Download', font = 'calibri 10 bold', image = video_icon, command = video_download, compound = LEFT, bg = '#0059b3', fg = 'white')
Button1.place(x=40, y=160)
Button2 = Button(root, text= ' Audio Download', font = 'calibri 10 bold', image = music_icon, command = audio_download, compound = LEFT, bg = '#8c0327', fg = 'white')
Button2.place(x=320, y=160)


root.mainloop()
