from util import *

# second window frame page1 
class Page1(tk.Frame):
    
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)


