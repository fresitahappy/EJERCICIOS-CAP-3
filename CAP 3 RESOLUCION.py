import tkinter as tk
from tkinter import messagebox

# Función para calcular G(n)
def calcular_g(n):
    return (4 * n**3 + 9 * n**2 - 13 * n) / 6

# Función para calcular la aproximación (2/3)n^3
def calcular_aproximacion(n):
    return (2 / 3) * n**3

# Función para calcular el error porcentual
def calcular_error(g_n, aprox):
    if g_n == 0:  # Verificar si g_n es cero para evitar división por cero
        return float('inf')  # Retorna infinito si g_n es cero
    return abs(g_n - aprox) / g_n * 100

# Función para buscar el primer valor de n con error < 1%
def encontrar_valor_n():
    n = 1
    while True:
        g_n = calcular_g(n)
        aprox = calcular_aproximacion(n)
        error = calcular_error(g_n, aprox)
        if error < 1:
            return n
        n += 1

# Función para ejecutar el cálculo y mostrar los resultados
def ejecutar_calculo():
    try:
        # Asegurarse de que el valor de n es un entero válido
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("El valor de n debe ser mayor que cero.")

        # Cálculos
        g_n = calcular_g(n)
        aprox = calcular_aproximacion(n)
        error = calcular_error(g_n, aprox)
        primer_n = encontrar_valor_n()

        # Mostrar resultados formateados
        result_text = (f"Cálculo exacto de G({n}): {g_n:,.2f}\n"
                       f"Aproximación (2/3)n^3: {aprox:,.2f}\n"
                       f"Error porcentual: {error:.4f}%\n"
                       f"Primer valor de n con error < 1%: {primer_n}")

        messagebox.showinfo("Resultados", result_text)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")

# Crear la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Cálculo de Operaciones Aritméticas")

# Etiqueta y campo de entrada para el valor de n
label_n = tk.Label(root, text="Ingrese el valor de n:")
label_n.pack(pady=10)
entry_n = tk.Entry(root)
entry_n.pack(pady=5)

# Botón para ejecutar el cálculo
btn_calcular = tk.Button(root, text="Calcular", command=ejecutar_calculo)
btn_calcular.pack(pady=10)

# Iniciar la ventana
root.mainloop()
