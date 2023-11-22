import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Initialize canvas as a global variable
canvas = None

def draw_rectangle():
    global canvas  # Declare canvas as a global variable
    try:
        # Lấy giá trị từ các Entry
        side1 = float(side1_entry.get())
        side2 = float(side2_entry.get())
        side3 = float(side3_entry.get())
        side4 = float(side4_entry.get())

        # Vẽ hình chữ nhật
        fig, ax = plt.subplots()
        rectangle = plt.Rectangle((0, 0), side1, side2, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rectangle)

        # Cập nhật canvas
        canvas.get_tk_widget().destroy()
        canvas_container = tk.Frame(root)
        canvas_container.grid(row=1, column=2, rowspan=6, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)
        canvas = FigureCanvasTkAgg(fig, master=canvas_container)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    except ValueError:
        # Xử lý nếu nhập không đúng giá trị
        result_label.config(text="Vui lòng nhập đúng giá trị cho độ dài các cạnh.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Vẽ Hình Chữ Nhật")

# Tạo các widget
side1_label = tk.Label(root, text="Cạnh 1:")
side1_entry = tk.Entry(root)

side2_label = tk.Label(root, text="Cạnh 2:")
side2_entry = tk.Entry(root)

side3_label = tk.Label(root, text="Cạnh 3:")
side3_entry = tk.Entry(root)

side4_label = tk.Label(root, text="Cạnh 4:")
side4_entry = tk.Entry(root)

draw_button = tk.Button(root, text="Vẽ Hình Chữ Nhật", command=draw_rectangle)

result_label = tk.Label(root, text="Kết quả vẽ sẽ được hiển thị ở đây.")

# Định vị các widget trong cửa sổ
side1_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
side1_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
side2_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
side2_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
side3_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
side3_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
side4_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
side4_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
draw_button.grid(row=4, column=0, columnspan=2, pady=10)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Canvas để hiển thị đồ thị
canvas_container = tk.Frame(root)
canvas_container.grid(row=1, column=2, rowspan=6, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)
canvas = FigureCanvasTkAgg(plt.Figure(), master=canvas_container)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Chạy ứng dụng
root.mainloop()
