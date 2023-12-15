from util import *

class DisplayPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
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
            info = f"Task ID: {task._id},\n Status: {task.status},\n Name: {task.displayname}\n"
            task_label = tk.Label(self, text=info)
            task_label.grid(row=row, column=column, padx=15, pady=5)
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

    @staticmethod
    def get_tab_name():
        return "Display Tasks"