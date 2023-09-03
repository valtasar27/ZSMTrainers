from customtkinter import *
from time import sleep
import threading,keyboard
import pyMeow as pm

class Tr:
    def __init__(self):
        self.root = CTk()
        self.root.title("HFR Trainer")
        self.root.geometry("500x800")
        self.root.resizable(0,0)
        set_appearance_mode("Dark")
        
        self.welcome = CTkLabel(master=self.root,text="Hi Fi RUSH trainer by ZSM",font=("Century Gothic",20))
        self.welcome.pack()
        self.welcome.place(x=20,y=34)
        
        self.scrap_var = IntVar()
        self.none_var = IntVar()
        
        self.scrap_en = CTkEntry(master=self.root,placeholder_text="Ammount")
        self.scrap_en.pack()
        self.scrap_en.place(x=98,y=110)
        
        self.scrap_bt = CTkButton(master=self.root,text="Set Scrap Ammount",command=self.write_scrap)
        self.scrap_bt.pack()
        self.scrap_bt.place(x=250,y=110)
        
    def check(self):
        None
        
    def write_scrap(self):
        a = self.scrap_en.get()
        pm.w_int(game,pm.pointer_chain_64(game,module + 0x071ECE48,offsets),int(a))
        
    def run(self):
        self.root.mainloop()


game = pm.open_process("Hi-Fi-RUSH.exe") #proc is 64-bits
module = pm.get_module(game,"Hi-Fi-RUSH.exe")['base']
offsets = [0x190,0x2B8,0x418]

app = Tr()
app.run()