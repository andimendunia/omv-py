import wx
import os
from datetime import datetime
from omv_ui import frMain, dgColSelector  # Adjust the import statement based on your file's name and structure

os.environ['WXSUPPRESS_SIZER_FLAGS_CHECK'] = '1'

class frameMain(frMain):
    def __init__(self, parent):
        # Initialize the parent class
        frMain.__init__(self, parent)

        # Waktu nyata
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateTime, self.timer)
        self.timer.Start(1000)

    def updateTime(self, event):
        # Format the current time as a string. Adjust the format as needed.
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Update the wx.StaticText widget with the current time
        self.stTime.SetLabel(currentTime)
        
    def btnColMainOnClick(self, event):
        # Custom logic for opening the dgColSelector dialog
        dialog = dgColSelector(self)
        if dialog.ShowModal() == wx.ID_OK:
            # Handle dialog OK result here, if necessary
            pass
        dialog.Destroy()
        # No need to call event.Skip() unless you have a specific reason to continue event propagation

class MainApp(wx.App):
    def OnInit(self):
        self.frame = frameMain(None)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = MainApp(redirect=False)
    app.MainLoop()
