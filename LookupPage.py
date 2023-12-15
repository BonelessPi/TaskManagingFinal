from util import *

class LookupPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent


        self.task_label = tk.Label(self, text="Task:")
        self.task_label.grid(row=0,column =0)
        self.task_clicked = tk.StringVar()
        self.task_dropdown = ttk.OptionMenu(self, self.task_clicked, None, [], command=self.load_task)
        self.task_dropdown.grid(row = 0,colum = 1)

        self.displayname_label = tk.Label(self, text="Name:")
        self.displayname_label.grid(row = 1, column = 0)
        self.displayname_entry = tk.Entry(self)
        self.displayname_entry.grid(row = 1, column = 1)

        self.description_label = tk.Label(self, text="Description:")
        self.description_label.grid(row = 2, column = 0)
        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row = 2, column = 1)

        self.task_status = tk.Label(self, text="Status:")
        self.task_status.grid(row = 3, column = 0)
        options = [s for _,s in self.parent.db_manager.get_status()]
        self.status_clicked = tk.StringVar()
        self.status_dropdown = ttk.OptionMenu(self, self.status_clicked, None, *options)
        self.status_dropdown.grid(row = 3, column = 1)

        self.update_task_button = tk.Button(self, text="Update", command=self.update_task)
        self.update_task_button.grid(row = 4, column = 0)

        self.employeeid_label = tk.Label(self, text="EmployeeId:")
        self.employeeid_label.grid(row = 5, column = 0)
        self.Id = tk.Entry(self)
        self.Id.grid(row = 5, column = 1)
        self.comment = tk.Label(self, text="Comment:")
        self.comment.grid(row = 6, column = 0)
        self.comment = tk.Entry(self)
        self.comment.grid(row = 6, column = 1)

        # space_label = tk.Label(self, text="")
        # space_label.pack()

        # self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        # self.add_task_button.pack()

        self.refresh_menu()
    
    def refresh_menu(self):
        self.task_dict = {str(task):task for task in self.parent.db_manager.get_tasks()}
        self.task_dropdown.set_menu(None, *self.task_dict.values())
        self.task_clicked.set("Select a task...")
        self.displayname_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.status_clicked.set("")
        self.displayname_entry["state"] = tk.DISABLED
        self.description_entry["state"] = tk.DISABLED
        self.status_dropdown["state"] = tk.DISABLED
        self.update_task_button["state"] = tk.DISABLED

    def load_task(self,event):
        self.displayname_entry["state"] = tk.NORMAL
        self.description_entry["state"] = tk.NORMAL
        self.status_dropdown["state"] = tk.NORMAL
        self.update_task_button["state"] = tk.NORMAL
        task_obj = self.task_dict[self.task_clicked.get()]
        self.displayname_entry.delete(0, tk.END)
        self.displayname_entry.insert(0, task_obj.displayname)
        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, task_obj.description)
        self.status_clicked.set(task_obj.status)
        self.display_comments(task_obj._id)

    def update_task(self):
        displayname = self.displayname_entry.get()
        description = self.description_entry.get()
        status = self.status_clicked.get()
        task_obj = self.task_dict[self.task_clicked.get()]
        task_obj.displayname = displayname
        task_obj.description = description
        task_obj.status = status
        self.parent.db_manager.update_task(task_obj)

    def display_comments(self, task_id):
        comments = self.parent.db_manager.get_comments_by_task(task_id)
        count = 0
        for comment in comments:
            comment_text = f"Comment: {comment.content}\n"
            comment_label = tk.Label(self, text=comment_text)
            comment_label.grid(row = count, column = 2)
            count += 1

    @staticmethod
    def get_tab_name():
        return "Lookup/Update Task"
    