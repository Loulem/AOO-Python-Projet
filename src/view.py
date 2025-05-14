from tkinter import Tk, Menu, Button, Listbox, END, StringVar, Label, Entry

root = Tk()
root.title("MeetingPro")
root.geometry("1080x720")
root.minsize(480, 360)
root.iconbitmap("src/MeetingPro.ico")


# change menu
def main_menu():
    main_file.pack(fill="both", expand=1)


def add_menu():
    add_file.pack(fill="both", expand=1)


# create a menu bar
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="ajouter", menu=file_menu)
file_menu.add_command(label="ajouter", command=add_menu)
file_menu.add_command(label="menu principal", command=main_menu)


# create menu
main_file = Menu(root, bg="red", withdraw=1)

add_file = Menu(root, bg="blue")


root.mainloop()
