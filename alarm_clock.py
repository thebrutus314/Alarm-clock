#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import strftime 
from time import sleep
import os

print("Alarm clock")
print("Codet by @thebrutus314")

try:
    # Tkinter for Python 2.xx
    import Tkinter as tk
except ImportError:
    # Tkinter for Python 3.xx
    import tkinter as tk

APP_TITLE = "Alarm clock in Python by thebrutus314"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200

LABEL_01_FONT = ('Helevtica', 14, 'bold')
LABEL_BG = 'light blue'
LABEL_ALARM_BG = 'red'

class Application(tk.Frame):

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)

        self.act_time_var = tk.StringVar()
        tk.Label(self, textvariable=self.act_time_var, font=LABEL_01_FONT,
            fg='green').pack()

        label_frame = tk.Frame(self, bg=LABEL_BG, padx=2, pady=2)
        label_frame.pack(pady=4)
        
        self.label_01 = tk.Label(label_frame, text='Enter time:',
            font=LABEL_01_FONT, bg=LABEL_BG)
        self.label_01.pack()
        
        self.label_02 = tk.Label(label_frame, text='ss:mm(:ss)', bg=LABEL_BG)
        self.label_02.pack()
        
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=4)
        
        self.entry_std = tk.Entry(entry_frame, width=2)
        self.entry_std.pack(side='left')
        
        self.entry_min = tk.Entry(entry_frame, width=2)
        self.entry_min.pack(side='left')

        self.entry_sec = tk.Entry(entry_frame, width=2)
        self.entry_sec.pack(side='left')
 
        self.alarm_set_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(self, text='On', onvalue=1, offvalue=0,
            variable=self.alarm_set_var)
        self.checkbox.pack(expand=True)
        
        self.alarm_flag = False
        self.label_frame = label_frame
        
        self.update_time()
        
    def update_time(self):
        act_time = strftime('%H:%M:%S')
        self.act_time_var.set(act_time)
        alarm_time = "{}:{}:{}".format(
            self.entry_std.get(),
            self.entry_min.get(),
            self.entry_sec.get())
                    
        if self.alarm_set_var.get():
            if alarm_time == act_time:
                self.alarm_display(True)
                
        else:
            if self.alarm_flag:
                self.alarm_display(False)
                     
        self.after(100, self.update_time)

    def alarm_display(self, alarm=False):
        self.alarm_flag = alarm
        if alarm:
                self.label_frame['bg'] = LABEL_ALARM_BG
                self.label_01['bg'] = LABEL_ALARM_BG
                self.label_02['bg'] = LABEL_ALARM_BG
                for i in range(10):
                    os.system("echo -ne '\007'")
            
        else:
            self.label_frame['bg'] = LABEL_BG
            self.label_01['bg'] = LABEL_BG
            self.label_02['bg'] = LABEL_BG

        
def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
    
    app = Application(app_win).pack(expand=True)
    
    app_win.mainloop()
 
 
if __name__ == '__main__':
    main()      
