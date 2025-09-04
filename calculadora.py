import tkinter as tk

ventana= tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x400")

numero1=tk.Label(ventana, text="Ingrese primer numero:")
numero1.pack(pady=5)

entrada1=tk.Entry(ventana)
entrada1.pack(pady=1)

numero2=tk.Label(ventana, text="Ingrese segundo numero:")
numero2.pack(pady=5)

entrada2=tk.Entry(ventana)
entrada2.pack(pady=1)


def sumar():
    resultado= float(entrada1.get()) + float(entrada2.get())
    resultado_final = tk.Label(ventana, text="Resultado: " + str(resultado))
    resultado_final.pack(pady=5)

def restar():
    resultado= float(entrada1.get()) - float(entrada2.get())
    resultado_final=tk.Label(ventana, text="Resultado:"+ str(resultado))
    resultado_final.pack(pady=5)
def multiplicar():
    resultado= float(entrada1.get()) * float(entrada2.get())
    resultado_final = tk.Label(ventana, text="Resultado:" + str(resultado))
    resultado_final.pack(pady=5)


boton_sumar=tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)
boton_restar= tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady=5)
boton_multiplicar=tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady=5)

ventana.mainloop()