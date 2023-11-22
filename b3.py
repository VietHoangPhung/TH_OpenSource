import tkinter as tk
import sympy as sym
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def draw_rectangle(side1, side2):
    # Vẽ hình chữ nhật
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((0, 0), side1, side2, linewidth=1, edgecolor='r', facecolor='y')
    ax.add_patch(rectangle)

    # Đảm bảo tỷ lệ giữa các trục x và y được duy trì
    plt.axis('scaled')

    # Tối ưu hóa bố cục của đồ thị
    plt.tight_layout()

    # Hiển thị đồ thị
    plt.show()

def open_rect_win():
    sub_win = tk.Toplevel(win)
    sub_win.title("Hinh chu nhat")
    sub_win.geometry("400x400")
    l1 = tk.Label(sub_win, text="Do dai canh 1:")
    l1.pack()
    c1_entry = tk.Entry(sub_win, width=50)
    c1_entry.pack()
    l2 = tk.Label(sub_win, text="Do dai canh 2:")
    l2.pack()
    c2_entry = tk.Entry(sub_win, width=50)
    c2_entry.pack()
    dt = tk.Label(sub_win)
    dt.pack()
    cv = tk.Label(sub_win)
    cv.pack()
    button_draw = tk.Button(sub_win, text = "Ve", command= lambda:draw_rectangle(float(c1_entry.get()), float(c2_entry.get())))
    button_draw.pack()
    button_cal1 = tk.Button(sub_win, text = "Dien tich", command= lambda:dt.config(text="Dien tich: " + str(float(c1_entry.get())* float(c2_entry.get()))))
    button_cal1.pack()
    button_cal2 = tk.Button(sub_win, text = "Chu vi", command= lambda:cv.config(text="Chu vi: " + str(float(c1_entry.get())+ float(c2_entry.get()))))
    button_cal2.pack()
    
    
def draw_triangle(side1, side2, side3):
    # Kiểm tra xem các độ dài cạnh có tạo thành một tam giác hợp lệ không
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        # Vẽ hình tam giác
        fig, ax = plt.subplots()
        triangle = Polygon([[0, 0], [side1, 0], [0.5*(side2), 0.5*((np.sqrt(3) * side2))]], closed=True, edgecolor='r', facecolor='none')
        ax.add_patch(triangle)

        # Đảm bảo tỷ lệ giữa các trục x và y được duy trì
        plt.axis('scaled')

        # Tối ưu hóa bố cục của đồ thị
        plt.tight_layout()

        # Hiển thị đồ thị
        plt.show()
    #else:
        #result_label.config(text="Độ dài các cạnh không tạo thành tam giác hợp lệ.")

def open_triangle_win():
    sub_win = tk.Toplevel(win)
    sub_win.title("Hinh tam giac")
    sub_win.geometry("400x400")
    l1 = tk.Label(sub_win, text="Do dai canh 1:")
    l1.pack()
    c1_entry = tk.Entry(sub_win, width=50)
    c1_entry.pack()
    l2 = tk.Label(sub_win, text="Do dai canh 2:")
    l2.pack()
    c2_entry = tk.Entry(sub_win, width=50)
    c2_entry.pack()
    l3 = tk.Label(sub_win, text="Do dai canh 3:")
    l3.pack()
    c3_entry = tk.Entry(sub_win, width=50)
    c3_entry.pack()
    dt = tk.Label(sub_win)
    dt.pack()
    cv = tk.Label(sub_win)
    cv.pack()
    button_draw = tk.Button(sub_win, text = "Ve", command= lambda:draw_triangle(float(c1_entry.get()), float(c2_entry.get()), float(c3_entry.get())))
    button_draw.pack()
    button_cal1 = tk.Button(sub_win, text = "Dien tich", command= lambda:dt.config(text="Dien tich: " + str(float(c1_entry.get())* float(c2_entry.get()))))
    button_cal1.pack()
    button_cal2 = tk.Button(sub_win, text = "Chu vi", command= lambda:cv.config(text="Chu vi: " + str(float(c1_entry.get())+ float(c2_entry.get()), float(c3_entry.get()))))
    button_cal2.pack()
    
        
    
    

win = tk.Tk()
win.title("Hinh hoc co ban")
win.geometry("400x500")
rect_button = tk.Button(win, text = "Tinh dien tich hinh phang", command = open_rect_win)
rect_button.pack()
rect_button = tk.Button(win, text = "Tinh dien tich hinh phang", command = open_triangle_win)
rect_button.pack()
rect_button = tk.Button(win, text = "Tinh dien tich hinh phang", command = open_rect_win)
rect_button.pack()
rect_button = tk.Button(win, text = "Tinh dien tich hinh phang", command = open_rect_win)
rect_button.pack()
win.mainloop()




