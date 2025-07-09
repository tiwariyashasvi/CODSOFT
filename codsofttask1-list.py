import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List") # Simplified window title as we'll use a label for the main title
        master.geometry("500x600") # Set initial window size
        master.resizable(True, True) # Allow window resizing

        # Configure grid for responsiveness
        master.grid_rowconfigure(0, weight=0) # Title Label
        master.grid_rowconfigure(1, weight=0) # Input frame
        master.grid_rowconfigure(2, weight=1) # Listbox frame
        master.grid_rowconfigure(3, weight=0) # Button frame (for Mark Complete, Edit)
        master.grid_rowconfigure(4, weight=0) # New Button frame (for Delete, Clear All)
        master.grid_columnconfigure(0, weight=1)

        self.tasks = []

        # --- Title Label ---
        # Made the title even bolder by increasing font size
        self.title_label = tk.Label(master, text="My To-Do List", font=("Arial", 30, "bold"), pady=10) # Increased font size to 30
        self.title_label.grid(row=0, column=0, sticky="ew")

        # --- Input Frame ---
        self.input_frame = tk.Frame(master, padx=10, pady=10)
        self.input_frame.grid(row=1, column=0, sticky="ew") # Moved to row 1 after the title label
        self.input_frame.grid_columnconfigure(0, weight=1) # Entry field takes most space

        # Added black outline to the Entry field
        self.task_entry = tk.Entry(self.input_frame, width=40, font=("Arial", 12),
                                   bd=1, relief="solid", highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.task_entry.grid(row=0, column=0, padx=(0, 0), pady=5, sticky="ew") # Entry at row 0, column 0
        self.task_entry.bind("<Return>", lambda event: self.add_task()) # Bind Enter key

        # Modified Add Task button: background black, text white, moved to row 1, reduced length
        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task, font=("Arial", 10), bg="black", fg="white", relief="raised", bd=2)
        # Removed sticky="ew" to reduce its length and centered it with columnconfigure
        self.add_button.grid(row=1, column=0, pady=5, sticky="n") # Changed sticky to "n" to center horizontally

        # --- Listbox Frame ---
        self.list_frame = tk.Frame(master, padx=10, pady=10)
        self.list_frame.grid(row=2, column=0, sticky="nsew") # Moved to row 2
        self.list_frame.grid_rowconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=1)

        # Added black outline to the Listbox
        self.task_listbox = tk.Listbox(self.list_frame, height=15, font=("Arial", 12), selectmode=tk.SINGLE,
                                       bd=2, relief="solid", highlightbackground="black", highlightcolor="black", highlightthickness=1) # Changed relief to solid and added highlight properties
        self.task_listbox.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical", command=self.task_listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # --- Button Frame for Mark Complete and Edit Task ---
        self.button_frame_row1 = tk.Frame(master, padx=10, pady=5) # Reduced pady for closer buttons
        self.button_frame_row1.grid(row=3, column=0, sticky="ew") # Moved to row 3
        self.button_frame_row1.grid_columnconfigure(0, weight=1)
        self.button_frame_row1.grid_columnconfigure(1, weight=1)

        # Changed button background to grey and text to black
        self.complete_button = tk.Button(self.button_frame_row1, text="Mark Complete", command=self.mark_complete, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
        self.complete_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Added Edit Task button
        self.edit_button = tk.Button(self.button_frame_row1, text="Edit Task", command=self.edit_task, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
        self.edit_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # --- Button Frame for Delete Task and Clear All ---
        self.button_frame_row2 = tk.Frame(master, padx=10, pady=5) # Reduced pady for closer buttons
        self.button_frame_row2.grid(row=4, column=0, sticky="ew") # New row 4 for these buttons
        self.button_frame_row2.grid_columnconfigure(0, weight=1)
        self.button_frame_row2.grid_columnconfigure(1, weight=1)

        self.delete_button = tk.Button(self.button_frame_row2, text="Delete Task", command=self.delete_task, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
        self.delete_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.clear_button = tk.Button(self.button_frame_row2, text="Clear All", command=self.clear_all_tasks, font=("Arial", 10), bg="grey", fg="black", relief="raised", bd=2)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")


        master.protocol("WM_DELETE_WINDOW", self.on_closing) # Handle window close event

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
                display_text = "✔ " + display_text # Add a checkmark for completed tasks
                self.task_listbox.insert(tk.END, display_text)
                self.task_listbox.itemconfig(tk.END, fg="gray") # Grey out completed tasks
            else:
                self.task_listbox.insert(tk.END, display_text)
                self.task_listbox.itemconfig(tk.END, fg="black") # Ensure uncompleted tasks are black

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            if 0 <= selected_index < len(self.tasks):
                self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"] # Toggle completion status
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark complete.")

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            if 0 <= selected_index < len(self.tasks):
                current_task_text = self.tasks[selected_index]["text"]

                # Create a new top-level window for editing
                edit_window = tk.Toplevel(self.master)
                edit_window.title("Edit Task")
                edit_window.geometry("300x100")
                edit_window.transient(self.master) # Make it appear on top of the main window
                edit_window.grab_set() # Disable interaction with the main window

                edit_label = tk.Label(edit_window, text="Edit Task:", font=("Arial", 10))
                edit_label.pack(pady=5)

                edit_entry = tk.Entry(edit_window, width=40, font=("Arial", 10))
                edit_entry.insert(0, current_task_text) # Pre-fill with current task text
                edit_entry.pack(pady=5)
                edit_entry.focus_set() # Set focus to the entry field

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

                edit_window.wait_window(edit_window) # Wait for the edit window to close
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
