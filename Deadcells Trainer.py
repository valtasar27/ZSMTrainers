import pyMeow as pm
from customtkinter import * 
import threading, keyboard
from time import sleep
from PIL import Image

class OffSets:
    offsets_health = [0x42C,0x0,0x58,0x64,0x10C]
    offsets_pn = [0x648,0x8,0x18,0x64,0x144]
    offsets_money = [0x648,0x8,0x18,0x5C,0x2C]
    offsets_cells = [0x42C,0x0,0x58,0x64,0x360]

class Trainer:
    
    def __init__(self):
        self.root = CTk()
        self.root.title("DCT By ZMS")
        set_appearance_mode("Dark")
        self.root.geometry("600x500")
        self.root.resizable(0,0)

        self.mainframe = CTkFrame(master=self.root)
        self.mainframe.pack(fill="both", expand=True)
        
        self.title = CTkLabel(master=self.mainframe,text="Deadcells Trainer",font=("Century Gothic", 20))
        self.title.pack()
        self.title.place(x=15,y=5)
        
        self.health_var = IntVar()
        self.pn_var= IntVar()
        
        self.health_switch = CTkSwitch(master=self.mainframe,text="Unlimited Health",variable=self.health_var,command=self.check)
        self.health_switch.pack()
        self.health_switch.place(x=40,y=50)
        
        self.pn_switch = CTkSwitch(self.mainframe,text="Max Brutallity (Depricated)",variable=self.pn_var,command=self.check)
        self.pn_switch.pack()
        self.pn_switch.place(x=40,y=78)
        
        self.coins_Button = CTkButton(master=self.mainframe,width=80,text="Set Coins",command=self.write_coins)
        self.coins_Button.pack()
        self.coins_Button.place(x=150,y=110)
        
        self.coins_value = CTkEntry(master=self.mainframe,width=100,placeholder_text="Amount")
        self.coins_value.pack()
        self.coins_value.place(x=40,y=110)
        
        self.cells_Button = CTkButton(master=self.mainframe,width=80,text="Set Cells",command=self.write_cells)
        self.cells_Button.pack()
        self.cells_Button.place(x=150,y=150)
        
        self.cells_value = CTkEntry(master=self.mainframe,width=100,placeholder_text="Amount")
        self.cells_value.pack()
        self.cells_value.place(x=40,y=150)
        
        self.img_d = CTkImage(dark_image=Image.open("C:\\Users\\Nicolas\\Documents\\Dead_cells_cover_art.png"),size=(289,345))
        self.cover_art_l = CTkLabel(master=self.mainframe,image=self.img_d,text="")
        self.cover_art_l.pack()
        self.cover_art_l.place(x=300,y=20)
        
        self.game_lable = CTkLabel(master=self.mainframe,text="Game process name: deadcells.exe",font=("Century Gothic",13))
        self.game_lable.pack()
        self.game_lable.place(x=300,y=365)
        
        self.version = CTkLabel(master=self.mainframe,text="Game Version: v32",font=("Century Gothic",13))
        self.version.pack()
        self.version.place(x=300,y=395)
        
        self.pid = CTkLabel(master=self.mainframe,text="Process ID: " + str(game['pid']),font=("Century Gothic",13))
        self.pid.pack()
        self.pid.place(x=300,y=425)
        
        self.credit = CTkLabel(master=self.mainframe,text="Made By: ZSM",font=("Century Gothic",13))
        self.credit.pack()
        self.credit.place(x=300,y=455)
        
        
        self.keep_running_health = True
        self.keep_running_pn = True
        
        keyboard.add_hotkey("f1",self.health_sc)
        keyboard.add_hotkey("f2",self.pn_sc)
        keyboard.add_hotkey("f3",self.write_coins)
        keyboard.add_hotkey("f4",self.write_cells)
    
    def health_sc(self):
        self.health_var.set(not self.health_var.get())
        self.check()
        
    def pn_sc(self):
        self.pn_var.set(not self.pn_var.get())
        self.check()
    
    def check(self):
        
        if self.health_var.get() == 1:
            self.keep_running_health = True
            t_h = threading.Thread(target=self.write_health)
            t_h.daemon = True
            t_h.start()
        
        elif self.health_var.get() == 0:
            self.keep_running_health = False
            
        if self.pn_var.get() == 1:
            self.keep_running_pn = True
            t_pn = threading.Thread(target=self.write_pn)
            t_pn.daemon = True
            t_pn.start()
            
        elif self.pn_var.get() == 0:
            self.keep_running_pn = False
        

    def write_health(self):
        while self.keep_running_health:
            pm.w_int(game, pm.pointer_chain_32(game, module + 0x00048184, OffSets.offsets_health),999999)
            sleep(0.3)
            
    def write_pn(self):
        while self.keep_running_pn:
            sleep(0.2)
            if pm.key_pressed(0x01) == True:
                pm.w_int(game, pm.pointer_chain_32(game, module + 0x00048184, OffSets.offsets_pn),50)
                sleep(1)
                pm.w_int(game, pm.pointer_chain_32(game, module + 0x00048184, OffSets.offsets_pn),1)
             
    def write_coins(self):
        a = self.coins_value.get()
        pm.w_int(game, pm.pointer_chain_32(game, module + 0x00048184, OffSets.offsets_money),int(a))
    
    def write_cells(self):
        b = self.cells_value.get()
        pm.w_int(game, pm.pointer_chain_32(game, module + 0x00048184, OffSets.offsets_cells),int(b))
            
    def run(self):
        self.root.mainloop()
    

game = pm.open_process("deadcells.exe") #32 bits
module = pm.get_module(game, "libhl.dll")['base']

app = Trainer()
app.run()
