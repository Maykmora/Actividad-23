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

ventana.mainloop()