from util import *

class CreatePage(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        self.displayname_label = ttk.Label(self, text="Name:")
        self.displayname_label.pack()
        self.displayname_entry = ttk.Entry(self, width=50)
        self.displayname_entry.pack()

        self.description_label = ttk.Label(self, text="Description:")
        self.description_label.pack()
        self.description_entry = ttk.Entry(self, width=50)
        self.description_entry.pack()

        self.task_status = ttk.Label(self, text="Status:")
        self.task_status.pack()
        options = [s for _,s in self.parent.db_manager.get_status()]
        self.clicked = tk.StringVar()
        self.status_dropdown = ttk.OptionMenu(self, self.clicked, options[0], *options)
        self.status_dropdown.pack()

        space_label = ttk.Label(self, text="")
        space_label.pack()

        self.add_task_button = ttk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
    
    def add_task(self):
        issue = self.displayname_entry.get()
        description = self.description_entry.get()
        status = self.clicked.get()
        
        self.parent.db_manager.insert_task(issue, description, status)

    @staticmethod
    def get_tab_name():
        return "Create New Task"