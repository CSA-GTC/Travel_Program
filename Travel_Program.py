'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
#Gregory Clarke
#10/22/2018
#Advanced Computer Programming
'''


from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, master=None):
        self.frame = Frame(root)
        self.master = master

        self.items = Listbox(self.frame, height=10, width=25)
        self.items.bind("<<ListboxSelect>>")
        for x in ["Argentina","Australia","Austria","Brazil","Canada","China","Croatia","Cuba","Czech Republic",
                  "Denmark","Egypt","Estonia","Ethiopia","Finland","France","Germany","Great Britain",
                  "Greece","Hungary","Iceland","India","Indonesia","Jamaica","Japan","Jordan","Kenya","North Korea",
                  "South Korea","Latvia","Lebanon","Liberia","Libya","Madagascar","Malaysia","Maldives","Mexico",
                  "Morocco","Mozambique","Nepal","New Zealand","Norway","Peru","Philippines","Poland","Portugal",
                  "Puerto Rico","Russia","Saudi Arabia","Singapore","Slovak Republic (Slovakia)","South Africa",
                  "Spain","Sri Lanka","Sweden","Switzerland","Thailand","Netherlands","Ukraine","United Arab Emirates",
                  "United States of America","Vietnam"]:
            self.items.insert(END, x)

            self.spin = StringVar()
            self.spinx = StringVar()
            self.w = Spinbox(self.frame, values=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"), textvariable=self.spin, wrap=True, width=15, state="readonly")
            self.z = Spinbox(self.frame, values=("Air", "Train", "Car"), textvariable=self.spinx, wrap=True, width=15, state="readonly")

        #scrollbar
        self.s = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.items.yview)
        self.items.configure(yscrollcommand=self.s.set)

        #notes
        self.t = Text(self.frame, width=20, height=10, wrap=WORD)
        self.textshow = Label(self.frame, text="Notes")

        #buttons
        self.submit = ttk.Button(self.frame, text="Submit", command=self.fileWrite)
        self.clear = ttk.Button(self.frame, text="Clear", command=self.clr)

        #sizegrip
        self.size = ttk.Sizegrip(self.frame)


        #Gridding
        self.frame.grid(column=0, row=0, sticky=NSEW)
        self.items.grid(column=0, row=0, rowspan=2, padx=(20, 0), pady=(20,0)) #listbox
        self.s.grid(column=1, row=0, rowspan=2, sticky=NS, padx=(0, 30)) #scrollbar
        self.z.grid(column=3, row=3, pady=(5, 10)) #transportation
        self.w.grid(column=3, row=2, pady=(15, 10)) #month
        self.textshow.grid(column=2, row=0, sticky=NS) #textlabel
        self.t.grid(column=2, row=1, padx=(10,10)) #notes
        self.submit.grid(column=3, row=1,sticky=N) #submit
        self.clear.grid(column=3, row=1) #clear
        self.size.grid(column=999, row=999)
        self.size.columnconfigure(0, weight=1)
        self.size.rowconfigure(0, weight=1)
        self.wLabel = Label(self.frame, text="")
        self.wLabel.grid(column=3, row=0)
        self.init_window()

    def fileWrite(self):
        values = [self.items.get(idx) for idx in self.items.curselection()]
        with open("travel_log", "a") as file:
            if self.t != "" and values != "" and self.z != "" and self.w != "":
                file.write(str(values) + "***" + self.z.get() + "***" + self.w.get() + "***" + self.t.get("1.0", END) + "\n")
                self.works()

            else:
                self.wLabel.config("Error")

    def works(self):
        self.wLabel.config(text="Log Successful")
        self.clr()

    def clr(self):
        self.items.selection_clear(0, END)
        self.z.config()
        self.w.config()
        self.t.delete("1.0", END)

    def init_window(self):
        # create a toplevel menu
        self.menubar = Menu(self.master)
        file = Menu(self.menubar, tearoff=0)
        file.add_command(label="Exit", command=root.destroy)
        file.add_command(label="Save", command=self.fileWrite)
        self.menubar.add_cascade(label="File", menu=file)

        help = Menu(self.menubar, tearoff=0)
        help.add_command(label="Help", command=self.help_window)
        self.menubar.add_cascade(label="Help", menu=help)

        # display the menu
        self.master.config(menu=self.menubar)

    def help_window(self):
        self.top = Toplevel()
        self.top.title("Help")
        self.msg = Message(self.top, text="Travel Program", width=200)
        self.msg.grid(column=0, row=0, padx=(10,10))

        self.msg1 = Message(self.top, text="Version 1.0", width=200)
        self.msg1.grid(column=0, row=1, padx=(10, 10))

        self.msg2 = Message(self.top, text="Gregory Clarke", width=200)
        self.msg2.grid(column=0, row=2, padx=(10, 10))

        self.button = Button(self.top, text="Dismiss", command=self.top.destroy)
        self.button.grid(column=0, row=3, padx=(10,10), pady=(0, 10))


root = Tk()
app = App(root)
root.title("Travel Log")
root.mainloop()
root.destroy()
