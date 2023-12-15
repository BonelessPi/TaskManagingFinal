from util import *

# second window frame page1 
class Page1(tk.Frame):
    
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)


    def show_tasks_by_status(self, status):
        open_tasks = self.db_manager.get_tasks_by_status(status)
        column = self.get_column_for_status(status)
        row = 0
        for task in open_tasks:
            info = f"Task ID: {task._id}\n, Status: {task.status}\n, Name: {task.displayname}\n"
            task_label = tk.Label(self.tasks, text=info)
            task_label.grid(row=row, column=column)
            row += 1
    
    def get_column_for_status(self, status):
        columns = {
            "TODO": 0,
            "In Progress": 1,
            "Paused": 2,
            "Finished": 3,
            "Canceled": 4
        }
        return columns.get(status, 0)
    '''
    def show_tasks_by_status(self, status):
        #for label in self.tasksList:
        #    label.destroy()
        open_tasks = self.db_manager.get_tasks_by_status(status)
        for task in open_tasks:
            info =  f"Task ID: {task._id}\n, Status: {task.status}\n, Name: {task.displayname}\n"
            task_label = tk.Label(self.tasks, text=info)
            task_label.pack(side = 'left')
            self.tasksList.append(task_label)
    '''
    def refresh_tasks(self):
        self.show_tasks_by_status("TODO")
        self.show_tasks_by_status("In Progress")
        self.show_tasks_by_status("Paused")
        self.show_tasks_by_status("Finished")
        self.show_tasks_by_status("Canceled")

    tasksList = []
    def callTasks(self):
        for label in self.tasksList:
            label.destroy()
        self.refresh_tasks()