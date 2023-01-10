from tkinter import *
#Label(text='Spam').pack()
#mainloop()

from tkinter.messagebox import showinfo

def reply():
	showinfo(title='popup', message='Button pressed!')
	
window = Tk()
window.title('GUI tkinter')
window.geometry("500x200")
button1 = Button(window, text='press', command=reply)
button2 = Button(window, text='close', command=reply)
button1.place(x=50, y=50)
button2.place(x=50, y=100)
button1.pack()
button2.pack()
window.mainloop()
