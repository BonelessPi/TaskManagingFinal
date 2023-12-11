from util import *
from startpage import StartPage
from page1 import Page1
from page2 import Page2

class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text='Tab 1')
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text='Tab 2')

        name_label = tk.Label(tab1, text="Name:", background="#6495ED", foreground="white")
        name_label.pack()
        name_entry = tk.Entry(tab1)
        name_entry.pack()

        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {} 

        for F in (StartPage, Page1, Page2):
            frame = F(container)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)

        menubar = tk.Menu(self)
        file = tk.Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Pages', menu = file) 
        file.add_command(label ='Start', command = self.show_start_page) 
        file.add_command(label ='Page1', command = self.show_page1) 
        file.add_command(label ='Page2', command = self.show_page2)
        self.config(menu=menubar)

    def show_start_page(self):
        self.show_frame(StartPage)
    def show_page1(self):
        self.show_frame(Page1)
    def show_page2(self):
        self.show_frame(Page2)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Driver Code
app = tkinterApp()
app.mainloop()
