from cProfile import label
import re
from curses import window
from tkinter import *
from tkinter import messagebox

from zmq import device

ip_regex = '^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$'
ip_match = re.compile(ip_regex)

device_list = ['10.10.10.10']


def submit_func():
    ip = entry.get()

    if(re.search(ip_match, ip)):
        messagebox.askyesno("Confirmation", "Do you want to block '%s' ?" % ip)
        if ip in device_list:
            messagebox.showinfo(
                "Informaton", "%s is already a part of malicious group" % ip)
        else:
            messagebox.showinfo(
                "Informaton", "BLOCKED!\n%s is added to the malicious group" % ip)
    else:
        messagebox.showwarning(
            "Invalid IP", "%s is not an valid IP.\nPlease check." % ip)


def clear_func():
    entry.delete(0, END)


window = Tk()
window.title('IP Blocker')
window.geometry('450x300')
window.iconbitmap("assa-abloy-lcon.ico")

ab_logo = PhotoImage(name="AB Logo", file=".\\ab-logo.png")
label = Label(window, image=ab_logo, bd=5)
label.pack(padx=10, pady=10)

entry = Entry()
entry.config(font=('Sans serif', 14), background='sky blue',
             foreground='#0047ab', width=15)
# use show attr for password, show="*"
submit = Button(window, text="Block", command=submit_func, relief=RAISED)
clear = Button(window, text="Clear", command=clear_func, relief=RAISED)
entry.pack()
submit.pack()
clear.pack()

window.mainloop()
