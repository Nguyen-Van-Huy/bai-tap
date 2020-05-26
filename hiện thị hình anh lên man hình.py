from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Label")
        self.img = Image.open("Photos\\nguoichoi.jpg.png")
        tatras = ImageTk.PhotoImage(self.img)
        label = Label(self, image=tatras)
        label.image = tatras
        label.pack()
        self.pack()
    def setGeometry(self):
        w, h = self.img.size
        self.parent.geometry(("%dx%d+300+300") % (w, h))
root = Tk()
ex = Example(root)
ex.setGeometry()
root.mainloop()
