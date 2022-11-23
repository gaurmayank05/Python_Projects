from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import time

Yt_Downloader = Tk()
Yt_Downloader.geometry('500x300')
Yt_Downloader.resizable(0,0)
Yt_Downloader.title("Youtube Downloader")
Label(Yt_Downloader,text= 'Youtube Video Downloader', font= 'arial 20 bold').pack()

progress = ttk.Progressbar(Yt_Downloader, orient= "horizontal", length= 477, mode='determinate')
progress.place(x=10,y=270)

def download():
    link = v1.get()
    yt = YouTube(link)
    Output_PATH = "E:\VIDEOS"
    filename = None
    filename_prefix = None
    existing_name = None
    timeout = None
    max_retries = None

    quality = s1.get()

    try:

        if (quality == "144p"):
            stream = yt.streams.get_by_itag(17)

        elif (quality == "360p"):
            stream = yt.streams.get_by_itag(18)
        
        elif (quality == "720p"):
            stream = yt.streams.get_by_itag(22)

        else:
            messagebox.showerror(Yt_Downloader,"Youtube Video downloader","Error")

        t = yt.title
        l6.config(text = t)

        len = yt.length
        if ((len > 3600) or (len == 3600)):
            len = (len/3600)
            len = (str(len) + "hours")
            l8.config(text=len)
        if (len < 3600):
            len = round(len/60)
            len = (str(len) + "minutes")
            l8.config(text=len)

        size = stream.filesize
        if (size < 1073741824):
            size = round(size*0.000001)
            size = (str(size)+"MB")
            l10.config(text=size)
        

        progress['value']=20
        Yt_Downloader.update_idletasks()
        time.sleep(1)

        progress['value']=40
        Yt_Downloader.update_idletasks()
        time.sleep(1)

        progress['value']=60
        Yt_Downloader.update_idletasks()
        time.sleep(1)

        progress['value']=80
        Yt_Downloader.update_idletasks()
        time.sleep(1)

        progress['value']=100
        Yt_Downloader.update_idletasks()
        time.sleep(1)

        stream.download(Output_PATH)
        messagebox.showinfo("Youtube Downloader",'Download Complete')

    except Exception:
        messagebox.showerror("Youytube downloader", "Server Error!!"'\n'"Check your Internet Connection")

# LINK
l1 = Label(Yt_Downloader, text='URL')
l1.place(x=30,y=60)

l2 = Label(Yt_Downloader, text='Select Quality')
l2.place(x=30,y=100)

l3 = Label(Yt_Downloader, text='Output Path')
l3.place(x=30,y=140)

l4 = Label(Yt_Downloader, text='E:\Videos')
l4.place(x=150,y=140)

l6 = Label(Yt_Downloader, text='')
l6.place(x=150,y=165)

l7 = Label(Yt_Downloader,text='Video Length :')
l7.place(x=30,y=190)

l8 = Label(Yt_Downloader,text='')
l8.place(x=150,y=190)

l9 = Label(Yt_Downloader,text='Video size :')
l9.place(x=30,y=215)

l10 = Label(Yt_Downloader,text='')
l10.place(x=150,y=215)


v1 = StringVar()
e1 = Entry(Yt_Downloader,textvariable=v1)
e1.place(x=100,y=60)

b2 = Button(Yt_Downloader, width=8, text= "Cancel", font="arial 13 bold",bg='red',command=Yt_Downloader.quit)
b2.place(x=250,y=100)

s1 = StringVar()
video_quality = ttk.Combobox(Yt_Downloader,width=5,textvariable=s1)
video_quality.place(x=120,y=100)
video_quality['values'] = ('144p',
                            '360p',
                            '720p')


b1 = Button(Yt_Downloader, width=10, text="Download", font= "arial 13 bold" ,bg='green',command=download)
b1.place(x=250,y=60)

b2 = Button(Yt_Downloader, width=8, text= "Cancel", font="arial 13 bold",bg='red',command=Yt_Downloader.quit)
b2.place(x=250,y=100)
Yt_Downloader.mainloop()