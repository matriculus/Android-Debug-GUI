from tkinter import *

def donothing():
   filewin = Toplevel(app)
   button = Button(filewin, text="Do nothing button")
   button.pack()

class AppWindow(Tk):
    width, height = 640, 480
    geo = f"{width}x{height}"
    def __init__(self):
        Tk.__init__(self)
        self.title("Android Debug Bridge (GUI)")
        self.geometry(self.geo)
        self.menuSetup()
        
    def menuSetup(self):
        self.menu = Menu(self)
        # File menu
        filemenu = Menu(self.menu, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.quit)
        self.menu.add_cascade(label="File", menu=filemenu)
        
        # Edit menu
        editmenu = Menu(self.menu, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)

        self.menu.add_cascade(label="Edit", menu=editmenu)

        # Help menu
        helpmenu = Menu(self.menu, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        self.menu.add_cascade(label="Help", menu=helpmenu)

        self.config(menu=self.menu)
    
    def loop(self):
        self.mainloop()


if __name__ == "__main__":
    app = AppWindow()
    app.loop()