import tkinter as tk
import sympy as sym
from tkinter import messagebox

def dao_ham(f, var = 'x'):
    x = sym.symbols(var)
    result = sym.diff(f, x)
    return str(result)

    
def tich_phan(f, var = 'x', lower_limit = None, upper_limit  = None):
    x = sym.symbols(var)
    result = sym.integrate(f, (x, lower_limit, upper_limit))
    return str(result)
    
    
def nguyen_ham(f, var = 'x'):
    x = sym.symbols(var)
    result = sym.integrate(f, x)
    return str(result)



        
def display_DH():
    try:
        f_str = str(entry_f.get())
        f = sym.sympify(f_str)
        result = dao_ham(f)
        text_DH.delete(1.0, tk.END)
        text_DH.insert(tk.END, result)
        
    except: 
        messagebox.showerror("Lỗi", "Nhập lại hàm số.")
        text_DH.delete(1.0, tk.END)
    
    
def display_NH():
    try:
        f_str = str(entry_f.get())
        f = sym.sympify(f_str)
        result = nguyen_ham(f)
        text_NH.delete(1.0, tk.END)
        text_NH.insert(tk.END, result)
        
    except: 
        messagebox.showerror("Lỗi", "Nhập lại hàm số.")
        text_NH.delete(1.0, tk.END)   
        
        
def display_TP():
    try:
        f_str = str(entry_f.get())
        high = entry_upper.get()
        low = entry_lower.get()
        f = sym.sympify(f_str)
        result = tich_phan(f, low, high)
        text_TP.delete(1.0, tk.END)
        text_TP.insert(tk.END, result)
        
    except Exception as e: 
        messagebox.showerror("Lỗi", str(e))
        text_TP.delete(1.0, tk.END)  

window = tk.Tk()

window.title("Giải tích cơ bản")
window.geometry("900x360")
entry_label = tk.Label(window, text="Nhập hàm số: ").grid(row = 0, column = 0)
entry_f = tk.Entry(window, width=100)
entry_f.grid(row = 0, column = 1)
text_DH = tk.Text(window, height=1, width=50)
text_DH.grid(row = 2, column = 1)



blank1 = tk.Label().grid(row = 1)
button_DH = tk.Button(window, text = "Tính đạo hàm", command = display_DH)
button_DH.grid(row = 2, column= 0)
#label_DH = tk.Label(window, text = "Result appears here").grid(row = 2, column = 1)

blank2 = tk.Label().grid(row = 3)
button_DH = tk.Button(window, text = "Tính nguyên hàm", command=display_NH)
button_DH.grid(row = 4, column= 0)
text_NH = tk.Text(window, height=1, width=50)
text_NH.grid(row = 4, column = 1)


blank3 = tk.Label().grid(row = 5)
upper_label = tk.Label(window, text = "Ngưỡng trên").grid(row = 6, column=0)
entry_upper = tk.Entry(window, width=20)
entry_upper.grid(row = 6, column=1)

lower_label = tk.Label(window, text = "Ngưỡng dưới").grid(row = 7, column=0)
entry_lower = tk.Entry(window, width=20)
entry_lower.grid(row = 7, column=1)

blank4 = tk.Label().grid(row = 8)
button_TP = tk.Button(window, text = "Tính tích phân", command=display_TP)
button_TP.grid(row = 9, column= 0)
text_TP = tk.Text(window, height=1, width=50)
text_TP.grid(row = 9, column = 1)

window.mainloop()