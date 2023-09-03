import pyMeow as pm
from customtkinter import *
import keyboard as kb

class Main:
    def __init__(self):
        self.root = CTk()
        self.root.title("Alto Coins")
        self.root.geometry("230x100")
        set_appearance_mode("Dark")
        self.root.resizable(0,0)
        
        self.add_coins = CTkButton(master=self.root,text="Add Coins",command=self.coins)
        self.add_coins.pack()
        self.add_coins.place(x=47,y=34)
        
    def coins(self):
        pm.w_int(game,pm.pointer_chain_64(game,module + 0x00492DA8,offsets),1000000)
        
    def run(self):
        self.root.mainloop()

game = pm.open_process("The Alto Collection.exe")
module = pm.get_module(game,"mono-2.0-bdwgc.dll")['base']
offsets = [0xA8,0x568,0x20,0x80,0x10]

app = Main()
app.run()