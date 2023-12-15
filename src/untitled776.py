import tkinter as tk
from tkinter import ttk
from taskdbmanager import TaskDBManager  


        
    def display_comments(self, task_id):
        comments = self.db_manager.get_comments_by_task(task_id)
        
        for comment in comments:
                
                comment_text = f"Comment: {comment.content}\n"
                comment_label = tk.Label(self.LookUp, text=comment_text)
                comment_label.pack(side = 'right')
    
    def show_task_by_id(self):
        taskId = self.task_id_entry.get()
        task = self.db_manager.get_task_by_id(taskId)
        
        
        task_details_text = f"Task ID: {task._id}\nDisplay Name: {task.displayname}\nDescription: {task.description}\nStatus: {task.status}"
        task_details_label = tk.Label(self.LookUp, text=task_details_text)
        task_details_label.pack()
        self.updateTask(task)
        self.display_comments(taskId)
        self.createComments(taskId)
    def updateTask(self,task):
        self.name_label = tk.Label(self.LookUp, text="TaskName:")
        self.name_label.pack()
        self.taskName = tk.Entry(self.LookUp)
        self.taskName.pack()
        self.name_label = tk.Label(self.LookUp, text="Decsription:")
        self.name_label.pack()
        self.taskDescription = tk.Entry(self.LookUp)
        self.taskDescription.pack()
        self.name_label = tk.Label(self.LookUp, text="Status:")
        self.name_label.pack()
        self.status_enter = tk.Entry(self.LookUp)
        self.status_enter.pack()
        task.displayname = self.taskName.get()
        task.description = self.taskDescription.get()
        task.status = self.status_enter.get()
        self.updateTaskButton = tk.Button(self.LookUp, text="Update", command=lambda: self.db_manager.update_task(task))
        self.updateTaskButton.pack()

    
        
    def createComments(self,taskID):
        
        self.Id = tk.Label(self.createTask, text="EmplyoeeId:")
        self.Id.pack()
        self.Id = tk.Entry(self.createTask)
        self.Id.pack()
        
        self.comment = tk.Label(self.createTask, text="Comment:")
        self.comment.pack()
        self.comment = tk.Entry(self.createTask)
        self.comment.pack()

        

       

 
        self.add_task_button = tk.Button(self.createTask, text="Add Task", command=self.add_comment)
        self.add_task_button.pack()
    

    
        

    def add_task(self):
        issue = self.task_issue.get()
        description = self.task_description.get()
        status = self.task_status.get()
        
        self.db_manager.insert_task(issue, description, status)
        print("Task added!")
    def add_comment(self,taskId):
        employee = int(self.Id.get())
        task = taskId
        comment = self.comment.get()
        
        self.db_manager.insert_comment(employee,task, comment)
        print("Comment added!")
     
root = tk.Tk()
app = MyApp(root)
root.mainloop()
