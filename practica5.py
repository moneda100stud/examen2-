from tkinter import *
from tkinter import filedialog, colorchooser, simpledialog  # Importar módulos necesarios


def open_file():
    """Función para abrir un archivo y mostrar su contenido en el área de texto."""
    file_path = filedialog.askopenfilename()  # Abrir un cuadro de diálogo para seleccionar un archivo
    if file_path:  # Verificar si se seleccionó un archivo
        with open(file_path, 'r') as file:  # Abrir el archivo en modo lectura
            content = file.read()  # Leer el contenido del archivo
            text_area.delete(1.0, END)  # Borrar el área de texto antes de mostrar el nuevo contenido
            text_area.insert(END, content)  # Insertar el contenido del archivo en el área de texto



def save_file():
    """Función para guardar el contenido del área de texto en un archivo."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",  # Abrir un cuadro de diálogo para guardar el archivo
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:  # Verificar si se seleccionó una ubicación para guardar
        with open(file_path, 'w') as file:  # Abrir el archivo en modo escritura
            content = text_area.get(1.0, END)  # Obtener el contenido del área de texto
            file.write(content)  # Escribir el contenido en el archivo


def delete_text():
    text_area.delete(1.0, END)  # borrar el texto del area de texto

def change_color():
    """Función para cambiar el color de texto del área de texto."""
    color = colorchooser.askcolor()[1]  # Abrir un cuadro de diálogo para seleccionar un color
    if color:  # Verificar si se seleccionó un color
        text_area.config(fg=color)  # Cambiar el color de texto del área de texto


def search_and_replace():
    """Función para buscar y reemplazar texto en el área de texto."""
    search_text = simpledialog.askstring("Buscar", "Texto a buscar:")  # Pedir al usuario el texto a buscar
    replace_text = simpledialog.askstring("Reemplazar", "Texto de reemplazo:")  # Pedir al usuario el texto de reemplazo
    if search_text and replace_text:  # Verificar que ambos textos sean proporcionados
        content = text_area.get(1.0, END)  # Obtener el contenido del área de texto
        new_content = content.replace(search_text, replace_text)  # Reemplazar el texto buscado por el texto de reemplazo
        text_area.delete(1.0, END)  # Borrar el área de texto
        text_area.insert(END, new_content)  # Insertar el nuevo contenido en el área de texto



#Aqui esta el cuerpo base de la ventana principal
ventana_principal = Tk()
ventana_principal.title("Ventana principal")
ventana_principal.minsize(width=400, height=300)
ventana_principal.config(padx=35, pady=35)

# se crear el area de texto
text_area = Text(ventana_principal, wrap='word', width=50, height=15)
text_area.pack()

# aqui se crear la barra de menu 
menu_bar = Menu(ventana_principal)

# aqui añades las opciones del menu y archivos (open,save,delete,file)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Delete", command=delete_text, accelerator="Ctrl+D")
menu_bar.add_cascade(label="File", menu=file_menu)

# Aqui se añade el boton  cambio de color de texto 
color_button = Button(ventana_principal, text="cambio de color de texto", command=change_color)
color_button.pack()

# se agregar el boton de buscar y reemplazar texto
search_button = Button(ventana_principal, text="buscar y remplazar texto", command=search_and_replace)
search_button.pack()
# aqui se muestra la ventana principal
ventana_principal.config(menu=menu_bar)

# Vincular atajos de teclado
ventana_principal.bind('<Control-o>', lambda event: open_file())
ventana_principal.bind('<Control-s>', lambda event: save_file())
ventana_principal.bind('<Control-d>', lambda event: delete_text())
#aqui es el bucle para mantener abierto la ventana principal
ventana_principal.mainloop()
