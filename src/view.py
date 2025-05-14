from tkinter import (
    Tk,
    Menu,
    Button,
    Listbox,
    END,
    StringVar,
    Label,
    Entry,
    Frame,
    Text,
    Scrollbar,
    messagebox,
    filedialog,
    Toplevel,
    PhotoImage,
    Canvas,
    StringVar,
    IntVar,
    Radiobutton,
    Checkbutton,
    messagebox,
)

root = Tk()
root.title("MeetingPro")
root.geometry("1080x720")
root.minsize(480, 360)
root.iconbitmap("src/MeetingPro.ico")


# change menu
def main_menu():
    hide_all()
    main_file.pack(fill="both", expand=1)
def add_menu():
    hide_all()
    add_file.pack(fill="both", expand=1)
def show_menu():
    hide_all()
    show_file.pack(fill="both", expand=1)


def reserve_menu():
    hide_all()
    reserve_file.pack(fill="both", expand=1)


# hide all frames
def hide_all():
    main_file.pack_forget()
    add_file.pack_forget()
    show_file.pack_forget()
    reserve_file.pack_forget()


# create a menu bar
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_checkbutton(label="accueil", command=main_menu)
my_menu.add_checkbutton(label="ajouter", command=add_menu)
my_menu.add_checkbutton(label="réserver", command=reserve_menu)
my_menu.add_checkbutton(label="afficher", command=show_menu)


# create menu
main_file = Frame(root, bg="red")
add_file = Frame(root, bg="blue")
show_file = Frame(root, bg="green")
reserve_file = Frame(root, bg="yellow")


root.mainloop()
