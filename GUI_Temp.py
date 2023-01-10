from tkinter import *
class MyWindow:
	def __init__(self,window):
		self.label1 = Label(window, text='Temp in Degree Celcius')
		self.label2 = Label(window, text='Temp in Fahrenheit')
		self.celcius = Entry(bd=3)
		self.fahren = Entry(bd=3)
		self.button = Button(window, text='Convert')
		self.label1.place(x=100, y=50)
		self.celcius.place(x=250, y=50)
		self.label2.place(x=70, y=100)
		self.fahren.place(x=250, y=100)
		#self.btn = (window, text='Convert', command=self.convert)
		self.btn = Button(window, text='Convert')
		self.btn.bind('<Button-1>', self.convert)
		self.btn.place(x=300, y=150)
	
	def convert(self, event):
		self.fahren.delete(0, 'end')
		num1=float(self.celcius.get())
		result=(num1*1.8)+32
		self.fahren.insert(END, str(result))

gui = Tk()
mywin=MyWindow(gui)
gui.title('Celcius to Fahrenheit')
gui.geometry("500x300")
gui.mainloop()
