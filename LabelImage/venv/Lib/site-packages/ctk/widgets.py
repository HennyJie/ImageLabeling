from ctk import CtkFrame
from imports import tk, ttk

class AutoScrollbar(tk.Scrollbar):
    ''' a scrollbar that will disappear when not needed '''
    def set(self, lo, hi):
        # if this is getting set to the whole size, hide since we can't scroll anyways
        if float(lo) == 0 and float(hi) == 1.0:
            self.grid_remove()
        else:
            self.grid()
        tk.Scrollbar.set(self, lo, hi)

class ScrollableText(CtkFrame):
    '''
    a widget that contains a text with a vertical (auto) scrollbar
    '''
    def __init__(self, *args, **kwargs):
        CtkFrame.__init__(self, *args, **kwargs)

        self.addWidget(AutoScrollbar, name="scrollY", x=1, y=0, gridKwargs={"sticky" : tk.NS})
        self.addWidget(tk.Text, name="text", x=0, y=0, yscrollcommand=self.scrollY.set, gridKwargs={"sticky" : tk.NSEW})
        self.scrollY.config(command=self.text.yview)
        self.expandColumn(0) # expand text
        self.expandRow(0) # expand text

    def clearText(self):
        ''' helper to clear the text '''
        self.text.delete(1.0, tk.END)
        self.update_idletasks()

    def appendText(self, txt):
        ''' helper to append text '''
        self.text.insert(tk.END, txt)
        self.update_idletasks()
        self.text.see(tk.END)

    def getText(self):
        ''' helper to get the text '''
        return self.text.get(1.0, tk.END)

    def setText(self, txt):
        ''' helper to set the text '''
        self.clearText()
        self.appendText(txt)
        self.update_idletasks()