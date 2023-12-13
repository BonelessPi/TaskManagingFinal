import tkinter as tk
from tkinter import ttk
from taskdbmanager import TaskDBManager  

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Database Manager")

        self.db_manager = TaskDBManager()

        #self.main_frame = tk.Frame(self.root)
        #self.main_frame.pack()
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        '''
        self.lookup_task_button = tk.Button(self.main_frame, text="Look Up Task by ID", command=self.lookup_task_page)
        self.lookup_task_button.pack()

        self.create_task_button = tk.Button(self.main_frame, text="Create New Task", command=self.create_task_page)
        self.create_task_button.pack()
        '''
      

        
        self.tasks = tk.Frame(self.notebook)
        self.notebook.add(self.tasks, text='Tasks')
        self.notebook.bind("<<NotebookTabChanged>>", self.tabChange)
        # Name label and entry on the first tab
        '''
        name_label = tk.Label(tab1, text="Name:", background="#6495ED", foreground="white")
        name_label.pack()
        name_entry = tk.Entry(tab1)
        name_entry.pack()
        '''
        
        
        self.createTask = tk.Frame(self.notebook)
        self.notebook.add(self.createTask, text='Create Tasks')
        self.create_task_page()
        
        
        
        
        self.LookUp = tk.Frame(self.notebook)
        self.notebook.add(self.LookUp, text='LookUp tasks')
        self.name_label = tk.Label(self.LookUp, text="TaskID:")
        self.name_label.pack()
        self.task_id_entry = tk.Entry(self.LookUp)
        self.task_id_entry.pack()
        self.create_task_button = tk.Button(self.LookUp, text="Look Up", command=self.show_task_by_id)
        self.create_task_button.pack()
        self.comments_text = tk.Text(self.LookUp,)
        self.comments_text.pack(side ='right')
        
    def tabChange(self,event):
        #print(tab,self.tasks,tab is self.tasks)
        #print(dir(tab),type(tab),dir(self.tasks),type(self.tasks))

        tab = self.notebook.tab(self.notebook.select(), "text")
        if tab == 'Tasks':
            self.callTasks()
        
    def display_comments(self, task_id):
        comments = self.db_manager.get_comments_by_task(task_id)
        
        for comment in comments:
                
                comment_text = f"Comment: {comment.content}\n"
                comment_label = tk.Label(self.LookUp, text=comment_text)
                comment_label.pack()
       
    def callTasks(self):
        for label in self.tasksList:
            label.destroy()
        self.refresh_tasks()
    def show_task_by_id(self):
        taskId = self.task_id_entry.get()
        task = self.db_manager.get_task_by_id(taskId)
    
        
        task_details_text = f"Task ID: {task._id}\nDisplay Name: {task.displayname}\nDescription: {task.description}\nStatus: {task.status}"
        task_details_label = tk.Label(self.LookUp, text=task_details_text)
        task_details_label.pack()
        self.display_comments(taskId)

    def create_task_page(self):
        self.task_issue = tk.Label(self.createTask, text="Issue:")
        self.task_issue.pack()
        self.task_issue = tk.Entry(self.createTask)
        self.task_issue.pack()

        self.task_description = tk.Label(self.createTask, text="Description:")
        self.task_description.pack()
        self.task_description = tk.Entry(self.createTask)
        self.task_description.pack()

        self.task_status = tk.Label(self.createTask, text="Status:")
        self.task_status.pack()
        self.task_status = tk.Entry(self.createTask)
        self.task_status.pack()

 
        self.add_task_button = tk.Button(self.createTask, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
        
    
    tasksList = []
    def show_tasks_by_status(self, status):
        #for label in self.tasksList:
        #    label.destroy()
        open_tasks = self.db_manager.get_tasks_by_status(status)
        for task in open_tasks:
            info =  f"Task ID: {task._id}\n, Status: {task.status}\n, Name: {task.displayname}\n"
            task_label = tk.Label(self.tasks, text=info)
            task_label.pack(side = 'left')
            self.tasksList.append(task_label)
    
    def refresh_tasks(self):
        self.show_tasks_by_status("TODO")
        self.show_tasks_by_status("In Progress")
        self.show_tasks_by_status("Paused")
        self.show_tasks_by_status("Finished")
        self.show_tasks_by_status("Canceled")
       
    def lookup_task_page(self):
        lookupWin = tk.Toplevel(self.root)
        lookup_task_frame = tk.Frame(lookupWin)
        lookup_task_frame.pack()
        

    def add_task(self):
        issue = self.task_issue.get()
        description = self.task_description.get()
        status = self.task_status.get()
        
        self.db_manager.insert_task(issue, description, status)
        print("Task added!")
    def add_comment(self):
        employee = int(self.comment_employee.get())
        task = int(self.taskID.get())
        comment = self.comment.get()
        
        self.db_manager.insert_comment(employee,task, comment)
        print("Comment added!")
     
root = tk.Tk()
app = MyApp(root)
root.mainloop()
