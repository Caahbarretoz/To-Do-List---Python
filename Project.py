
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
import customtkinter
import os


lista = []
def get_task():
    global entry
    if entry.get() == "":
        messagebox.showinfo(title="Erro", message="Digite algo no campo")
        return
    value = [("•" + entry.get())]
    lista.append(value)
    tree.insert('', "end", values=value)
    entry.delete(0, END)
    entry.focus()


def enter(event):
    get_task()


def delete_task():
    try:
        item = tree.selection()[0]
        tree.delete(item)
    except:
        messagebox.showinfo(title="Erro", message="Selecione uma tarefa a ser deletada")


def save_file():
    global entry
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output:
        first = '\n'.join(lista[0])
        output.write(first)
        for i in range(1, len(lista)):
            text = '\n'.join(lista[i])
            output.write("\n" + text)
        output.close()
    janela.title(f"To Do List - {filepath}")


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

janela = customtkinter.CTk()
janela.geometry("400x650")
janela.resizable(False, False)
janela.iconbitmap('./pictures/notepad.ico')
janela.config(bg="black")

current_path = os.path.dirname((os.path.realpath(__file__)))

bg_image = customtkinter.CTkImage(Image.open(current_path + "./pictures/sidefire.png"),
                                             size = (240, 700))

add_image = customtkinter.CTkImage(Image.open(current_path + "./pictures/plusor.png"), size=(10, 10))

delete_image = customtkinter.CTkImage(Image.open(current_path + "./pictures/deleteor.png"), size=(15, 15))

save_image = customtkinter.CTkImage(Image.open(current_path + "./pictures/downloador.png"), size=(15, 15))

logo = customtkinter.CTkImage(Image.open(current_path + "./pictures/agenda.png"),
                                             size = (35, 35))

style = ttk.Style(janela)
# set ttk theme to "clam" which support the fieldbackground option
style.theme_use("clam")
style.configure("Treeview", background="gray10",
                fieldbackground="gray10", foreground="#ff8f00", font=("Roboto", 12))

style.configure("Treeview.Heading", background="DarkOrchid4", foreground="#ff8f00", font=("Roboto", 12))

janela.title("To Do List")

bg_image_label = customtkinter.CTkLabel(janela, image=bg_image, text="", bg_color="black")
bg_image_label.grid(row=0, column=0, padx=(0,160))

logolbl = customtkinter.CTkLabel(janela,
                              text="",
                              image=logo,
                                bg_color="black"
                              )
logolbl.grid(row=0, column=0, padx=(230, 0), pady=(40, 600))


label = customtkinter.CTkLabel(janela,
                                text="To Do List",
                                text_color="DarkOrchid4",
                                font=("Bentham", 40),
                                bg_color="black")
label.grid(row=0, column=0, pady=(40, 600), padx=(40, 60))


columns = ('Tarefas')
tree = ttk.Treeview(janela, columns=columns, show='headings')

tree.heading('Tarefas', text='Tarefas')
tree.grid(row=0, column=0, pady=(100, 350), ipadx=50)


entry = customtkinter.CTkEntry(janela,
                               placeholder_text="Digite nova tarefa...",
                               placeholder_text_color="#ff8f00",
                                fg_color="gray23",
                                text_color="#ff8f00",
                                border_color="DarkOrchid4",
                                border_width=3,
                                corner_radius=15,
                               bg_color="black"
                               )
entry.grid(row=0, column=0, padx=(30, 70), pady=(230,50), ipadx=10)

add_btn = customtkinter.CTkButton(janela,
                                  corner_radius=15,
                                  fg_color="gray23",
                                  border_width=3,
                                  width=30,
                                  height=30,
                                  border_color="DarkOrchid4",
                                  image=add_image,
                                  text="",
                                  bg_color="black",
                                  command=get_task)
add_btn.grid(row=0, column=0, pady=(230,50), padx=(180,0),ipadx=0, ipady=0)


frame_btn = customtkinter.CTkFrame(janela, fg_color="transparent", bg_color="black")
frame_btn.grid(row=0, column=0, pady=(430, 0))


btn_delete = customtkinter.CTkButton(frame_btn,
                                     text="Deletar",
                                     text_color="#ff8f00",
                                     fg_color="gray23",
                                     border_color="DarkOrchid4",
                                     command=delete_task,
                                     border_width=3,
                                     corner_radius=15,
                                     image=delete_image,
                                     compound="right",
                                     bg_color="black"
                                     )
btn_delete.grid(row=0, column=0, pady=(0,10))

btn_save = customtkinter.CTkButton(frame_btn,
                                   text="Salvar",
                                   text_color="#ff8f00",
                                   fg_color="gray23",
                                   command=save_file,
                                   border_color="DarkOrchid4",
                                   border_width=3,
                                   corner_radius=15,
                                   image=save_image,
                                   compound="right",
                                   bg_color="black"
                                   )
btn_save.grid(row=4, column=0)

janela.grid_columnconfigure(0, weight=1)
frame_btn.grid_columnconfigure(0, weight=1)
janela.bind("<Return>", enter)

janela.mainloop()


