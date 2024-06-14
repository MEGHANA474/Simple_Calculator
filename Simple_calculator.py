import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""
        self.entry_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry_frame = tk.Frame(self.root)
        entry_frame.pack()

        entry = tk.Entry(entry_frame, textvariable=self.entry_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sqrt',
            '1', '2', '3', '-', '^',
            '0', '.', '=', '+', 'M'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = tk.Button(buttons_frame, text=button, padx=20, pady=20, font=('Arial', 18), bd=5,
                                command=self.evaluate_expression)
            elif button == 'C':
                btn = tk.Button(buttons_frame, text=button, padx=20, pady=20, font=('Arial', 18), bd=5,
                                command=self.clear_expression)
            elif button == 'sqrt':
                btn = tk.Button(buttons_frame, text=button, padx=20, pady=20, font=('Arial', 18), bd=5,
                                command=self.sqrt_expression)
            elif button == '^':
                btn = tk.Button(buttons_frame, text=button, padx=20, pady=20, font=('Arial', 18), bd=5,
                                command=lambda: self.update_expression('**'))
            elif button == 'M':
                btn = tk.Button(buttons_frame, text=button, padx=20, pady=20, font=('Arial', 18), bd=5,
                                command=self.memory_store)
            else:
                btn = tk.Button(buttons_frame, text=button, padx=20, pady=20, font=('Arial', 18), bd=5,
                                command=lambda btn=button: self.update_expression(btn))

            btn.grid(row=row_val, column=col_val)

            col_val += 1
            if col_val == 5:
                col_val = 0
                row_val += 1

    def update_expression(self, value):
        self.expression += str(value)
        self.entry_text.set(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.entry_text.set("")

    def sqrt_expression(self):
        try:
            result = math.sqrt(float(self.expression))
            self.entry_text.set(result)
            self.expression = str(result)
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.entry_text.set(result)
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by Zero")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

    def memory_store(self):
        try:
            self.memory = eval(self.expression)
            messagebox.showinfo("Memory", f"Stored: {self.memory}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
