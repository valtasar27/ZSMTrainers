from customtkinter import *
import pyMeow as pm
import threading,keyboard,time
from PIL import Image

class Tr:
    def __init__(self):
        
        self.root = CTk()
        self.root.title("COFT")
        set_appearance_mode("Dark")
        self.root.geometry("500x310")
        
        self.title = CTkLabel(master=self.root,
                              text="Cry Of Fear Trainer",
                              font=("Century Gothic",20))
        self.title.pack()
        self.title.place(x=20,y=30)
        
        self.health_var = IntVar()
        
        self.health_cheat = CTkSwitch(master=self.root,text="Unlimited Health",variable=self.health_var,command=self.check)
        self.health_cheat.pack()
        self.health_cheat.place(x=25,y=70)
        
        self.cover_art = CTkImage(dark_image=Image.open("C:\\Users\\Nicolas\\Desktop\\COF cover art.png"),size=(212,300))
        self.cover_art_lable = CTkLabel(master=self.root,text="",image=self.cover_art)
        self.cover_art_lable.pack()
        self.cover_art_lable.place(x=250,y=7)
        
        self.kr_health = True
        
        keyboard.add_hotkey("h",self.health_shortcut)
        
    def health_shortcut(self):
        self.health_var.set(not self.health_var.get())
        self.check()
        
    def check(self):
        if self.health_var.get() == 1:
            self.kr_health = True
            t = threading.Thread(target=self.health_write)
            t.daemon = True
            t.start()
        
        elif self.health_var.get() == 0:
            self.kr_health = False
            
    def health_write(self):
        while self.kr_health:
            pm.w_float(game,pm.pointer_chain_32(game,addr + 0x002119A8,offsets_health),100)
            time.sleep(0.8)
        

    def run(self):
        self.root.mainloop()
        
        
game = pm.open_process("cof.exe")
module = pm.get_module(game, "hl.dll")
addr = module['base']

offsets_health = [0x4,0x164]

#health = pm.pointer_chain_32(game,addr + 0x002119A8,offsets_health)

app = Tr()
app.run()