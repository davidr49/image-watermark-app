import tkinter
from tkinter import filedialog
from PIL import ImageTk, ImageGrab
from tkinter import *
from PIL import Image

window = tkinter.Tk()
window.title("Image Watermarker")
window.config(padx=50, pady=10, bg='#ADD8E6', width=500, height=500)

# Choose photo to watermark, adds to window
upload = filedialog.askopenfilename(initialdir='/', title="Select an Image",
                                    filetypes=(('png files', '*.png'), ('jpeg files', '*.jpeg')))
photo = ImageTk.PhotoImage(Image.open(upload))
h = photo.height()
w = photo.width()
canvas = Canvas(window, width=w, height=h, highlightthickness=0)
canvas.create_image((w / 2), (h / 2), image=photo, anchor=CENTER)
watermark = canvas.create_text(w / 2, h / 2, text='Your Watermark', font=('Calibri Light', 30))

canvas.grid(column=1, row =0, rowspan=8, padx=(30,0), columnspan=3)


def update_watermark():
    global watermark
    text = text_entry.get()
    color = color_chosen.get()
    size = size_chosen.get()
    x_axis = x_input.get()
    y_axis = y_input.get()
    font = font_chosen.get()
    watermark = canvas.create_text(x_axis, y_axis, text=text, font=(font, size), fill=color)
    canvas.grid(column=1, row=0, rowspan=8, padx=(30,0), columnspan=3)


def delete_watermark():
    global watermark
    canvas.delete(watermark)


def save_image():
    global photo
    photo_name = str(photo)
    x1 = window.winfo_rootx() + canvas.winfo_x()
    y1 = window.winfo_rooty() + canvas.winfo_y()
    x2 = x1 + canvas.winfo_width()
    y2 = y1 + canvas.winfo_height()
    final_name = photo_name + '_watermark.jpg'
    file_location = filedialog.askdirectory(title="Save as...")
    saving_photo = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    saving_photo.save(f"{file_location}/{final_name}")


#Button and input to change watermark text
default_text = StringVar()
default_text.set('Your Watermark')
text_entry = tkinter.Entry(window, textvariable=default_text)
text_entry.grid(column=0, row=0)

text_entry_button = tkinter.Button(text='Create Watermark', command=update_watermark)
text_entry_button.grid(column=2, row=8, padx=(30,0))

delete_watermark_button = tkinter.Button(text='Delete Prev', command=delete_watermark)
delete_watermark_button.grid(column=3, row=8, padx=(30,0))

# Change color of text
color_chosen = StringVar()
color_chosen.set('Black')
color_drop = OptionMenu(window, color_chosen, "Blue", "Black", "Yellow", "Green", "Red")
color_drop.grid(column=0, row=1)

# Change size of text
size_list = []
for size in range(2, 51)[::2]:
    size_list.append(size)

size_chosen = IntVar()
size_chosen.set(24)
size_drop = OptionMenu(window, size_chosen, *size_list)
size_drop.grid(column=0, row=2)


#change location of watermark x and y
x_label = tkinter.Label(window, text=f'X Axis. Image Size: {w}px', bg='#ADD8E6')
x_label.grid(column=0, row=4)
x_chosen = IntVar()
x_chosen.set(round(w / 2))
x_input = tkinter.Entry(window, textvariable=x_chosen)
x_input.grid(column=0, row=5)

y_label = tkinter.Label(window, text=f'Y Axis. Image Size: {h}px', bg='#ADD8E6')
y_label.grid(column=0, row=6)
y_chosen = IntVar()
y_chosen.set(round(h / 2))
y_input = tkinter.Entry(window, textvariable=y_chosen)
y_input.grid(column=0, row=7)


#change font of watermark
font_list = ['Calibri Light', 'Times New Roman', 'Courier New', 'Arial', 'Courier', 'MS Serif']
font_chosen = StringVar()
font_chosen.set('Calibri Light')
font_drop = OptionMenu(window, font_chosen, *font_list)
font_drop.grid(column=0, row=3)

#save button
save_button = Button(text='Save As', command=save_image)
save_button.grid(column=1, row=8, pady=(20,20), padx=(30,0))


window.mainloop()
