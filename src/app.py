from util import *
from DisplayPage import DisplayPage
from CreatePage import CreatePage
from LookupPage import LookupPage
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

        for F in (DisplayPage, CreatePage, LookupPage):
            frame = F(self)
            self.frames[F] = frame
            self.notebook.add(frame, text=F.get_tab_name())
        self.notebook.bind("<<NotebookTabChanged>>", self.tabChange)

    def tabChange(self,event):
        tab = self.notebook.tab(self.notebook.select(), "text")
        if tab == DisplayPage.get_tab_name():
            self.frames[DisplayPage].refresh_tasks()
        elif tab == LookupPage.get_tab_name():
            self.frames[LookupPage].refresh_menu()

# Driver Code
app = MyApp()
app.mainloop()
