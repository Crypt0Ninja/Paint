######### Modules Import #########
from tkinter import *
from time import sleep		     
from PIL import Image, ImageTk   
import pyscreenshot as ImageGrab 
##################################

def saver(event,filename,window,box):
	window.destroy()
	sleep(0.5)
	if ".jpg" in filename:
		ImageGrab.grab(bbox = box).save(filename)
	else:
		ImageGrab.grab(bbox = box).save("{}.jpg".format(filename))

def canvas_color_changer():
	global canvas_bg
	global frame
	window = Tk()
	window.title("Canvas Color")
	color_canvas = Entry(window)
	color_canvas.pack()
	color_canvas.bind("<Return>",lambda e: frame.config(bg = color_canvas.get()))
	window.mainloop()
def savefile():
	global frame
	box = (frame.winfo_rootx(),frame.winfo_rooty(),frame.winfo_rootx()+frame.winfo_width(),frame.winfo_rooty() + frame.winfo_height())
	win = Tk()
	win.title("Save")
	Label(win,text = "Write File Name:").pack()
	filename = ""
	ent = Entry(win)
	ent.pack()
	ent.bind("<Return>", lambda e: saver(e,ent.get(),win,box))
	win.mainloop()
root = Tk()

# Window Configuration #

root.title("PAINT")

root.geometry("800x600")

########################

main_panel = Menu(root)

root.config(menu = main_panel)

file = Menu(main_panel)

main_panel.add_cascade(label = "File",menu = file)

main_panel.add_command(label = "Canvas Color",command = canvas_color_changer)

file.add_command(label = "Save",command = savefile)

file.add_separator()

file.add_command(label = "Close",command = root.destroy)

global_width = 1
def callback(event):
	print("Pressed mouse at position: x={};y={}".format(event.x,event.y))
	global frame
	global canvas_color
	x1, y1 = (event.x - int(global_width)), (event.y - int(global_width))
	x2, y2 = (event.x + int(global_width)), (event.y + int(global_width))
	frame.create_oval(x1, y1, x2, y2, fill=canvas_color, outline="")

def change_color(color):
	global canvas_color
	canvas_color = color

def sumbit_function():
	global paint_width
	global global_width

	global_width = paint_width.get()

def clear_canvas():
	global frame
	frame.delete("all")

canvas_color = "white"

canvas_bg = "black"

frame = Canvas(root,width=800,height=400,bg = canvas_bg)
frame.bind("<B1-Motion>", callback)
frame.bind("<Button-1>", callback)
frame.place(x = 0,y = 0)

print(frame)

fr = Frame(root,width = 800,height = 200,bg = "gray19")
fr.place(x = 0,y = 400)
green = Button(fr,text = "Green",width = 10,bg = "green",fg = "white",height = 1,command = lambda: change_color("green"))

green.place(x = 680,y = 150)

white = Button(fr,text = "White",width = 10,bg = "white",fg = "black",height = 1,command = lambda: change_color("white"))

white.place(x = 550,y = 150)

clear = Button(fr,text = "Clear Canvas",command = clear_canvas)

clear.place(x = 420,y = 150)

paint_width = Entry(fr)

paint_width.place(
	x = 0,
	y = 0
)

sumbit_color = Button(fr,text = "Sumbit!",bg = "darkblue",command = sumbit_function)

sumbit_color.place(
	x = 0,
	y = 30
)
root.mainloop()
