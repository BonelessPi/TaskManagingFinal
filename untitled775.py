import tkinter as tk
from taskdbmanager import ForumDBManager  

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Forum Database Manager")

        self.db_manager = ForumDBManager()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.lookup_task_button = tk.Button(self.main_frame, text="Look Up Task by ID", command=self.lookup_task_page)
        self.lookup_task_button.pack()

        self.create_task_button = tk.Button(self.main_frame, text="Create New Task", command=self.create_task_page)
        self.create_task_button.pack()

        self.open_tasks_button = tk.Button(root, text="Show Open Tasks", command=self.show_open_tasks)
        self.open_tasks_button.pack()
    def create_task_page(self):
        new_window = tk.Toplevel(self.root)
        create_task_frame = tk.Frame(new_window)
        create_task_frame.pack()
        
    def show_open_tasks(self):
         open_tasks = self.db_manager.get_tasks_by_status("TODO")
         for task in open_tasks:
             print(task)

    def lookup_task_page(self):
        new_window = tk.Toplevel(self.root)
        lookup_task_frame = tk.Frame(new_window)
        lookup_task_frame.pack()

     
root = tk.Tk()
app = MyApp(root)
root.mainloop()
