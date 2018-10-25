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
'''
""" 
    This is a travel program where you can log your travels and add notes to each log.
"""

#Gregory Clarke
#Advanced Computer Programming
#10/24/2018


from tkinter import *
from tkinter import ttk


class App:
    def __init__(self):
        self.content = Frame(root)

        self.countries = Label(self.content, text="Countries")
        self.items = Listbox(self.content, height=10, selectmode="SINGLE",
                             exportselection=FALSE)  # listbox for items on sale
        self.items.bind("<<ListboxSelect>>")
        for b in ["Argentina","Australia","Austria","Brazil","Canada","China","Croatia","Cuba","Czech Republic",
                  "Denmark","Egypt","Estonia","Ethiopia","Finland","France","Germany","Great Britain",
                  "Greece","Hungary","Iceland","India","Indonesia","Jamaica","Japan","Jordan","Kenya","North Korea",
                  "South Korea","Latvia","Lebanon","Liberia","Libya","Madagascar","Malaysia","Maldives","Mexico",
                  "Morocco","Mozambique","Nepal","New Zealand","Norway","Peru","Philippines","Poland","Portugal",
                  "Puerto Rico","Russia","Saudi Arabia","Singapore","Slovak Republic (Slovakia)","South Africa",
                  "Spain","Sri Lanka","Sweden","Switzerland","Thailand","Netherlands","Ukraine","United Arab Emirates",
                  "United States of America","Vietnam"]:
            self.items.insert(END, b)  # Adds values to listbox

        self.bar = ttk.Scrollbar(self.content, orient=VERTICAL, command=self.items.yview)
        self.items.configure(yscrollcommand=self.bar.set)  # attaches scrollbar to listbox

        self.write = Text(self.content, width=14, height=10, wrap=WORD)  # textbox
        self.write.bind("<FocusIn>")
        self.textshow = Label(self.content, text="Description")  # label for textbox
        self.limit = Label(self.content, text="")

        self.spinvallabel = Label(self.content, text="Month")
        self.spinval = StringVar()
        self.s = Spinbox(self.content, values=(
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
        "December"), textvariable=self.spinval, wrap=True, width=22, state="readonly")

        self.show = Label(self.content, text="Transportation")  # label for combobox
        self.choosevalue = StringVar()  # value for combobox
        self.choosevalue.set("")
        self.box = ttk.Combobox(self.content, state="readonly", textvariable=self.choosevalue)
        self.box["values"] = ["Air", "Train", "Car"]  # Types of transportation
        self.box.bind("<<ComboboxSelected>>")  # applies selected value

        self.submitbutton = Button(self.content, text="Submit", command=self.submit)  # buttons to submit and clear
        self.clear = Button(self.content, text="Clear", command=self.clear)

        self.menubar = Menu(root)  # menubar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)  # creates option in menubar
        self.filemenu.add_command(label="Save", command=self.submit)  # options in file
        self.filemenu.add_command(label="Exit", command=root.quit)

        self.error = Label(self.content)  # label for errors

        self.menubar2 = Menu(root)  # second menu for "help"
        self.helpmenu = Menu(self.menubar2, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)  # creates option in menubar
        self.helpmenu.add_command(label="About", command=self.new)  # option in help
        root.config(menu=self.menubar)

        self.grip_frame = Frame(root)

        self.size = ttk.Sizegrip(self.grip_frame)

        self.content.grid(column=0, row=0)  # grids widgets
        self.error.grid(column=3, row=4, sticky=N)
        self.countries.grid(column=0, row=0)
        self.items.grid(column=0, row=0, rowspan=4, sticky=NS)
        self.box.grid(column=3, row=1, sticky=N, padx=(10, 0))  # grid for items/combobox
        self.bar.grid(column=1, row=0, rowspan=4, sticky=NS, padx=(0, 20))
        self.write.grid(column=2, row=1, rowspan=3)  # textbox grid
        self.limit.grid(column=2, row=4)
        self.textshow.grid(column=2, row=0)
        self.spinvallabel.grid(column=3, row=1, sticky=S, pady=(15, 0))
        self.s.grid(column=3, row=2, sticky=N, pady=(0, 15), padx=(12, 0))
        self.show.grid(column=3, row=0)
        self.submitbutton.grid(column=3, row=2, sticky=S, pady=(15, 5))
        self.clear.grid(column=3, row=3, sticky=N, pady=0)
        self.size.grid(column=999, row=999, sticky=NSEW)
        self.grip_frame.grid(column=999, row=999)

        root.columnconfigure(0, weight=1)  # weight for rows and columns
        root.rowconfigure(0, weight=1)
        root.minsize(450, 250)
        self.grip_frame.columnconfigure(999, weight=1)
        self.grip_frame.rowconfigure(999, weight=1)

    def clear(self):  # clears all widgets
        self.write.delete("1.0", END)
        self.spinval.set("January")
        self.choosevalue.set("")
        self.items.bind(self.items.selection_clear(0, END))
        self.error.config(text="")
        self.limit.config(text="")

    def submit(self):  # submits values to file
        z = 0
        values = [self.items.get(idx) for idx in self.items.curselection()]  # gets all values
        textvalue = self.write.get("1.0", 'end-1c')
        count = len(textvalue)
        if count > 500:  # checks for max amount of characters
            z = 1
            self.error.config(text="Error")
            self.limit.config(text=("Over 500 characters\n" + str(count) + " characters"))
        month = self.spinval.get()
        transport = self.choosevalue.get()
        if any(x in "abcdefghijklmnopqrstuvwxyz" for x in textvalue):  # checks for letters in textbox
            self.x = []  # puts all values in list
            textvalue = textvalue.replace("\n", "*")
            textvalue = textvalue.replace(" ", "^")
            self.x.append(values[0])
            self.x.append(textvalue)
            self.x.append(month)
            self.x.append(transport)
            for y in self.x:  # runs through all values
                if y == "" or y == 0 or y == []:  # checks for empty inputs
                    self.error.config(text="Error")
                    z = 1
        else:  # if no letters in input
            z = 1
            self.error.config(text="Error")
        if z == 0:  # no errors
            str1 = ' '.join(str(e) for e in self.x)  # turns values into string
            file = open("travel_log.txt", "a")
            file.write(str1)  # writes values to file
            file.write("\n")
            file.close()
            self.write.delete("1.0", END)  # clears all boxes
            self.spinval.set("January")
            self.choosevalue.set("")
            self.items.bind(self.items.selection_clear(0, END))
            self.error.config(text="Submitted")
            self.limit.config(text="")

    def new(self):  # makes new top level for about
        top = Toplevel(root, padx=15, pady=15)
        top.title("About")
        msg = Message(top, text="Travel Log\nVersion 1.1\nGregory Clarke", width=100)
        msg.pack()
        button = Button(top, text="Close", command=top.destroy)
        button.pack()
        top.resizable(width=False, height=False)


root = Tk()
app = App()
root.title("Travel Log")
root.mainloop()
root.destroy()