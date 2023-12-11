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
        taskWindow = tk.Toplevel(self.root)
        create_task_frame = tk.Frame(taskWindow)
        create_task_frame.pack()
        self.task_issue = tk.Label(taskWindow, text="Issue:")
        self.task_issue.pack()
        self.task_issue = tk.Entry(taskWindow)
        self.task_issue.pack()

        self.task_description = tk.Label(taskWindow, text="Description:")
        self.task_description.pack()
        self.task_description = tk.Entry(taskWindow)
        self.task_description.pack()

        self.task_status = tk.Label(taskWindow, text="Status:")
        self.task_status.pack()
        self.task_status = tk.Entry(taskWindow)
        self.task_status.pack()

 
        self.add_task_button = tk.Button(taskWindow, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
        
        
   
    
    tasks = []
    def show_open_tasks(self):
       for label in self.tasks:
            label.destroy()
       open_tasks = self.db_manager.get_tasks_by_status("TODO")
       for task in open_tasks:
            info =  f"Task ID: {task._id}, Status: {task.status}, Name: {task.displayname}"
            task_label = tk.Label(self.main_frame, text=info)
            task_label.pack()
            self.tasks.append(task_label)
       
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
