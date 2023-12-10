import tkinter as tk
from taskdbmanager import ForumDBManager  

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Forum Database Manager")

      
        self.db_manager = ForumDBManager()

     
        self.task_displayname_label = tk.Label(root, text="Display Name:")
        self.task_displayname_label.pack()
        self.task_displayname_entry = tk.Entry(root)
        self.task_displayname_entry.pack()

        self.task_description_label = tk.Label(root, text="Description:")
        self.task_description_label.pack()
        self.task_description_entry = tk.Entry(root)
        self.task_description_entry.pack()

        self.task_status_label = tk.Label(root, text="Status:")
        self.task_status_label.pack()
        self.task_status_entry = tk.Entry(root)
        self.task_status_entry.pack()

 
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

 
        self.comment_author_label = tk.Label(root, text="Author ID:")
        self.comment_author_label.pack()
        self.comment_author_entry = tk.Entry(root)
        self.comment_author_entry.pack()

        self.comment_task_label = tk.Label(root, text="Task ID:")
        self.comment_task_label.pack()
        self.comment_task_entry = tk.Entry(root)
        self.comment_task_entry.pack()

        self.comment_content_label = tk.Label(root, text="Content:")
        self.comment_content_label.pack()
        self.comment_content_entry = tk.Entry(root)
        self.comment_content_entry.pack()

       
        self.add_comment_button = tk.Button(root, text="Add Comment", command=self.add_comment)
        self.add_comment_button.pack()

    def add_task(self):
        displayname = self.task_displayname_entry.get()
        description = self.task_description_entry.get()
        status = self.task_status_entry.get()
        
        self.db_manager.insert_task(displayname, description, status)
        print("Task added!")

    def add_comment(self):
        author = int(self.comment_author_entry.get())
        task = int(self.comment_task_entry.get())
        content = self.comment_content_entry.get()
        
        self.db_manager.insert_comment(author, task, content)
        print("Comment added!")


root = tk.Tk()
app = MyApp(root)
root.mainloop()