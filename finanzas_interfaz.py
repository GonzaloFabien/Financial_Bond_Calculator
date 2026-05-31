import tkinter as tk

#Creamos la función: 
def guardar_valor():
    valor_consola = caja_texto.get()
    print(f"El valor guardado es = {valor_consola}")
    return valor_consola

#1-Se crea la ventana principal:
ventana = tk.Tk()
ventana.title("Bonos")
ventana.geometry("700x600")

#2-Se añade texto inicial con Label:
texto_inicial = tk.Label(ventana, text="Texto inicial")
texto_inicial.pack(pady=5)


#3-Se crea el input_text:
caja_texto = tk.Entry(ventana, width=20)
caja_texto.pack(pady=50)

#4-Se añade texto por defecto en el input:
caja_texto.insert(0,"100")

#Se crea el boton para capturar la función:
botoncito = tk.Button(ventana, text="Ejecutar", command=guardar_valor)
botoncito.pack(pady=20)

ventana.mainloop()