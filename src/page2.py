from util import *

# third window frame page2
class Page2(tk.Frame): 
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
