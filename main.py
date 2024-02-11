import wx
import wx.svg
import os
import sqlite3
from datetime import datetime
from omv_ui import frMain, dgColor, dgRecipe

os.environ['WXSUPPRESS_SIZER_FLAGS_CHECK'] = '1'

# Menghubungkan ke database
conn = sqlite3.connect('omv.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS operators (id INTEGER PRIMARY KEY, name TEXT)''')

conn.commit()

class frameMain(frMain):
    def __init__(self, parent):

        # Insiasi parent class
        frMain.__init__(self, parent)

        # Tanggal dan waktu bergerak
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateTime, self.timer)
        self.timer.Start(1000)

        # Inisasi kolom Recipes
        self.lcRecRecipes.InsertColumn(0, "Color")
        self.lcRecRecipes.InsertColumn(1, "Description 1", width=200)
        self.lcRecRecipes.InsertColumn(2, "Time 1")
        self.lcRecRecipes.InsertColumn(3, "Description 2", width=200)
        self.lcRecRecipes.InsertColumn(4, "Time 2")
        self.lcRecRecipes.InsertColumn(5, "Description 3", width=200)
        self.lcRecRecipes.InsertColumn(6, "Time 3")

        # Inisiasi Operators
        self.lcOpOperators.InsertColumn(0, "Name")
        self.btnOpRefreshOnClick(self)
        self.cbHomeOpUpdate()

    def updateTime(self, event):
        # Format tanggal dan waktu bergerak
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Update status bar yang di bawah
        self.sbMain.SetStatusText("Ready", 0)
        self.sbMain.SetStatusText("COM3", 1)
        self.sbMain.SetStatusText("BAUD 9600", 2)
        self.sbMain.SetStatusText(currentTime, 3)

#### KODE UNTUK TAB HOME
        
    def btnHomeColOnClick(self, event):
        # Buka dialog pilih warna
        dialog = dialogColor(self)
        if dialog.ShowModal() == wx.ID_OK:
            # Eksekusi pilih warna ketika OK
            pass
        dialog.Destroy()
        # No need to call event.Skip() unless you have a specific reason to continue event propagation
    
    def cbHomeOpUpdate(self):
        results = self.getOpNames()
        names = [item[0] for item in results]


#### KODE UNTUK TAB RECORDS 
        
#### KODE UNTUK TAB SUMMARY

#### KODE UNTUK TAB RECIPES
    def btnRecCreateOnButtonClick(self, event):
        # Buka dialog editor resep
        dialog = dialogRecipe(self)
        if dialog.ShowModal() == wx.ID_OK:
            # jika OK
            pass
        dialog.Destroy()

#### KODE UNTUK TAB OPERATORS
        
    def btnOpCreateOnButtonClick(self, event):
        message = """Create a new operator name

1. Go to the Home tab.
2. Type it in the "Operator 1" or "Operator 2" field.

The app will remember the name if it doesn't already exist."""

        wx.MessageBox(message, "Create a new name", wx.OK | wx.ICON_INFORMATION)

    def btnOpRefreshOnClick(self, event):
        results = self.getOpNames()

        # Clear the list control first
        self.lcOpOperators.DeleteAllItems()

        for i, row in enumerate(results):
            name = row[0]
            index = self.lcOpOperators.InsertItem(i, name)

    def getOpNames(self):
        try:
            c.execute("SELECT name FROM operators") 
            return c.fetchall()
        except sqlite3.Error as e:
            wx.MessageBox(f"Error fetching data: {e}.", "Error", wx.OK | wx.ICON_ERROR)
            return []

    def btnOpDeleteOnClick(self, event):
        # Jika ada yang di pilih
        index = self.lcOpOperators.GetFirstSelected()
        if index != -1:  # Ensure there is at least one selection
            # Retrieve the text of the selected item(s)
            name = self.lcOpOperators.GetItemText(index)
            self.cfmOpDelete(name)
        else:
            wx.MessageBox(f"Please choose an operator name to delete.", "No name selected", wx.OK)


    def cfmOpDelete(self, name):
        dialog = wx.MessageDialog(self,
                                f"Are you sure you want to delete '{name}'?",
                                "Delete confirmation",
                                style=wx.YES_NO | wx.NO_DEFAULT)
        if dialog.ShowModal() == wx.ID_YES:
            self.delOpName(name)

    def delOpName(self, name):
        try:
            c.execute("DELETE FROM operators WHERE LOWER(name) = LOWER(?)", (name,))
            conn.commit()

            self.btnOpRefreshOnClick(self)
            self.cbHomeOpUpdate()

        except sqlite3.Error as e:
            wx.MessageBox(f"Error deleting item: {e}", "Error", wx.OK | wx.ICON_ERROR)

class dialogColor(dgColor):
    def __init__(self, parent):
        
        # Insiasi parent class
        dgColor.__init__(self, parent)

        self.lcColors.InsertColumn(0, "Colors")
        width = self.GetSize().width - 40
        self.lcColors.SetColumnWidth(0, width)
        self.lcColors.Append(["WHITE"])
        self.lcColors.Append(["BLACK"])
        self.lcColors.Append(["WHITE REGRIND"])

        font = self.lcColors.GetFont()
        font.SetPointSize(font.GetPointSize() + 6)  # Increase font size
        self.lcColors.SetFont(font)
    
    def btnApplyOnButtonClick(self, event):
        
        index = self.lcColors.GetFirstSelected()
        if index != -1:  # Ensure there is at least one selection
            # Retrieve the text of the selected item(s)
            color = self.lcColors.GetItemText(index)
            wx.MessageBox(f"Selected color: {color}", "Information")
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox(f"Please choose a color.", "No color selected", wx.OK)
   

class dialogRecipe(dgRecipe):
    def __init__(self, parent):
        
        # Insiasi parent class
        dgRecipe.__init__(self, parent)
    
    def btnSaveOnButtonClick(self, event):
        self.EndModal(wx.ID_OK)

#### MENYALAKAN APLIKASI ####            

class MainApp(wx.App):
    def OnInit(self):
        self.frame = frameMain(None)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = MainApp(redirect=False)
    app.MainLoop()
