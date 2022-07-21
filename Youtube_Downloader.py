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
    Label2 = Label(root, text='Video saved in location:  ' + Default)
    Label2.place(x=40, y=260)
    Label3 = Label(root, text='Video resolution:  ' + url.streams.get_highest_resolution().resolution)
    Label3.place(x=40, y=240)
    label4 = Label(root, text='Video name: '+ url.title)
    label4.place(x=40, y=220)
    Label(root, text="Video downloaded", font="calibri 12").place(x=48, y=120) #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.

def audio_download():
    res = mb.askquestion('Confirm', 'Do you want to download Audio only')      
    if res == 'yes' :
        url = YouTube(str(link.get())) 
        audio_only = url.streams.filter(only_audio=True).first()
        down = audio_only.download(Default)
        Label6 = Label(root, text='Audio saved in location:  ' + Default)
        Label6.place(x=40, y=300)
        label7 = Label(root, text='Audio name: '+ url.title)
        label7.place(x=40, y=320)
        Label5 = Label(root, text="Audio downloaded", font="calibri 12")
        Label5.place(x=318, y=120)
        base, ext = os.path.splitext(down)
        new_file = base + '.mp3'
        os.rename(down, new_file)
    else :
        root.destroy() 

Label(root, text="Youtube downloader", font='calibri 13 bold').pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste URL", font='calibri 14 bold').place(x=200, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)

Button1 = Button(root, text='Video Downloader', font='calibri 14 bold', bg='blue', padx=2,command= video_download)
Button1.place(x=40, y=160)
Button2 = Button(root, text='Audio downloader', font='calibri 14 bold', bg='red', padx=2, command= audio_download)
Button2.place(x=310, y=160)


root.mainloop()
