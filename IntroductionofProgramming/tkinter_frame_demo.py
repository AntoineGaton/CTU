import tkinter as tk
import math
from tkinter import Canvas, Frame, BOTH

# class HistogramViewer(tk.Frame):
#    def __init__(self, master=None):
#        super().__init__(master)
#        self.master = master
#        self.master.title('Histogram Viewer')
#        self.pack(fill=BOTH, expand=1)

#        canvas = Canvas(self)
#        canvas.create_rectangle(10, 10, 210, 60, outline='black', fill='blue')
#        canvas.create_oval(10, 75, 160, 125, outline='cyan', fill='cyan')
#        canvas.create_polygon(10, 200, 110, 130, 160, 180, 10, 180, outline='red', fill='red')

#        canvas.pack(fill=BOTH, expand=1)
#        self.pack()

# app_frame = tk.Tk()
# app_frame.geometry('400x250')
# histogram_viewer = HistogramViewer(master=app_frame)
# histogram_viewer.mainloop()
#############################################################################################################
# def draw_star(canvas, x, y, outer_radius, inner_radius, color):
#     points = []
#     angle = math.pi / 2  # Starting angle

#     # Calculate the coordinates of the star's points
#     for _ in range(5):
#         outer_x = x + outer_radius * math.cos(angle)
#         outer_y = y - outer_radius * math.sin(angle)  # Negative sin to account for the coordinate system
#         points.append((outer_x, outer_y))

#         inner_x = x + inner_radius * math.cos(angle + math.pi / 5)
#         inner_y = y - inner_radius * math.sin(angle + math.pi / 5)
#         points.append((inner_x, inner_y))

#         angle += 2 * math.pi / 5

#     # Draw the star on the canvas
#     canvas.create_polygon(points, fill=color)

# # Create a Tkinter window
# window = tk.Tk()

# # Create a Canvas widget
# canvas = tk.Canvas(window, width=400, height=400)
# canvas.pack()

# # Draw a star on the canvas
# draw_star(canvas, 200, 200, 100, 50, 'yellow')

# # Start the Tkinter event loop
# window.mainloop()
#############################################################################################################
import tkinter as tk

def draw_happy_face(canvas, x, y, radius):
    # Draw the head
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='black', fill='yellow')

    # Calculate the coordinates of the eyes
    eye_radius = radius / 10
    left_eye_x = x - radius / 3
    right_eye_x = x + radius / 3
    eye_y = y - radius / 6

    # Draw the eyes
    canvas.create_oval(left_eye_x - eye_radius, eye_y - eye_radius, left_eye_x + eye_radius, eye_y + eye_radius, outline='black', fill='black')
    canvas.create_oval(right_eye_x - eye_radius, eye_y - eye_radius, right_eye_x + eye_radius, eye_y + eye_radius, outline='black', fill='black')

    # Calculate the coordinates of the mouth
    mouth_width = radius / 2
    mouth_height = radius / 3
    mouth_x = x - mouth_width / 2
    mouth_y = y + radius / 5

    # Draw the mouth
    canvas.create_arc(mouth_x, mouth_y, mouth_x + mouth_width, mouth_y + mouth_height, start=200, extent=140, style='arc', outline='black', width=2)

# Create a Tkinter window
window = tk.Tk()

# Create a Canvas widget
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Draw a happy face on the canvas
draw_happy_face(canvas, 200, 200, 100)

# Start the Tkinter event loop
window.mainloop()