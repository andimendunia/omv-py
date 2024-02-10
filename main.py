import wx
import os
import sqlite3
from datetime import datetime
from omv_ui import frMain, dgColors, dgRecipe

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

        # Inisasi Recipes
        self.lcRecRecipes.InsertColumn(0, "Color")
        self.lcRecRecipes.InsertColumn(1, "Description 1")
        self.lcRecRecipes.InsertColumn(2, "Time 1")
        self.lcRecRecipes.InsertColumn(3, "Description 2")
        self.lcRecRecipes.InsertColumn(4, "Time 2")
        self.lcRecRecipes.InsertColumn(5, "Description 3")
        self.lcRecRecipes.InsertColumn(6, "Time 3")

        # Inisiasi Operators
        self.lcOpOperators.InsertColumn(0, "Name")
        self.btnOpRefreshOnClick(self)

        self.OpIndexSelected = -1
        self.OpNameSelected = ""
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
        dialog = dgColors(self)
        if dialog.ShowModal() == wx.ID_OK:
            # Eksekusi pilih warna ketika OK
            pass
        dialog.Destroy()
        # No need to call event.Skip() unless you have a specific reason to continue event propagation
    
    def cbHomeOpUpdate(self):
        results = self.getOpNames()
        names = [item[0] for item in results]
        self.cbHomeOp1.Set(names)
        self.cbHomeOp2.Set(names)
        self.cbHomeOp1.AutoComplete(names)
        self.cbHomeOp2.AutoComplete(names)


#### KODE UNTUK TAB RECORDS 
        
#### KODE UNTUK TAB SUMMARY

#### KODE UNTUK TAB RECIPES
    def btnRecCreateOnButtonClick(self, event):
        # Buka dialog editor resep
        dialog = dgRecipe(self)
        if dialog.ShowModal() == wx.ID_OK:
            # jika OK
            pass
        dialog.Destroy()

#### KODE UNTUK TAB OPERATORS

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
   
    def lcOpOperatorsOnListItemSelected(self, event):
        self.OpIndexSelected = event.GetIndex()
        if self.OpIndexSelected != -1:
            # Get selected item data (assuming "name" in column 0)
            self.OpNameSelected = self.lcOpOperators.GetItemText(self.OpIndexSelected, 0)

    def btnOpDeleteOnClick(self, event):
        # Jika ada yang di pilih
        if self.OpIndexSelected != -1:
            self.cfmOpDelete()
            # Jika tidak ada yang di pilih
        else:    
            wx.MessageBox(f"No name selected.", "Error", wx.OK | wx.ICON_ERROR)


    def cfmOpDelete(self):
        dialog = wx.MessageDialog(self,
                                f"Are you sure you want to delete '{self.OpNameSelected}'?",
                                "Delete Confirmation",
                                style=wx.YES_NO | wx.NO_DEFAULT)
        if dialog.ShowModal() == wx.ID_YES:
            self.delOpName()

    def delOpName(self):
        try:
            c.execute("DELETE FROM operators WHERE LOWER(name) = LOWER(?)", (self.OpNameSelected,))
            conn.commit()

            # Remove item from list control after successful deletion
            self.lcOpOperators.DeleteItem(self.OpIndexSelected)
            self.OpIndexSelected = -1  # Reset selected index
            self.cbHomeOpUpdate()

        except sqlite3.Error as e:
            wx.MessageBox(f"Error deleting item: {e}", "Error", wx.OK | wx.ICON_ERROR)


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
