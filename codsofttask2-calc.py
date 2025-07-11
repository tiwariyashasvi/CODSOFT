from tkinter import *

def result():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == "+":
            output = num1 + num2
        elif op == "-":
            output = num1 - num2
        elif op == "*":
            output = num1 * num2
        elif op == "/":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            output = num1 / num2
        else:
            result_label.config(text="Select an operation")
            return

        result_label.config(text=f"Result: {output}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = Tk()
root.title("Simple Calculator - Task 2")
root.geometry("380x400")
root.resizable(False, False)

title = Label(root, text="CALCULATOR", font=("Arial", 20, "bold"), fg="brown")
title.pack(pady=10)

frame1 = Frame(root)
frame1.pack(pady=5)
Label(frame1, text="Enter First Number:").pack(side=LEFT, padx=5)
entry1 = Entry(frame1, highlightthickness=2, highlightbackground="brown", highlightcolor="brown")
entry1.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(pady=5)
Label(frame2, text="Enter Second Number:").pack(side=LEFT, padx=5)
entry2 = Entry(frame2, highlightthickness=2, highlightbackground="brown", highlightcolor="brown")
entry2.pack(side=LEFT)

Label(root, text="Select Operation:").pack(pady=5)
operator = StringVar()
operator.set("+")

operation_frame = Frame(root)
operation_frame.pack(pady=5)

for op in ["+", "-", "*", "/"]:
    Radiobutton(
        operation_frame, text=op, variable=operator, value=op,
        font=("Arial", 12), indicatoron=0, width=4, padx=10, pady=5,
        relief="solid", bd=2, highlightbackground="brown", highlightcolor="brown", background="white"
    ).pack(side=LEFT, padx=5)

Button(
    root, text="Show Result", font=("Arial", 12, "bold"),
    bg="black", fg="white", activebackground="grey", activeforeground="white",
    command=result
).pack(pady=15)

result_label = Label(root, text="Result will be shown here", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
