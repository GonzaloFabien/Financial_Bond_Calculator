import tkinter as tk

#6-Creamos la función: 
def guardar_valor():
    valor_consola = caja_texto.get()
    print(f"El valor guardado es = {valor_consola}")
    return valor_consola

#1-Se crea la ventana principal:
ventana = tk.Tk()
ventana.title("Bonos")
ventana.geometry("700x600")

#2-Se añade texto inicial con Label:
texto_inicial = tk.Label(ventana, text="Calculadora de Bonos: Precio, valor, Duración, Convexidad, etc:")
texto_inicial.pack(pady=5)


#3-Se crea el input_text,:
#7- Le añadimos estilo a este formulario:
#4-Se añade texto por defecto en el input:
contenedor_form = tk.Frame(ventana)
contenedor_form.pack(pady=10)

texto_izquierda = tk.Label(contenedor_form, text="F= Face Value:")
texto_izquierda.pack(side="left",padx=10)

caja_texto = tk.Entry(contenedor_form, width=20)
caja_texto.pack(pady=20)

caja_texto.insert(0,"100")

#8- Se hace los demás formularios para cada item de los bonos:"M= Años por vencer:"

contenedor_M = tk.Frame(ventana)
contenedor_M.pack(pady=10)
texto_izq_M = tk.Label(contenedor_M, text="M= Años por vencer:")
texto_izq_M.pack(side="left", padx=10)

caja_entry_M = tk.Entry(contenedor_M,width=20)
caja_entry_M.pack(pady=20)



#5-Se crea el boton para capturar la función:
botoncito = tk.Button(ventana, text="Ejecutar", command=guardar_valor)
botoncito.pack(pady=20)

ventana.mainloop()