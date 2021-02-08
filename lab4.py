import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()

frame = tkinter.Frame(root)
frame.grid()
image = Image.open('_сarib_TC.bmp') #_Carib16.bmp  _Carib256.bmp _сarib_TC.bmp
width = image.size[0]
height = image.size[1]
canvas = tkinter.Canvas(root, height = height, width = width)
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(row = 1, column = 1)
root.mainloop()