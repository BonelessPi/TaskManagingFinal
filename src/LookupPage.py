from util import *

class LookupPage(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.commentList = []

        self.task_label = ttk.Label(self, text="Task:")
        self.task_label.grid(row=0,column =0)
        self.task_clicked = tk.StringVar()
        self.task_dropdown = ttk.OptionMenu(self, self.task_clicked, None, [], command=self.load_task)
        self.task_dropdown.grid(row = 0,column = 1)

        self.displayname_label = ttk.Label(self, text="Name:")
        self.displayname_label.grid(row = 1, column = 0)
        self.displayname_entry = ttk.Entry(self)
        self.displayname_entry.grid(row = 1, column = 1, sticky='WE')

        self.description_label = ttk.Label(self, text="Description:")
        self.description_label.grid(row = 2, column = 0)
        self.description_entry = ttk.Entry(self)
        self.description_entry.grid(row = 2, column = 1, sticky='WE')

        self.task_status = ttk.Label(self, text="Status:")
        self.task_status.grid(row = 3, column = 0)
        options = [s for _,s in self.parent.db_manager.get_status()]
        self.status_clicked = tk.StringVar()
        self.status_dropdown = ttk.OptionMenu(self, self.status_clicked, None, *options)
        self.status_dropdown.grid(row = 3, column = 1)

        self.update_task_button = ttk.Button(self, text="Update", command=self.update_task)
        self.update_task_button.grid(row = 4, column = 0)

        space_label = ttk.Label(self, text="")
        space_label.grid(row = 5)

        self.employeeid_label = ttk.Label(self, text="EmployeeId:")
        self.employeeid_label.grid(row = 6, column = 0)
        self.employee_clicked = tk.StringVar()
        self.employee_dropdown = ttk.OptionMenu(self, self.employee_clicked, "Select an employee...", [])
        self.employee_dropdown.grid(row = 6,column = 1)

        self.comment_label = ttk.Label(self, text="Comment:")
        self.comment_label.grid(row = 7, column = 0)
        self.comment_entry = ttk.Entry(self)
        self.comment_entry.grid(row = 7, column = 1)
        self.add_comment_button = ttk.Button(self, text="Add Comment", command=self.add_comment)
        self.add_comment_button.grid(row = 8, column = 0)

        self.refresh_menu()
    
    def format_task_string(self, task):
        i,n,d = task._id,task.displayname,task.description
        NAME_MAX_CHARACTERS_SHOWN = 30
        n = n[:NAME_MAX_CHARACTERS_SHOWN] + (len(n)>NAME_MAX_CHARACTERS_SHOWN)*'...'
        d = d[:NAME_MAX_CHARACTERS_SHOWN] + (len(d)>NAME_MAX_CHARACTERS_SHOWN)*'...'
        return f"Task ID: {i}; Name: {n}; Desc: {d}"

    def refresh_menu(self):
        self.task_dict = {self.format_task_string(task):task for task in self.parent.db_manager.get_tasks()}
        self.task_dropdown.set_menu(None, *self.task_dict.keys())
        self.task_clicked.set("Select a task...")
        self.displayname_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.status_clicked.set("")
        self.employee_dict = {str(employee):employee for employee in self.parent.db_manager.get_employees()}
        self.employee_dropdown.set_menu(None, *self.employee_dict.keys())
        self.displayname_entry["state"] = tk.DISABLED
        self.description_entry["state"] = tk.DISABLED
        self.status_dropdown["state"] = tk.DISABLED
        self.update_task_button["state"] = tk.DISABLED
        self.add_comment_button["state"] = tk.DISABLED
        self.clear_comments()

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
        self.add_comment_button["state"] = tk.NORMAL
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
        self.clear_comments()
        comments = self.parent.db_manager.get_comments_by_task(task_id)
        count = 0
        for comment in comments:
            authorname = self.parent.db_manager.get_employee_by_id(comment.authorid).name
            comment_text = f"{authorname}: {comment.content}\n"
            comment_label = ttk.Label(self, text=comment_text)
            comment_label.grid(row = count, column = 2, sticky='W', padx=10)
            self.commentList.append(comment_label)
            count += 1
    
    def clear_comments(self):
        for label in self.commentList:
            label.destroy()
    
    def add_comment(self):
        employee = self.employee_dict[self.employee_clicked.get()]._id
        task_id = self.task_dict[self.task_clicked.get()]._id
        comment = self.comment_entry.get()
        self.parent.db_manager.insert_comment(employee, task_id, comment)
        self.display_comments(task_id)
        
    @staticmethod
    def get_tab_name():
        return "Lookup/Update Task"
    