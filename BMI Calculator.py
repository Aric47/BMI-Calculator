import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()

        height_meters = height / 100

        bmi = weight / (height_meters ** 2)

        normal_range = (18.5, 24.9, 29.9, 30)

        if normal_range[0] <= bmi <= normal_range[1]:
            health_status = "Normal Weight, keep it up"
        elif normal_range[1] <= bmi <= normal_range[2]:
            health_status = "Overweight"
        elif normal_range[2] <= bmi <= normal_range[3]:
            health_status = "You're Overweight"
        elif normal_range[3] <= bmi:
            health_status = "You're obese"
        else:
            health_status = "You're underweight"

        result_label.config(text=f"Your BMI is: {bmi:.2f}\n{health_status}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for height, weight, and age.")

window = tk.Tk()
window.title("BMI Calculator by Alric")

window.geometry("320x300")
window.resizable(False, False)
window.configure(bg="#2C3E50")

font_style = ("Poppins", 12)

entry_style = ttk.Style()
entry_style.configure("TEntry",
                      fieldbackground="white",
                      bordercolor="#2C3E50",
                      borderwidth=5,
                      relief="flat",
                      font=font_style)

title_label = tk.Label(window, text="BMI CALCULATOR", font=("Poppins", 16, "bold"), bg="#2C3E50", fg="white")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

age_label = tk.Label(window, text="Age:", font=font_style, bg="#2C3E50", fg="white")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
age_entry = ttk.Entry(window, font=font_style)
age_entry.grid(row=1, column=1, padx=10, pady=5)

height_label = tk.Label(window, text="Height (cm):", font=font_style, bg="#2C3E50", fg="white")
height_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
height_entry = ttk.Entry(window, font=font_style)
height_entry.grid(row=2, column=1, padx=10, pady=5)

weight_label = tk.Label(window, text="Weight (kg):", font=font_style, bg="#2C3E50", fg="white")
weight_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
weight_entry = ttk.Entry(window, font=font_style)
weight_entry.grid(row=3, column=1, padx=10, pady=5)

gender_label = tk.Label(window, text="Gender:", font=font_style, bg="#2C3E50", fg="white")
gender_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

gender_var = tk.StringVar()
gender_var.set("Male")

male_radiobutton = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", font=font_style, bg="#2C3E50")
male_radiobutton.grid(row=4, column=1, padx=5, pady=5, sticky="e")

female_radiobutton = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", font=font_style, bg="#2C3E50")
female_radiobutton.grid(row=4, column=0, columnspan=2, pady=10)

style = ttk.Style()
style.configure("TButton", font=font_style)

result_label = tk.Label(window, text="", font=font_style, bg="#2C3E50", fg="white")
result_label.grid(row=6, column=0, columnspan=2)

calculate_button = ttk.Button(window, text="Calculate BMI", style="TButton", command=calculate_bmi)
calculate_button.grid(row=7, column=0, columnspan=2, pady=10)

window.mainloop()
