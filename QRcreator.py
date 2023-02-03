from tkinter import filedialog
from tkinter import *
import qrcode
from pyzbar import pyzbar
from PIL import Image, ImageTk

users={"Administrator":"Qts21!^7dhc*^@hvbaj", "Saller":"XJjsajxkKUsu1*&hs"}
admins =["Administrator"]

class QRGenerator():
    def __init__(self):
        self.imgs=""
        black="Black"
        white="White"

        window = Tk()
        window.title("QRgenerator")
        window.configure(bg=black)
        Label(window, text="Введіть вміст QR-code:", font="TimesNewRoman 26", bg=black, fg=white).pack()
        self.text= Text(window, height=8, width=40, wrap=WORD, state="normal")
        self.text.pack()
        Button(window, bg=white, fg=black, text="Створити", command=lambda: self.qrgenerator(btn='')).pack(side="left")
        self.save_btn = Button(window, text="Зберегти",command=lambda : self.qrgenerator(btn="save"), state="disabled")
        self.save_btn.pack(side="right")
        self.photo = Label(window, image=self.imgs, bg=black, fg=white)
        self.photo.pack()
        Button(window, text="Decode", command=self.decoder).pack(side="bottom")

        window.mainloop()

    def qrgenerator(self, btn):
        text = self.text.get(1.0, END)
        img = qrcode.make(data=text)
        img.save("QR.png")
        self.img_obj = Image.open("QR.png").resize((200,200))
        self.imgs = ImageTk.PhotoImage(self.img_obj)
        self.photo["image"]=self.imgs
        self.save_btn["state"]="normal"
        if btn == "save":
            try:
                img.save(stream=filedialog.asksaveasfilename(filetypes=(("Files", ".*"), ("QRformat", ".png"))))
            except Exception: pass

    def decoder(self):
        ftype = (("Files", ".*"), ("Images", (".jpg", ".png", ".txt")))
        file = filedialog.askopenfilename(title="QR-code",filetypes=ftype)
        text = pyzbar.decode(Image.open(file))
        self.text.delete(1.0, END)
        print(text)
        try:
            self.text.insert(INSERT, text[0].data.decode("utf-8"))
        except Exception as e:
            self.text.insert(INSERT, "{}".format(e))
QRGenerator()