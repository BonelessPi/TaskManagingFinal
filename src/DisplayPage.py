from util import *

class DisplayPage(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.taskListDict = {}
        self.refresh_tasks()

    def refresh_tasks_by_status(self, status):
        for label in self.taskListDict.setdefault(status, []):
            label.destroy()
        open_tasks = self.parent.db_manager.get_tasks_by_status(status)
        column = self.get_column_for_status(status)
        row = 0
        for task in open_tasks:
            info = self.format_task_string(task)
            task_label = ttk.Label(self, text=info)
            task_label.grid(row=row, column=column, padx=15, pady=5, sticky='w')
            self.taskListDict[status].append(task_label)
            row += 1
    
    def get_column_for_status(self, status):
        status_tuple_list = self.parent.db_manager.get_status()
        status_tuple_list.sort(key=lambda x:x[0])
        columns = {s:i for i,(_,s) in enumerate(status_tuple_list)}
        return columns.get(status, len(status_tuple_list)+1)
    
    def refresh_tasks(self):
        for _,status in self.parent.db_manager.get_status():
            self.refresh_tasks_by_status(status)
    
    def format_task_string(self, task):
        i,s,n = task._id,task.status,task.displayname
        NAME_MAX_CHARACTERS_SHOWN = 30
        n = n[:NAME_MAX_CHARACTERS_SHOWN] + (len(n)>NAME_MAX_CHARACTERS_SHOWN)*'...'
        return f"Task ID: {i},\n Status: {s},\n Name: {n}\n"

    @staticmethod
    def get_tab_name():
        return "Display Tasks"