import tkinter as tk
class ToDoListGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x300")

        self.tasks = []

        # Create GUI elements
        self.label = tk.Label(self, text="To-Do List", font=("Arial", 16))
        self.label.pack(pady=10)

        self.task_entry = tk.Entry(self)
        self.task_entry.pack()

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_list = tk.Listbox(self, height=10, selectmode=tk.SINGLE)
        self.task_list.pack(pady=10)

        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

        # Bind events
        self.task_list.bind("<Double-1>", self.mark_as_done)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index[0])
            del self.tasks[selected_index[0]]

    def mark_as_done(self, event):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.task_list.get(selected_index[0])
            self.task_list.delete(selected_index[0])
            self.task_list.insert(tk.END, f"✅ {task}")

if __name__ == "__main__":
    app = ToDoListGUI()
    app.mainloop()
