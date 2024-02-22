import wx
import wx.svg
import os
import sqlite3
import math
import cerberus
import cv2
from datetime import datetime
from omv_ui import frMain, dgColor, dgRecipes

os.environ['WXSUPPRESS_SIZER_FLAGS_CHECK'] = '1'

# Menghubungkan ke database
conn = sqlite3.connect('omv.db')
c = conn.cursor()

# Buat tabel recipes
c.execute("""CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT,
    time_1 INTEGER,
    desc_1 TEXT,
    time_2 INTEGER,
    desc_2 TEXT,
    time_3 INTEGER,
    desc_3 TEXT
)""")

# Buat tabel operators
c.execute('''CREATE TABLE IF NOT EXISTS operators (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

conn.commit()

# Untuk mengubah time (integer) menjadi format mm:ss
def formatTime(secs):
    minutes = secs // 60
    seconds = secs % 60
    return f"{minutes:02d}:{seconds:02d}"

#### FRAME MAIN ####

class frameMain(frMain):
    def __init__(self, parent):

        # Insiasi parent class
        frMain.__init__(self, parent)

        # Tanggal dan waktu bergerak
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateTime, self.timer)
        self.timer.Start(1000)

        self.tBatchTsEnd1 = 0
        self.tBatchTsEnd2 = 0
        self.tBatchTsEnd3 = 0

        # Inisiasi font size
        fontTime = self.stHomeTime1.GetFont()
        fontDesc = self.stHomeDesc1.GetFont()
        fontTime.SetPointSize(fontTime.GetPointSize() + 2)  
        fontDesc.SetPointSize(fontDesc.GetPointSize() + 4)
        self.stHomeTime1.SetFont(fontTime)
        self.stHomeTime2.SetFont(fontTime)
        self.stHomeTime3.SetFont(fontTime)
        # self.stHomeStdTime1.SetFont(fontTime)
        # self.stHomeStdTime2.SetFont(fontTime)
        # self.stHomeStdTime3.SetFont(fontTime)
        self.stHomeDesc1.SetFont(fontDesc)
        self.stHomeDesc2.SetFont(fontDesc)
        self.stHomeDesc3.SetFont(fontDesc)

        # Inisiasi Operators
        self.lcOperators.InsertColumn(0, "Name")
        self.btnOpRefreshOnButtonClick(self)
        self.cbHomeOpUpdate()

        # Inisasi Kolom Recipes
        self.lcRecipes.InsertColumn(0, "Color")
        self.lcRecipes.InsertColumn(1, "Time 1")
        self.lcRecipes.InsertColumn(2, "Description 1", width=200)
        self.lcRecipes.InsertColumn(3, "Time 2")
        self.lcRecipes.InsertColumn(4, "Description 2", width=200)
        self.lcRecipes.InsertColumn(5, "Time 3")
        self.lcRecipes.InsertColumn(6, "Description 3", width=200)
        self.lcRecipesUpdate()

    def updateTime(self, event):
        # Format tanggal dan waktu bergerak
        now     = datetime.now()
        nowStr  = now.strftime('%Y-%m-%d %H:%M:%S')
        nowTs   = now.timestamp()
        
        # Update status bar yang di bawah
        self.sbMain.SetStatusText("Ready", 0)
        self.sbMain.SetStatusText("COM3", 1)
        self.sbMain.SetStatusText("BAUD 9600", 2)
        self.sbMain.SetStatusText(nowStr, 3)
        timeact = 99999
        timeTotal = self.gHome1.GetRange() + self.gHome2.GetRange() + self.gHome3.GetRange()

        # Update hitung mundur jika tBatchTsEnd3 terisi
        if not timeact == 0:

            # Elapsed Time
            # timeTotal = self.gHome1.GetRange() + self.gHome2.GetRange() + self.gHome3.GetRange()
            # remainingTotal = self.tBatchTsEnd3 - nowTs
            # elapsedTotal = timeTotal - remainingTotal
            timeact -= 1
            timeTotal -= 1
            self.stHomeElapsed.SetLabel(formatTime(math.floor(timeTotal))) 
           
            if nowTs < self.tBatchTsEnd1:
                print('Step 1')
                self.btnHomeFinish.Disable()
                remaining = math.floor(self.tBatchTsEnd1 - nowTs)
                elapsed = self.gHome1.GetRange() - remaining
                self.stHomeTime1.SetLabel(formatTime(remaining))
                self.gHome1.SetValue(elapsed)
                timeact += 1

            elif nowTs < self.tBatchTsEnd2:
                print('Step 2')
                self.btnHomeFinish.Disable()
                remaining = math.floor(self.tBatchTsEnd2 - nowTs)
                elapsed = self.gHome2.GetRange() - remaining
                self.stHomeTime2.SetLabel(formatTime(remaining))
                self.gHome2.SetValue(elapsed)
            
            elif nowTs < self.tBatchTsEnd3:
                print('Step 3')
                self.btnHomeFinish.Enable()
                remaining = math.floor(self.tBatchTsEnd3 - nowTs)
                elapsed = self.gHome3.GetRange() - remaining
                self.stHomeTime3.SetLabel(formatTime(remaining))               
                self.gHome3.SetValue(elapsed) 
            else:
                self.tBatchTsEnd3 = 0
                self.btnHomeStatusLoad.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

#### FRAME MAIN: TAB HOME ####

    # Kode untuk pilih warna    
    def btnHomeColOnClick(self, event):

        # Buka dialog pilih warna
        dialog = dialogColor(self)
        if dialog.ShowModal() == wx.ID_OK:
           
            # Eksekusi pilih warna ketika OK
            color_choice = dialog.GetColorChoice()
            event.GetEventObject().SetLabel(color_choice)
            pass

        dialog.Destroy()
    
    # Update combo box operator 1 dan operator 2
    def cbHomeOpUpdate(self):
        
        operators = self.getOp()
        names = [item[0] for item in operators]
        # kode belum beres

    # Start manual proses batch (harusnya pake sensor arduino)
    def btnStartOnButtonClick(self, event):
        Time1 = 5
        Time2 = 5
        Time3 = 5
        self.btnHomeStatusLoad.SetBackgroundColour(wx.GREEN)

        self.gHome1.SetRange(Time1)
        self.gHome2.SetRange(Time2)
        self.gHome3.SetRange(Time3)

        self.gHome1.SetValue(0)
        self.gHome2.SetValue(0)
        self.gHome3.SetValue(0)

        self.stHomeTime1.SetLabel(formatTime(Time1))
        self.stHomeTime2.SetLabel(formatTime(Time2))
        self.stHomeTime3.SetLabel(formatTime(Time3))

        nowTs = datetime.now().timestamp()
        # Waktu berakhir step 1
        self.tBatchTsEnd1 = nowTs + Time1
        # Waktu berakhir step 2
        self.tBatchTsEnd2 = self.tBatchTsEnd1 + Time2
        # Waktu berakhir step 3
        self.tBatchTsEnd3 = self.tBatchTsEnd2 + Time3

    # Fungsi button finish
    def btnHomeFinishOnButtonClick(self, event):
        self.tBatchTsEnd3 = 0
        wx.MessageBox(f"Process Finished", "Final Step", wx.OK)
        self.gHome1.SetValue(0)
        self.gHome2.SetValue(0)
        self.gHome3.SetValue(0)
        self.btnHomeStatusLoad.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
    
    # Ambil foto dari webcam dan simpan dengan nama timestamp
    def btnHomeCam1OnButtonClick(self, event):

        # Inisiasi webcam, jangan lupa kamera nomor berapa 0 kamera utama, 1 kamera kedua, 2 kamera ketiga etc...
        cap = cv2.VideoCapture(0)

        # Cek jika sambungn ke webcam berhasil
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        # Ambil satu foto / frame
        ret, frame = cap.read()

        if ret:
            # Tentukan nama foto berdasarkan tanggal dan waktu
            namaFoto = datetime.now().strftime('%Y%m%d-%H%M%S')

            # Cek apabila ada folder photos
            os.makedirs("photos", exist_ok=True)

            # Simpan foto yang ditangkap dalam format JPG
            cv2.imwrite(f"photos/{namaFoto}.jpg", frame)
            print("Photo captured and saved successfully.")

        else:
            wx.MessageBox("Failed to capture photo.", "Error", wx.OK | wx.ICON_ERROR)

        # Release the VideoCapture object
        cap.release()
    
    # Fungsi Button Connect/Disconnect
    def btnHomeConnectOnButtonClick(self, event):
        if self.btnHomeConnect.GetLabel() == "Connect":
            self.btnHomeConnect.SetLabel("Disconnect")
        else:
            self.btnHomeConnect.SetLabel("Connect")
            
#### FRAME MAIN: TAB RECORDS ####

#### FRAME MAIN: TAB SUMMARY ####
            
#### FRAME MAIN: TAB SETTINGS ####
            
#### FRAME MAIN: TAB SETTINGS: LIST BOOK: GENERAL ####
            
#### FRAME MAIN: TAB SETTINGS: LIST BOOK: RECIPES ####
            
    # Ambil semua data resep dari database
    def getRecipes(self):
        c.execute('SELECT color,time_1,desc_1,time_2,desc_2,time_3,desc_3 FROM recipes')
        data = c.fetchall()
        return data
    
    # Panggil data dari database recipes, dan masukkan ke list control recipes
    def lcRecipesUpdate(self):  

        # Hapus dulu
        self.lcRecipes.DeleteAllItems()  

        # ambil semua resep dari database
        data = self.getRecipes()

        # baru update lagi
        for row_index, row_data in enumerate(data):
            self.lcRecipes.InsertItem(row_index, str(row_data[0]))
            for col_index, value in enumerate(row_data[0:]):
                modified_value = formatTime(value) if isinstance(value, int) and col_index in (1, 3, 5) else value
                self.lcRecipes.SetItem(row_index, col_index, str(modified_value))

    # Buka dialog editor resep (Buat baru, atau edit kalau colornya sudah ada)
    def btnRecCreateOnButtonClick(self, event):

        # Inisiasi dialog resep
        dialog = dialogRecipes(self, colorName="")

        if dialog.ShowModal() == wx.ID_OK:
            self.lcRecipesUpdate()

        dialog.Destroy()

    def btnRecRefreshOnClick(self, event):
        # Clear the list control first
        self.lcRecipes.DeleteAllItems()
        self.lcRecipes.DeleteAllColumns()

        # Inisasi kolom Recipes
        self.lcRecipes.InsertColumn(0, "Color")
        self.lcRecipes.InsertColumn(1, "Time 1")
        self.lcRecipes.InsertColumn(2, "Description 1", width=200)
        self.lcRecipes.InsertColumn(3, "Time 2")
        self.lcRecipes.InsertColumn(4, "Description 2", width=200)
        self.lcRecipes.InsertColumn(5, "Time 3")
        self.lcRecipes.InsertColumn(6, "Description 3", width=200)

        data = self.getRecipes()
        for row_index, row_data in enumerate(data):
            self.lcRecipes.InsertItem(row_index, str(row_data[0]))
            for col_index, value in enumerate(row_data[1:]):
                self.lcRecipes.SetItem(row_index, col_index + 1, str(value))
       
    # Fungsi edit recipis (minus timer nya)
       
    def btnRecEditOnButtonClick(self, event):
        # Dapatkan baris yang dipilih
        index = self.lcRecipes.GetFirstSelected()

        # Jika ada baris yang dipilih
        if not index == -1:
            
            # Dapatkan warna berdasarkan index baris yang dipilih
            colorName = self.lcRecipes.GetItemText(index)
            
        else:
            wx.MessageBox(f"Please choose a recipe to edit.", "No recipe selected", wx.OK)

        # Inisiasi dialog resep
        dialog = dialogRecipes(self, colorName=colorName)

        if dialog.ShowModal() == wx.ID_OK:
            self.lcRecipesUpdate()
            pass

        dialog.Destroy()
    
    #Fungsi delete recipes
    
    def btnRecDeleteOnButtonClick(self, event):
        
        # Dapatkan baris yang dipilih
        index = self.lcRecipes.GetFirstSelected()

        # Jika ada baris yang dipilih
        if not index == -1:

            # Dapatkan warna berdasarkan index baris yang dipilih
            colorName = self.lcRecipes.GetItemText(index)

            # Konfirmasi penghapusan
            dialog = wx.MessageDialog(
                self,
                "Are you sure you want to delete this recipe?",
                "Delete",
                wx.YES_NO | wx.ICON_QUESTION,
            )
            result = dialog.ShowModal()

            # Jika dikonfirmasi
            if result == wx.ID_YES:
                # Hapus data dari database MySQL
                # ... (kode untuk menghapus data dari database)

                # Hapus item dari list control
                self.lcRecipes.DeleteItem(index)


    
#### FRAME MAIN: TAB SETTINGS: LIST BOOK: OPERATORS ####
                
        def btnOpCreateOnButtonClick(self, event):
            message = """Create a new operator name
                1. Go to the Home tab.
                2. Type it in the Operator field.

                The app will remember the name if it doesn't already exist."""

            wx.MessageBox(message, "Create a new name", wx.OK | wx.ICON_INFORMATION)

    def btnOpRefreshOnButtonClick(self, event):
        results = self.getOp()

        # Clear the list control first
        self.lcOperators.DeleteAllItems()

        for i, row in enumerate(results):
            name = row[0]
            index = self.lcOperators.InsertItem(i, name)

    def getOp(self):
        try:
            c.execute("SELECT name FROM operators") 
            return c.fetchall()
        except sqlite3.Error as e:
            wx.MessageBox(f"Error fetching data: {e}.", "Error", wx.OK | wx.ICON_ERROR)
            return []

    def btnOpDeleteOnClick(self, event):
        # Jika ada yang di pilih
        index = self.lcOperators.GetFirstSelected()
        if not index == -1:  # Ensure there is at least one selection
            # Retrieve the text of the selected item(s)
            name = self.lcOperators.GetItemText(index)
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

            self.btnOpRefreshOnButtonClick(self)
            self.cbHomeOpUpdate()

        except sqlite3.Error as e:
            wx.MessageBox(f"Error deleting item: {e}", "Error", wx.OK | wx.ICON_ERROR)

    #Fungsi button reset
    def btn_resetOnButtonClick(self, event):
        self.choicePort.SetLabel("")
        self.btnStatusLoad.SetLabel("")
         # Update status bar yang di bawah
        self.sbMain.SetStatusText("", 0)
        self.sbMain.SetStatusText("", 1)
        self.sbMain.SetStatusText("", 2)
        self.sbMain.SetStatusText("", 3)


#### DIALOG COLOR ####
        
class dialogColor(dgColor):
    def __init__(self, parent):
        
        # Insiasi parent class
        dgColor.__init__(self, parent)

        self.lcColor.InsertColumn(0, "Colors")
        width = self.GetSize().width - 40
        self.lcColor.SetColumnWidth(0, width)
        self.lcColor.Append(["WHITE"])
        self.lcColor.Append(["COLOR"])
        self.lcColor.Append(["CLEAR"])
        self.lcColor.Append(["BLACK & COLOR"])
        self.lcColor.Append(["LOGO"])
        self.lcColor.Append(["WHITE REGRIND"])
        self.lcColor.Append(["REGRIND 9%"])
        self.lcColor.Append(["REGRIND 15%"])

        font = self.lcColor.GetFont()
        font.SetPointSize(font.GetPointSize() + 6)  # Increase font size
        self.lcColor.SetFont(font)
    
    def btnApplyOnButtonClick(self, event):
        
        index = self.lcColor.GetFirstSelected()
        if index != -1:  # Ensure there is at least one selection
            # Retrieve the text of the selected item(s)
            color = self.lcColor.GetItemText(index)
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox(f"Please choose a color.", "No color selected", wx.OK)

    def GetColorChoice(self):
        index = self.lcColor.GetFirstSelected()
        return self.lcColor.GetItemText(index)


#### DIALOG RECIPES ####
      
class dialogRecipes(dgRecipes):
    def __init__(self, parent, colorName):
        
        # Insiasi parent class
        dgRecipes.__init__(self, parent)

        # Inisiasi variabel color
        self.colorName = colorName

        if colorName:
            print("Dialog recipes ada terima warna, ambil dari database...")
            data = self.getRecipe(colorName)
            if data:
                self.tcColor.SetValue(str(data[1]))
                self.scTime1.SetValue(int(data[2]))
                self.tcDesc1.SetValue(str(data[3]))
                self.scTime2.SetValue(int(data[4]))
                self.tcDesc2.SetValue(str(data[5]))
                self.scTime3.SetValue(int(data[6]))
                self.tcDesc3.SetValue(str(data[7]))
                # disable tcColor
                self.tcColor.Disable()

    def getRecipe(self, colorName):
        try:
            c.execute(f"SELECT * FROM recipes WHERE color = '{colorName}'") 
            return c.fetchone()
        except sqlite3.Error as e:
            wx.MessageBox(f"Error fetching data: {e}.", "Error", wx.OK | wx.ICON_ERROR)
            return []

    def scTime1Update(self, event):
        self.stTime1.SetLabel(formatTime(self.scTime1.GetValue()))

    def scTime2Update(self, event):
        self.stTime2.SetLabel(formatTime(self.scTime2.GetValue()))

    def scTime3Update(self, event):
        self.stTime3.SetLabel(formatTime(self.scTime3.GetValue()))
    
    def btnSaveOnButtonClick(self, event):
        schema = {
            "color": {
                "type": "string",
                "required": True,
                "minlength": 1,
                "maxlength": 20,
            },
            "time_1": {
                "type": "integer",
                "required": True,
                "min": 0,
                "max": 3599,
            },
            "desc_1": {
                "type": "string",
                "required": True,
                "minlength": 1,
                "maxlength": 250,
            },
            "time_2": {
                "type": "integer",
                "required": True,
                "min": 0,
                "max": 3599,
            },
            "desc_2": {
                "type": "string",
                "required": True,
                "minlength": 1,
                "maxlength": 250,
            },
            "time_3": {
                "type": "integer",
                "required": True,
                "min": 0,
                "max": 3599,
            },
            "desc_3": {
                "type": "string",
                "required": True,
                "minlength": 1,
                "maxlength": 250,
            },
        }
        validator = cerberus.Validator(schema)
        color = str(self.tcColor.GetValue()).upper()
        data = {
            "color" : color,
            "time_1": self.scTime1.GetValue(),
            "desc_1": self.tcDesc1.GetValue(),
            "time_2": self.scTime2.GetValue(),
            "desc_2": self.tcDesc2.GetValue(),
            "time_3": self.scTime3.GetValue(),
            "desc_3": self.tcDesc3.GetValue(),
        }
        print (data)
        is_valid = validator.validate(data)
        if is_valid:
            # Check if color exists
            c.execute("SELECT id FROM recipes WHERE color = ?", (color,))
            existing_id = c.fetchone()

            if existing_id:

                # Update resep yang sudah ada di database
                recipe_id = existing_id[0]
                update_sql = """
                    UPDATE recipes
                    SET time_1 = ?, desc_1 = ?, time_2 = ?, desc_2 = ?, time_3 = ?, desc_3 = ?
                    WHERE id = ?
                """
                c.execute(update_sql, (data['time_1'], data['desc_1'], data['time_2'], data['desc_2'], data['time_3'], data['desc_3'],  recipe_id))
                wx.MessageBox(f"Recipes with color '{color}' updated successfully!", "Recipes updated", wx.OK | wx.ICON_INFORMATION)
            else:
                # Simpan resep baru di database
                insert_sql = """
                    INSERT INTO recipes (color, time_1, desc_1, time_2, desc_2, time_3, desc_3)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """
                c.execute(insert_sql, (data['color'], data['time_1'], data['desc_1'], data['time_2'], data['desc_2'], data['time_3'], data['desc_3']))
                wx.MessageBox(f"Recipes with color '{color}' added successfully!", "Recipes added", wx.OK | wx.ICON_INFORMATION)
            conn.commit()

            self.EndModal(wx.ID_OK)
        else:
            error_messages = []
            for field, errors in validator.errors.items():
                error_messages.append(f"- {field}: {','.join(errors)}")

            error_message = "\n".join(error_messages)
            wx.MessageBox(error_message, "Data invalid", wx.OK | wx.ICON_EXCLAMATION)
        

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
