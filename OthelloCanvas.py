
import tkinter as tk 

from Constants import *
class OthelloCanvas(tk.Canvas):
    def __init__(self, **kwargs):
        tk.Canvas.__init__(self, **kwargs)
        self.width = WIDTH
        self.height = HEIGHT
        self.configure(background="#009933")
        
        self.draw_grid()
        
        self.bind("<Button-1>", self.on_click)
        
    def mainloop(self):
        super().mainloop()
        self.draw_grid()

    def draw_grid(self):
        for i in range(SIZE):
            start_x = self.width/SIZE * i
            start_y = self.height/SIZE * i
            #Vertical
            self.create_line(start_x, 0, start_x, self.height)
            #Horizontal
            self.create_line(0,start_y, self.width, start_y)


    def on_click(self, event):
        print ("clicked at", event.x, event.y)
        row = int(event.y / HEIGHT * SIZE)
        col = int(event.x / WIDTH * SIZE) 
        print("row ", row)
        print("col ", col)
