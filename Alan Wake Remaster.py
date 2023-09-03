import pyMeow as pm
from customtkinter import *
from time import sleep
import threading
import keyboard as kb


class Trainer:
    def __init__(self):
        
        self.root = CTk()
        self.root.title("Alan Wake Remaster Trainer")
        set_appearance_mode("dark")
        self.root.geometry("400x600")
        self.root.resizable(0,0)
    
        self.mf = CTkFrame(master=self.root)
        self.mf.pack(fill="both", expand= True)
    
        self.bc_var = IntVar()
        self.ammo_var = IntVar()
        self.health_var = IntVar()
        
        self.battery_checkbox = CTkCheckBox(master=self.mf,text="Unlimited Batteries",variable=self.bc_var,command=self.check)
        self.battery_checkbox.pack()
        self.battery_checkbox.place(x=140,y=50)
        
        self.ammo_checkbox = CTkCheckBox(master=self.mf, text="Unlimited Ammo", variable=self.ammo_var,command=self.check)
        self.ammo_checkbox.pack()
        self.ammo_checkbox.place(x=140,y=80)
        
        self.health_checkbox = CTkCheckBox(master=self.mf, text="Unlimited health", variable=self.health_var,command=self.check)

        self.keep_running_bat = True
        self.keep_running_ammo = True
        self.keep_running_health = True
        
        kb.add_hotkey('num_1',self.bck)
        kb.add_hotkey('num_2',self.amk)
        kb.add_hotkey("num_3",self.hlk)
    
    def bck(self):
        self.bc_var.set(not self.bc_var.get())
        self.check()
        
    def amk(self):
        self.ammo_var.set(not self.ammo_var.get())
        self.check()
    
    def hlk(self):
        self.health_var.set(not self.health_var.get())
        
    def check(self):
        if self.bc_var.get() == 1:
            self.keep_running_bat = True
            t = threading.Thread(target=self.write_bat)
            t.start()
            
        elif self.bc_var.get() == 0:
            self.keep_running_bat = False
            
        if self.ammo_var.get() == 1:
            self.keep_running_ammo = True
            t1 = threading.Thread(target=self.write_ammo)
            t1.start()
            
        elif self.ammo_var.get() == 0:
            self.keep_running_ammo = False
            
        if self.health_var.get == 1:
            self.keep_running_health = True
            t2 = threading.Thread(target=self.write_health)
            t2.start

    def write_bat(self):
        while self.keep_running_bat:
            sleep(0.3)
            pm.w_int(mem, pm.pointer_chain(mem, module + 0x00AE69D0, offsets_bat), 20)
        
    def write_ammo(self):
        while self.keep_running_ammo:
            sleep(0.3)
            pm.w_int(mem, pm.pointer_chain(mem, module + 0x00AE8EB0, offsets_rev), 42)
            pm.w_int(mem, pm.pointer_chain(mem, module + 0x00D0B220, offsets_hr), 15)
            pm.w_int(mem, pm.pointer_chain(mem, module + 0x00AE69D0, offsets_sg), 30)
#           pm.w_int(mem, pm.pointer_chain(mem,module + 0x00B996D0, offsets_flg), 15)
    def write_health(self):
        pass
    def run(self):
        self.root.mainloop()

 

mem = pm.open_process("Game_f_x64_EOS.exe")
module = pm.get_module(mem, "Game_f_x64_EOS.exe")['base']
offsets_bat = [0x50,0x128,0x10,0x48,0xD0,0x144]
offsets_rev = [0x128,0x10,0x48,0xC0,0x148]
offsets_hr = [0x108,0x10,0x48,0xC0,0x154]
offsets_sg = [0x50,0x130,0x8,0x50,0xC0,0x150]
offsets_flg = [0x860,0x30,0x10,0x130,0x10,0xE0,0x14C]
offsets_hl = None
app = Trainer()
app.run()