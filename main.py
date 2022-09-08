import tkinter
from tkinter import filedialog
from PIL import ImageTk
from tkinter import *
from PIL import Image

window = tkinter.Tk()
window.title("David's Image Watermarker")
window.config(padx=50, pady=10, bg='#ADD8E6', width=600, height=400)

# Choose photo to watermark, adds to window
upload = filedialog.askopenfilename(initialdir='/', title="Select an Image",
                                    filetypes=(('png files', '*.png'), ('jpeg files', '*.jpeg')))
photo = ImageTk.PhotoImage(Image.open(upload))
h = photo.height()
w = photo.width()
canvas = Canvas(window, bg='#ADD8E6', width=w, height=h, highlightthickness=0)
canvas.create_image((h / 2), (w / 2), anchor=CENTER, image=photo)
canvas.pack()

# Parameters allow for changes in text position,
# font size and font. These all need to be added as buttons which can then be added as variables. Find a list of all
# the OpenType/Truetype fonts, include them and have them as a drop down box which can then be added to the
# parameters of the text entry

# Function, input and button to add text to include in the watermark

watermark = canvas.create_text(w / 2, h / 2, text='Your Watermark', font=('OpenSans-Regular.ttf', 30))
canvas.pack()

# Image sizes to help configure positions
height_info = tkinter.Label(window, text=f'Image Height (Y): {h}px', bg='#ADD8E6')
width_info = tkinter.Label(window, text=f'Image Width (X): {w}px', bg='#ADD8E6')
height_info.pack()
width_info.pack()


def update_watermark():
    global watermark
    text = text_entry.get()
    color = color_chosen.get()
    size = size_chosen.get()
    x_axis = x_input.get()
    y_axis = y_input.get()
    canvas.itemconfig(watermark, text=text, font=('OpenSans-Regular.ttf', size), fill=color)
    canvas.pack()


text_label = tkinter.Label(window, text='Enter Text here.', bg='#ADD8E6')
text_label.pack()
text_entry = tkinter.Entry(window)
text_entry.pack()

text_entry_button = tkinter.Button(text='Create Watermark', command=update_watermark)
text_entry_button.pack()

# Change color of text
color_chosen = StringVar()
color_chosen.set('Black')
color_drop = OptionMenu(window, color_chosen, "Blue", "Black", "Yellow", "Green", "Red")
color_drop.pack()

# Change size of text
size_list = []
for size in range(2, 51)[::2]:
    size_list.append(size)

size_chosen = IntVar()
size_chosen.set(24)
size_drop = OptionMenu(window, size_chosen, *size_list)
size_drop.pack()


x_label = tkinter.Label(window, text=f'X Axis Placement. Image Size: {w}px', bg='#ADD8E6')
x_label.pack()
x_chosen = IntVar()
x_chosen.set(w/2)
x_input = tkinter.Entry(window)
x_input.pack()

y_label = tkinter.Label(window, text=f'Y Axis Placement. Image Size: {h}px', bg='#ADD8E6')
y_label.pack()
y_chosen = IntVar()
y_chosen.set(h/2)
y_input = tkinter.Entry(window)
y_input.pack()

window.mainloop()
