from util import *
from DisplayPage import DisplayPage
#from CreatePage import CreatePage
#from LookupPage import LookupPage
from taskdbmanager import TaskDBManager

class MyApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Task Database Manager")

        self.db_manager = TaskDBManager()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        # initializing frames to an empty array
        self.frames = {} 

        for F in (DisplayPage, ):#CreatePage, LookupPage):
            frame = F(self)
            self.frames[F] = frame
            self.notebook.add(frame, text=frame.get_tab_name())
        self.notebook.bind("<<NotebookTabChanged>>", self.tabChange)

    def tabChange(self,event):
        tab = self.notebook.tab(self.notebook.select(), "text")
        if tab == 'Tasks':
            self.frames[DisplayPage].refresh_tasks()

    # def show_display_page(self):
    #     self.show_frame(DisplayPage)
    # def show_create_page(self):
    #     self.show_frame(CreatePage)
    # def show_lookup_page(self):
    #     self.show_frame(LookupPage)
    # def show_frame(self, cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()
        
    # tab = ttk.Frame(self.notebook)
    # self.notebook.add(tab, text='Display Tasks')
        

# Driver Code
app = MyApp()
app.mainloop()


# class MyApp(tk.Tk):
#     def __init__(self, root):
#         self.root = root
        

    
#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.pack(fill='both', expand=True)
#         '''
#         self.lookup_task_button = tk.Button(self.main_frame, text="Look Up Task by ID", command=self.lookup_task_page)
#         self.lookup_task_button.pack()

#         self.create_task_button = tk.Button(self.main_frame, text="Create New Task", command=self.create_task_page)
#         self.create_task_button.pack()
#         '''
      

#         #creates the tasks tab
#         self.tasks = tk.Frame(self.notebook)
#         self.notebook.add(self.tasks, text='Tasks')
        
       
#         '''
#         name_label = tk.Label(tab1, text="Name:", background="#6495ED", foreground="white")
#         name_label.pack()
#         name_entry = tk.Entry(tab1)
#         name_entry.pack()
#         '''
        
#         #creates create task tab
#         '''
#         self.createTask = tk.Frame(self.notebook)
#         self.notebook.add(self.createTask, text='Create Tasks')
#         '''
#         self.createTaskPage()
        
        
#         #creates the look up panel
#         self.createLookUpPage()
#         '''
#         self.LookUp = tk.Frame(self.notebook)
#         self.notebook.add(self.LookUp, text='LookUp tasks')
#         self.name_label = tk.Label(self.LookUp, text="TaskID:")
#         self.name_label.pack()
#         self.task_id_entry = tk.Entry(self.LookUp)
#         self.task_id_entry.pack()
#         self.create_task_button = tk.Button(self.LookUp, text="Look Up", command=self.show_task_by_id)
#         self.create_task_button.pack()
#         self.comments_text = tk.Text(self.LookUp,)
#         self.comments_text.pack(side ='right')
#         '''
#     def createLookUpPage(self):
#         self.LookUp = tk.Frame(self.notebook)
#         self.notebook.add(self.LookUp, text='LookUp tasks')
#         self.name_label = tk.Label(self.LookUp, text="TaskID:")
#         self.name_label.pack()
#         self.task_id_entry = tk.Entry(self.LookUp)
#         self.task_id_entry.pack()
#         self.create_task_button = tk.Button(self.LookUp, text="Look Up", command=self.show_task_by_id)
#         self.create_task_button.pack()
    

#     def createTaskPage(self):
#         self.createTask = tk.Frame(self.notebook)
#         self.notebook.add(self.createTask, text='Create Tasks')
#         self.task_issue = tk.Label(self.createTask, text="Issue:")
#         self.task_issue.pack()
#         self.task_issue = tk.Entry(self.createTask)
#         self.task_issue.pack()

#         self.task_description = tk.Label(self.createTask, text="Description:")
#         self.task_description.pack()
#         self.task_description = tk.Entry(self.createTask)
#         self.task_description.pack()

#         self.task_status = tk.Label(self.createTask, text="Status:")
#         self.task_status.pack()
#         self.task_status = tk.Entry(self.createTask)
#         self.task_status.pack()

 
#         self.add_task_button = tk.Button(self.createTask, text="Add Task", command=self.add_task)
#         self.add_task_button.pack()
#     def lookup_task_page(self):
#         lookupWin = tk.Toplevel(self.root)
#         lookup_task_frame = tk.Frame(lookupWin)
#         lookup_task_frame.pack()