from tkinter import *
import subprocess
import os

win = Tk()

win.title("FILE CONVERTER by Jeric")
win.geometry("350x140")
win.resizable(False, False)

def copy():
    oldname = OneBox.get()
    newname = TwoBox.get()
    subprocess.call(["ffmpeg", "-i", oldname, "-b:a", "320k", newname])

def closeapp():
    sys.exit()

os.chdir("C:\\Users\\user\\Desktop\\JJ\\audio remuxing programs\\ffmpeg")
subprocess.call('echo MP4 files:', shell=True)
subprocess.call('dir /b *.mp4', shell=True)
subprocess.call('echo.', shell=True)
subprocess.call('echo MKV files:', shell=True)
subprocess.call('dir /b *.mkv', shell=True)
subprocess.call('echo.', shell=True)
subprocess.call('echo WEBM files:', shell=True)
subprocess.call('dir /b *.webm', shell=True)
subprocess.call('echo.', shell=True)
subprocess.call('echo M4A files:', shell=True)
subprocess.call('dir /b *.m4a', shell=True)
subprocess.call('echo.', shell=True)

oneLabel = Label(win, text="What's your file name?")
oneLabel.grid(row=0, column=0, sticky=W)
OneBox = Entry(win, width=50)
OneBox.grid(row=1, column=0, sticky=W)

twoLabel = Label(win, text="What's your new file name?")
twoLabel.grid(row=2, column=0, sticky=W)
TwoBox = Entry(win, width=50)
TwoBox.grid(row=3, column=0, sticky=W)

goButton = Button(win, text="GO!", command = copy)
goButton.grid(row=4, column=0, sticky=W)

threeLabel = Label(win, text= "El Psy Kongroo...")
threeLabel.grid(row=5, column=0,sticky=W)

exitButton = Button(win, text="EXIT", command = closeapp)
exitButton.grid(row=5, column=1, sticky=W)

win.mainloop()