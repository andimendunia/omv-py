import wx
import os
import sqlite3
from datetime import datetime
from omv_ui import frMain, dgColors 

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

        # Waktu bergerak
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateTime, self.timer)
        self.timer.Start(1000)

    def updateTime(self, event):
        #Format tanggal dan waktu bergerak
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Update waktu bergerak ke status bar
        self.sbMain.SetStatusText("Ready", 0)
        self.sbMain.SetStatusText("COM3", 1)
        self.sbMain.SetStatusText("BAUD 9600", 2)
        self.sbMain.SetStatusText(currentTime, 3)
        
    def btnHomeColOnClick(self, event):
        # Buka dialog pilih warna
        dialog = dgColors(self)
        if dialog.ShowModal() == wx.ID_OK:
            # Handle dialog OK result here, if necessary
            pass
        dialog.Destroy()
        # No need to call event.Skip() unless you have a specific reason to continue event propagation

    def btnOpSaveOnClick(self, event):
        name = self.tcOpName.GetValue().strip()
        if not len(name) > 0:
            wx.MessageBox(f"Name cannot be empty.", "Error", wx.OK | wx.ICON_ERROR)
        else:
            # Check if the name already exists in the database
            c.execute("SELECT * FROM operators WHERE LOWER(name) = LOWER(?)", (name,))
            if c.fetchone():
                # If the name exists, show a message box and do not insert
                wx.MessageBox(f"Name '{name}' already exists.", "Error", wx.OK | wx.ICON_ERROR)
            else:
                # If the name does not exist, insert it into the database
                c.execute("INSERT INTO operators (name) VALUES (?)", (name,))
                conn.commit()
                # Show a success message
                wx.MessageBox(f"Name '{name}' successfully saved", "Saved", wx.OK | wx.ICON_INFORMATION)
            

class MainApp(wx.App):
    def OnInit(self):
        self.frame = frameMain(None)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = MainApp(redirect=False)
    app.MainLoop()
