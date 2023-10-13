import tkinter as tk
from tkinter import Canvas, Frame, BOTH

class HistogramViewer(tk.Frame):
   def __init__(self, master=None):
       super().__init__(master)
       self.master = master
       self.master.title('Histogram Viewer')
       self.pack(fill=BOTH, expand=1)

       canvas = Canvas(self)
       canvas.create_rectangle(10, 10, 210, 60, outline='darkolivegreen4', fill='darkolivegreen4')
       canvas.create_rectangle(10, 75, 160, 125, outline='cyan', fill='cyan')
       canvas.create_rectangle(10, 140, 360, 190, outline='gray40', fill='gray40')

       canvas.pack(fill=BOTH, expand=1)
       self.pack()

app_frame = tk.Tk()
app_frame.geometry('400x250')
histogram_viewer = HistogramViewer(master=app_frame)
histogram_viewer.mainloop()