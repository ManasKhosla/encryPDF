import tkinter as tk
import tkinter.font as tkFont
from tkinter import Label, PhotoImage, filedialog,messagebox
from PIL import ImageTk,Image
from module import encryptPdf

class App:
    #setting vars
    # ownPass,userPass = StringVar(),StringVar()
    filepath=""

    def __init__(self, root):
        global selectedFileLbl
        #setting title
        root.title("EncryPDF")
        #setting window size
        width=400
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # canvas = Canvas(root, width=400, height=60) 
        img = ImageTk.PhotoImage(Image.open("assets/banner.png"))  
        # canvas.create_image(0, 0, image=img)

        # img = ImageTk.PhotoImage(file="banner.png")
        banner = Label(image=img)
        banner.image = img
        banner.place(width=400, height=60)

        selectPdfBtn=tk.Button(root)
        selectPdfBtn["bg"] = "#e9e9ed"
        selectPdfBtn["cursor"] = "pirate"
        ft = tkFont.Font(family='calibre',size=10)
        selectPdfBtn["font"] = ft
        selectPdfBtn["fg"] = "#000000"
        selectPdfBtn["justify"] = "center"
        selectPdfBtn["text"] = "Select PDF"
        selectPdfBtn["relief"] = "groove"
        selectPdfBtn.place(x=80,y=90,width=244,height=35)
        selectPdfBtn["command"] = self.selectPdfBtn_command

        encryptBtn=tk.Button(root)
        encryptBtn["bg"] = "#e9e9ed"
        encryptBtn["cursor"] = "exchange"
        ft = tkFont.Font(family='calibre',size=10)
        encryptBtn["font"] = ft
        encryptBtn["fg"] = "#000000"
        encryptBtn["justify"] = "center"
        encryptBtn["text"] = "Encrypt"
        encryptBtn["relief"] = "groove"
        encryptBtn.place(x=150,y=310,width=111,height=36)
        encryptBtn["command"] = self.encryptBtn_command

        self.ownPassInp=tk.Entry(root)
        self.ownPassInp["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibre',size=10)
        self.ownPassInp["font"] = ft
        self.ownPassInp["fg"] = "#333333"
        self.ownPassInp["justify"] = "center"
        self.ownPassInp["text"] = "Owner Password"
        self.ownPassInp.place(x=170,y=200,width=200,height=30)

        self.userPassInp=tk.Entry(root)
        self.userPassInp["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibre',size=10)
        self.userPassInp["font"] = ft
        self.userPassInp["fg"] = "#333333"
        self.userPassInp["justify"] = "center"
        self.userPassInp["text"] = "User Password"
        self.userPassInp.place(x=170,y=250,width=200,height=30)

        selectedFileLbl=tk.Label(root)
        ft = tkFont.Font(family='calibre',size=10)
        selectedFileLbl["font"] = ft
        selectedFileLbl["fg"] = "#333333"
        selectedFileLbl["justify"] = "center"
        selectedFileLbl["text"] = "Selected file name will show here"
        selectedFileLbl.place(x=50,y=140,width=300,height=30)

        ownPassLbl=tk.Label(root)
        ft = tkFont.Font(family='calibre',size=10)
        ownPassLbl["font"] = ft
        ownPassLbl["fg"] = "#333333"
        ownPassLbl["justify"] = "center"
        ownPassLbl["text"] = "Owner password"
        ownPassLbl.place(x=30,y=200,width=114,height=31)

        userPassLbl=tk.Label(root)
        ft = tkFont.Font(family='calibre',size=10)
        userPassLbl["font"] = ft
        userPassLbl["fg"] = "#333333"
        userPassLbl["justify"] = "center"
        userPassLbl["text"] = "User password"
        userPassLbl.place(x=30,y=250,width=114,height=30)


    def selectPdfBtn_command(self):
        global selectedFileLbl
        try:
            inpFile = filedialog.askopenfile(filetypes=[('PDF Files', '*.pdf')])
            self.filepath = inpFile.name
            selectedFileLbl["text"] = self.filepath
        except AttributeError:
            pass
        except Exception as e:
            messagebox.showerror("Error", "Error: "+str(e))


    def encryptBtn_command(self):
        if self.filepath == "":
            messagebox.showerror("File Error", "File not selected. Please select a file!")
        else:
            ownPass,userPass = self.ownPassInp.get(), self.userPassInp.get()
            statusCode = encryptPdf(self.filepath,ownPass,userPass)
            if statusCode[0] == 0:
                messagebox.showinfo("Status", "Encryption was successful!\n\nFile saved at: "+statusCode[1])
            else:
                messagebox.showerror("Status", "Encryption was unsuccessful!")


if __name__ == "__main__":
    root = tk.Tk()
    icon = PhotoImage(file="assets/ico.png")
    root.iconphoto(True,icon)
    app = App(root)
    root.mainloop()
