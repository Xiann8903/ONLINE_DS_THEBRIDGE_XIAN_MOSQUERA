import tkinter as tk

ventana_inicio = tk.Tk()
ventana_inicio.title("App cuentas de morsito")
ventana_inicio.geometry("300x200")
saludors = tk.Label(ventana_inicio, text="Bienvenida Morsito")
saludors.pack()
boton_inicio = tk.Button(ventana_inicio, text="Empezarors", cursor= "heart")
boton_inicio.pack(pady=20)

ventana_inicio.mainloop()