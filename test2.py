import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def draw_triangle(side1, side2, side3):
    # Kiểm tra xem các độ dài cạnh có tạo thành một tam giác hợp lệ không
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        # Vẽ hình tam giác
        fig, ax = plt.subplots()
        ax.plot([0, side1, side2, 0], [0, 0, side3, 0], 'r-')

        # Đảm bảo tỷ lệ giữa các trục x và y được duy trì
        plt.axis('scaled')

        # Tối ưu hóa bố cục của đồ thị
        plt.tight_layout()

        # Hiển thị đồ thị
        plt.show()
    else:
        result_label.config(text="Độ dài các cạnh không tạo thành tam giác hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Vẽ Tam Giác")

# Tạo các widget
side1_label = tk.Label(root, text="Cạnh 1:")
side1_entry = tk.Entry(root)

side2_label = tk.Label(root, text="Cạnh 2:")
side2_entry = tk.Entry(root)

side3_label = tk.Label(root, text="Cạnh 3:")
side3_entry = tk.Entry(root)

draw_button = tk.Button(root, text="Vẽ Tam Giác", command=lambda: draw_triangle(float(side1_entry.get()), float(side2_entry.get()), float(side3_entry.get())))

result_label = tk.Label(root, text="Kết quả vẽ sẽ được hiển thị ở đây.")

# Định vị các widget trong cửa sổ
side1_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
side1_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
side2_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
side2_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
side3_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
side3_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
draw_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Chạy ứng dụng
root.mainloop()
