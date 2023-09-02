from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import pyshorteners

# creating Tkinter app
app = Tk()
# Giving Size to our GUI window
app.geometry("640x360")
# bg = PhotoImage("1.jpg")

# add background image to window
img = Image.open('Photos/1.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(app, image=bg)
label.place(x=0, y=0)
canvabg = Canvas(app, width=500, height=500)
# canvabg.pack(fill="both", expand=True)
canvabg.create_image(0, 0, image=bg, anchor="nw")
canvabg.create_text(400, 250, text="URL Shortener")

# Function to shorten the given input URL
def shorten_url():
    shortener = pyshorteners.Shortener()
    short_url1 = shortener.tinyurl.short(long_url_entry.get())
    print(short_url_entry.insert(0, short_url1))


# Creating Label
long_url = Label(app, text="Enter long URL: ", font=("TimesNewRoman", '10'))
short_url = Label(app, text="Shorter URL is: ", font=("TimesNewRoman", '10'))

# Placing them in window
long_url.place(relheight=0.2, relwidth=0.2)
short_url.place(relwidth=0.3, relheight=0.3)

# creating grid so entry and label can be side by side
long_url.grid(row=0, column=0, sticky=W, pady=10, padx=5)
short_url.grid(row=1, column=0, sticky=W, pady=10, padx=5)

# Creating Entry  for longURL , ShortURL as Output
long_url_entry = Entry(app, width=40)
short_url_entry = Entry(app, width=40)
long_url_entry.grid(row=0, column=1, pady=20, padx=10)
short_url_entry.grid(row=1, column=1, pady=15, padx=10)
shorten_Button = Button(app, text="Shorten", command=shorten_url)
shorten_Button.place(relx=0.34, rely=0.34, anchor='center')

# To run Tkinter API
app.mainloop()
