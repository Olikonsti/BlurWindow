from BlurWindow import *
import tkinter.ttk as ttk

a = Tk()

b = BlurWindow(a, color=a["bg"])
b.enable()

c = ttk.Button(a, text="test")
c.pack()

a.mainloop()