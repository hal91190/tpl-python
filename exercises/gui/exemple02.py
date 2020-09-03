from tkinter import *

class MonDessin(Canvas):
    def __init__(self, root):
        Canvas.__init__(self, root)
        self.grid(column = 0, row = 0, sticky = (N, W, E, S))
        self.bind("<Button-1>", self.onLeftClick)
        self.bind("<B1-Motion>", self.onMouseMove)

        self.lastx, self.lasty = 0, 0


    def onLeftClick(self, event):
        self.lastx, self.lasty = event.x, event.y

    def onMouseMove(self, event):
        self.create_line((self.lastx, self.lasty, event.x, event.y))
        self.lastx, self.lasty = event.x, event.y


if __name__ == '__main__':
    root = Tk()
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)

    monDessin = MonDessin(root)

    root.mainloop()
