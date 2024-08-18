from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print('file_pat: ',file_path)
    #mp4 =  YouTube(video_path).streams.get_highest_resolution().download()
    #video_clip = VideoFileClip(mp4)
    #video_clip.close()
    select = YouTube(video_path).streams.filter(progressive=True,file_extension='mp4').last()
    mp4 = select.download(file_path)

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

root = Tk()
root.title('Video Downloader')
canvas = Canvas(root,width=350,height=300)
canvas.pack()

#app label
app_label = Label(root,text="Video downloader",fg='blue',font=('Arial',20))
canvas.create_window(175,20,window=app_label)

#entry to accept video URL
url_label = Label(root,text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(175,80,window=url_label)
canvas.create_window(175,100,window=url_entry)

#path to download videos
path_label = Label(root,text="Selcet path to download")
path_button = Button(root,text="Select",command=get_path)
canvas.create_window(175,150,window=path_label)
canvas.create_window(175,170,window=path_button)

#download button
download_button = Button(root,text='Download',command=download)
canvas.create_window(175,250,window=download_button)

root.mainloop()