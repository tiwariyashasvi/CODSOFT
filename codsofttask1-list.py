import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List") 
        master.geometry("500x600") 
        master.resizable(True, True) 
    
        master.grid_rowconfigure(0, weight=0)
        master.grid_rowconfigure(1, weight=0) 
        master.grid_rowconfigure(2, weight=1) 
        master.grid_rowconfigure(3, weight=0) 
        master.grid_rowconfigure(4, weight=0) 
        master.grid_columnconfigure(0, weight=1)

        self.tasks = []

        
        
        self.title_label = tk.Label(master, text="My To-Do List", font=("Arial", 30, "bold"), pady=10) 
        self.title_label.grid(row=0, column=0, sticky="ew")

        
        self.input_frame = tk.Frame(master, padx=10, pady=10)
        self.input_frame.grid(row=1, column=0, sticky="ew") 
        self.input_frame.grid_columnconfigure(0, weight=1) 

    
        self.task_entry = tk.Entry(self.input_frame, width=40, font=("Arial", 12),
                                   bd=1, relief="solid", highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.task_entry.grid(row=0, column=0, padx=(0, 0), pady=5, sticky="ew") 
        self.task_entry.bind("<Return>", lambda event: self.add_task()) 

        
        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task, font=("Arial", 10), bg="black", fg="white", relief="raised", bd=2)
        
        self.add_button.grid(row=1, column=0, pady=5, sticky="n") 

        
        self.list_frame = tk.Frame(master, padx=10, pady=10)
        self.list_frame.grid(row=2, column=0, sticky="nsew") 
        self.list_frame.grid_rowconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=1)

        
        self.task_listbox = tk.Listbox(self.list_frame, height=15, font=("Arial", 12), selectmode=tk.SINGLE,
                                       bd=2, relief="solid", highlightbackground="black", highlightcolor="black", highlightthickness=1) 
        self.task_listbox.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical", command=self.task_listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        
        self.button_frame_row1 = tk.Frame(master, padx=10, pady=5) 
        self.button_frame_row1.grid(row=3, column=0, sticky="ew") 
        self.button_frame_row1.grid_columnconfigure(0, weight=1)
        self.button_frame_row1.grid_columnconfigure(1, weight=1)

        
        self.complete_button = tk.Button(self.button_frame_row1, text="Mark Complete", command=self.mark_complete, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
        self.complete_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        
        self.edit_button = tk.Button(self.button_frame_row1, text="Edit Task", command=self.edit_task, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
        self.edit_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        
        self.button_frame_row2 = tk.Frame(master, padx=10, pady=5) 
        self.button_frame_row2.grid(row=4, column=0, sticky="ew") 
        self.button_frame_row2.grid_columnconfigure(0, weight=1)
        self.button_frame_row2.grid_columnconfigure(1, weight=1)

        self.delete_button = tk.Button(self.button_frame_row2, text="Delete Task", command=self.delete_task, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
        self.delete_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.clear_button = tk.Button(self.button_frame_row2, text="Clear All", command=self.clear_all_tasks, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")


        master.protocol("WM_DELETE_WINDOW", self.on_closing) 

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            display_text = task["text"]
            if task["completed"]:
                display_text = "✔ " + display_text 
                self.task_listbox.insert(tk.END, display_text)
                self.task_listbox.itemconfig(tk.END, fg="gray") 
            else:
                self.task_listbox.insert(tk.END, display_text)
                self.task_listbox.itemconfig(tk.END, fg="black") 

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            if 0 <= selected_index < len(self.tasks):
                self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"] 
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark complete.")

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            if 0 <= selected_index < len(self.tasks):
                current_task_text = self.tasks[selected_index]["text"]

                
                edit_window = tk.Toplevel(self.master)
                edit_window.title("Edit Task")
                edit_window.geometry("300x100")
                edit_window.transient(self.master) 
                edit_window.grab_set() 

                edit_label = tk.Label(edit_window, text="Edit Task:", font=("Arial", 10))
                edit_label.pack(pady=5)

                edit_entry = tk.Entry(edit_window, width=40, font=("Arial", 10))
                edit_entry.insert(0, current_task_text) 
                edit_entry.pack(pady=5)
                edit_entry.focus_set() 

                def save_edit():
                    new_text = edit_entry.get().strip()
                    if new_text:
                        self.tasks[selected_index]["text"] = new_text
                        self.update_task_listbox()
                        edit_window.destroy()
                    else:
                        messagebox.showwarning("Warning", "Task cannot be empty!", parent=edit_window)

                save_button = tk.Button(edit_window, text="Save", command=save_edit, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
                save_button.pack(pady=5)

                edit_window.wait_window(edit_window) 
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            if 0 <= selected_index < len(self.tasks):
                del self.tasks[selected_index]
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_all_tasks(self):
        if messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all tasks?"):
            self.tasks = []
            self.update_task_listbox()

    def on_closing(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
