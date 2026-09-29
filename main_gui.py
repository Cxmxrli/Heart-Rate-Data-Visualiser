import customtkinter as ctk 
from customtkinter import CTkImage
from PIL import ImageTk, Image

#need to make a variable for the ecg reading images
#need to make window to display the image
#need button to add file path into app
#need to add button to find peaks and stuff

#tkinter window
class ecg_main(ctk.CTk):
    def __init__(self):
        
        super().__init__()
        self.title("---ECG Reader---")
        self.geometry("1500x900")#1000x700
        self.resizable(True,True)


if __name__ == "__main__":
    app = ecg_main()
    app.mainloop()