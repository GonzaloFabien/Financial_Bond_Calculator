import tkinter as tk

#Declaramos las variables con None para posteriormente tener un mayor scope:
valor_FaceValue = None
valor_M_vencimiento = None
valor_C_cupon = None
valor_r_rendimiento = None
Flujo_Caja = None

#6-Creamos la función: 
def guardar_valor():
    global valor_FaceValue
    global valor_M_vencimiento
    global valor_C_cupon
    global valor_r_rendimiento
    global Flujo_Caja
    
    valor_FaceValue = int(caja_texto.get())
    valor_M_vencimiento = int(caja_entry_M.get())
    valor_C_cupon = int(caja_entry_C.get())
    valor_r_rendimiento = int(caja_entry_r.get())

    print(f"Los valores para FaceValue = {valor_FaceValue}, M_vencimiento = {valor_M_vencimiento}, C_cupon= {valor_C_cupon}, r_rendimiento= {valor_r_rendimiento}")
    
    #Creamos la variable array Flujo de Caja[t]:
    Flujo_Caja = [valor_FaceValue*valor_C_cupon] *valor_M_vencimiento
    print(len(Flujo_Caja))

    return valor_FaceValue

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

#9-Lo mismo para tasa Cupon:
contenedor_C= tk.Frame(ventana)
contenedor_C.pack(pady=10)
texto_izq_C = tk.Label(contenedor_C, text="C= Tasa cupón:")
texto_izq_C.pack(side="left", padx=10)

caja_entry_C = tk.Entry(contenedor_C,width=20)
caja_entry_C.pack(pady=20)

#10-Lo mismo para la tasa de Mercado r: 
contenedor_r= tk.Frame(ventana)
contenedor_r.pack(pady=10)
texto_izq_r = tk.Label(contenedor_r, text="r= rendimiento Mercado:")
texto_izq_r.pack(side="left", padx=10)

caja_entry_r = tk.Entry(contenedor_r,width=20)
caja_entry_r.pack(pady=20)



#5-Se crea el boton para capturar la función:
botoncito = tk.Button(ventana, text="Ejecutar", command=guardar_valor)
botoncito.pack(pady=20)


#Creamos el algoritmo para poder dar con la operacionalidad de las variables:
print(valor_M_vencimiento);




ventana.mainloop()

print(f"Una vez acabado el programa devolveré el valor del array, el último:{valor_M_vencimiento}")