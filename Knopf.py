import tkinter as tk
from MainLog import cpu, ram, ssd
from SystemInfo import systemwerte
from time import sleep

program_run = True

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quit = tk.Button(self, text="Fenster Schließen", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.log = tk.Button(self, text="Log CPU", fg="black", command=self.logging)
        self.log.pack(side="top")

        self.system_info = tk.Button(self, text="Systeminformationen", fg="black", command=self.systeminfo)
        self.system_info.pack(side="top")

        self.hilfe = tk.Button(self, text="Hilfe?", fg="blue", command=self.help)
        self.hilfe.pack(side="bottom")

    def logging(self):
        global program_run
        while program_run:
            cpu()
            ram()
            ssd()

    def systeminfo(self):
        systemwerte()

    def help(self):
        print("Wenden sie sich an Ihren Systemadministrator für Hilfe!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
