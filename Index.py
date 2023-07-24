import tkinter as tk
from tkinter import messagebox, colorchooser, Image, Frame, Label, PhotoImage, filedialog
from PIL import ImageTk, Image

 ##  Basic Configuration & Design  ##

app = tk.Tk()


app.title("Windows Application")
app.configure(background="black")
app.geometry("1150x700")


frame1 = Frame(app, width=450, height=300, highlightbackground='blue', highlightthickness=2)
frame1.place(anchor='center', relx=0.22, rely=0.4)
frame1.config(background="light grey")

frame2 = Frame(app, width=450, height=300)
frame2.place(anchor='center', relx=0.78, rely=0.4)
frame2.config(background="light grey")

##   Funcitons ##

def on_button_click():
     messagebox.showinfo("Message", "Button clicked!")
     
     # AI code starts here... 
     modified_pic = ""               
     for item in frame1.winfo_children():
          item.destroy()
     img = Image.open(modified_pic)
     photo = ImageTk.PhotoImage(img.resize((450, 300), Image.Resampling.LANCZOS) )
     dimensions = "image size: %dx%d" % (photo.width(), photo.height())
     print(dimensions)
     label = Label(frame2, image = photo, bg = "Dark Green")
     label.image = photo # type: ignore
     label.pack()


def insert_picture():
     formats = [("Image files",'*.jpg'), ("Image files", "*.png"), ("Image files", "*.jpeg")]
     try:
          path=filedialog.askopenfilename(filetypes=formats)               
          if path != '':
               for item in frame1.winfo_children():
                    item.destroy()
          img = Image.open(path)
          photo = ImageTk.PhotoImage(img.resize((450, 300), Image.Resampling.LANCZOS) )
          
          dimensions = "image size: %dx%d" % (photo.width(), photo.height())
          print(dimensions)
          
          label = Label(frame1, image = photo, bg = "Dark Green")
          label.image = photo # type: ignore
          label.pack()

     except AttributeError as err:
          print(err)


def remove_picture():
     for item in frame1.winfo_children():
          item.destroy()
     for item in frame2.winfo_children():
          item.destroy()


##   Buttons    ## 
    
button_add_pic = tk.Button(app, width=12, height=2, text="Select picture", command=insert_picture)
button_add_pic.place(anchor='center', relx=0.32, rely=0.75)

button_remove_pic = tk.Button(app, width=12, height=2, text="Remove picture", command=remove_picture)
button_remove_pic.place(anchor='center', relx=0.12, rely=0.75)

button_exec = tk.Button(app, width=15, height=4, text="Execute", command=on_button_click)
button_exec.place(anchor='se', relx=0.97, rely=0.95)


##   Texts    ## 

text1 = Label(app, text="Label One  ")
text1.config(background='yellow')
text1.place(anchor='center', relx=0.5, rely=0.2 )

text2 = Label(app, text="Label Two  ")
text2.config(background='Red')
text2.place(anchor='center', relx=0.5, rely=0.5 )


app.mainloop()
