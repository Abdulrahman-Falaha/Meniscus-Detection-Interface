import tkinter as tk
from tkinter import messagebox, colorchooser, Image, Frame, Label, PhotoImage, filedialog
from PIL import ImageTk, Image
from ultralytics import YOLO
import os

 ##  Basic Configuration & Design  ##
model = YOLO("yolov8best.pt")

app = tk.Tk()
selected_image = None
selected_image_name = None

app.title("Windows Application")
app.configure(background="black")
app.geometry("1150x700")


##   Texts    ## 

text2 = Label(app, text="Result here")
text2.config(background="Orange")
text2.place(anchor='center', relx=0.5, rely=0.5 )


text1 = Label(app, text="Label One  ")
text1.config(background='yellow')
text1.place(anchor='center', relx=0.5, rely=0.2 )


frame1 = Frame(app, width=450, height=300)
frame1.place(anchor='center', relx=0.22, rely=0.4)
frame1.config(background="light grey")

frame2 = Frame(app, width=450, height=300)
frame2.place(anchor='center', relx=0.78, rely=0.4)
frame2.config(background="light grey")

##   Funcitons ##

def on_button_click():
     global selected_image, frame2, text2
     global frame2
     
     if selected_image is None:
          return
     
     for item in frame2.winfo_children():
          item.destroy()    
     
     loading_label = Label(frame2, text="Loading...", font=("Arial", 20), bg="light grey")
     loading_label.pack()
     app.update_idletasks()
     
     results = model.predict(source=selected_image, save=True, save_crop=True, project="meniscus_predictions") # save plotted images
     
     loading_label.destroy()
    
     if not os.path.isdir(os.getcwd() + "/meniscus_predictions/predict/crops/"):          
          text2.config(background='Red', text="No Meniscus Detected!")
          frame2.config(background="light grey")
          return
          
     for item in frame1.winfo_children():
          item.destroy()

     meniscus_pic = os.getcwd() + "/meniscus_predictions/predict/crops/meniscus/" + selected_image_name  
     img2 = Image.open(meniscus_pic)
     photo2 = ImageTk.PhotoImage(img2.resize((450, 300), Image.Resampling.LANCZOS) )

     label2 = Label(frame2, image = photo2, bg = "Dark Green")
     label2.image = photo2 # type: ignore
     label2.pack()
     
     modified_pic = os.getcwd() + "/meniscus_predictions/predict/" + selected_image_name  
     img = Image.open(modified_pic)
     photo = ImageTk.PhotoImage(img.resize((450, 300), Image.Resampling.LANCZOS) )

     label = Label(frame1, image = photo, bg = "Dark Green")
     label.image = photo # type: ignore
     
     text2.config(background='Green', text="Meniscus Detected!")
     
     label.pack()
     

def insert_picture():
     global selected_image, selected_image_name
     
     formats = [("Image files",'*.jpg'), ("Image files", "*.png"), ("Image files", "*.jpeg")]
     try:
          path=filedialog.askopenfilename(filetypes=formats) 
          selected_image_name = os.path.basename(path)
          
          if path != '':
               delete_directory('meniscus_predictions')
               for item in frame1.winfo_children():
                    item.destroy()
          selected_image = Image.open(path)
          image_for_display = ImageTk.PhotoImage(selected_image.resize((450, 300), Image.Resampling.LANCZOS) )
          
          # dimensions = "image size: %dx%d" % (image_for_display.width(), image_for_display.height())
          # print(dimensions)
          
          label = Label(frame1, image = image_for_display, bg = "Dark Green")
          label.image = image_for_display # type: ignore
          label.pack()

     except AttributeError as err:
          print(err)


def remove_picture():
     for item in frame1.winfo_children():
          item.destroy()
     for item in frame2.winfo_children():
          item.destroy()


def on_exit():
     print("Exiting the application...")
     delete_directory('meniscus_predictions')
     app.destroy()
     

def delete_directory(directory_path):
    try:
        # First, delete all the files and subdirectories inside the directory
        for root, dirs, files in os.walk(directory_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)

        # Now, the directory should be empty, and you can remove it
        os.rmdir(directory_path)
        print(f"Directory '{directory_path}' successfully deleted.")
    except Exception as e:
        print(f"Error deleting directory: {str(e)}")

# Replace 'your_directory_path' with the actual path of the directory you want to delete


##   Buttons    ## 
    
button_add_pic = tk.Button(app, width=12, height=2, text="Select picture", command=insert_picture)
button_add_pic.place(anchor='center', relx=0.32, rely=0.75)

button_remove_pic = tk.Button(app, width=12, height=2, text="Remove picture", command=remove_picture)
button_remove_pic.place(anchor='center', relx=0.12, rely=0.75)

button_exec = tk.Button(app, width=15, height=4, text="Execute", command=on_button_click)
button_exec.place(anchor='se', relx=0.97, rely=0.95)



app.protocol("WM_DELETE_WINDOW", on_exit)

app.mainloop()
