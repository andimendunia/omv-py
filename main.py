import wx
import wx.svg
import os
import sqlite3
import math
import cerberus
import cv2
from datetime import datetime
from omv_ui import frMain, dgColor, dgRecipes, dgLogin, dgRegister

os.environ["WXSUPPRESS_SIZER_FLAGS_CHECK"] = "1"

# Menghubungkan ke database
conn = sqlite3.connect("omv.db")
c = conn.cursor()

# Buat tabel informasi (records)
c.execute(
    """CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date INTEGER,
    operator_1 TEXT,
    operator_2 TEXT,
    shift INTEGER,
    line INTEGER,
    color TEXT,
    no_batch TEXT,
    status_batch TEXT,
    start_time INTEGER,
    finish_time INTEGER,
    total_time INTEGER,
    validation_1 STRING,
    validation_2 STRING,
    validation_3 STRING
)"""
)

# Buat tabel rekap (summary)
c.execute(
    """CREATE TABLE IF NOT EXISTS summary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount_batch INTEGER,
    under CHAR,
    ok CHAR,
    over CHAR
)"""
)

# Buat tabel settings warna(recipes)
c.execute(
    """CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT,
    time_1 INTEGER,
    desc_1 TEXT,
    time_2 INTEGER,
    desc_2 TEXT,
    time_3 INTEGER,
    desc_3 TEXT
)"""
)

# Buat tabel operators
c.execute(
    """CREATE TABLE IF NOT EXISTS operators (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nik INTEGER,
    name TEXT
)"""
)

conn.commit()


# Untuk mengubah time (integer) menjadi format mm:ss
def formatTime(secs):
    if secs < 0:
        minutes = -(secs) // 60
        seconds = -(secs) % 60
        return f"-{minutes:02d}:{seconds:02d}"
    else:
        minutes = secs // 60
        seconds = secs % 60
        return f"{minutes:02d}:{seconds:02d}"


#### FRAME MAIN (BERANDA)####


class frameMain(frMain):
    def __init__(self, parent):

        # Insiasi parent class
        frMain.__init__(self, parent)

        # Tanggal dan waktu bergerak
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateTime, self.timer)
        self.timer.Start(1000)

        # Inisiasi data warna
        self.color = "Pilih Warna"
        self.time1 = 0
        self.time2 = 0
        self.time3 = 0
        self.desc1 = "Deskripsi Step 1"
        self.desc2 = "Deskripsi Step 2"
        self.desc3 = "Deskripsi Step 3"

        # Default value
        self.btnHomeCol.SetLabel(self.color)
        self.stHomeDesc1.SetLabel(self.desc1)
        self.stHomeDesc2.SetLabel(self.desc2)
        self.stHomeDesc3.SetLabel(self.desc3)
        self.stHomeStdTime1.SetLabel(formatTime(self.time1))
        self.stHomeStdTime2.SetLabel(formatTime(self.time2))
        self.stHomeStdTime3.SetLabel(formatTime(self.time3))
        self.btnHomeFinish.Disable()
        self.btnStart.Disable()
        self.stHomeOp1.SetLabel("-")
        self.stHomeOp2.SetLabel("-")
        self.stHomeShift.SetLabel("-")
        self.stHomeLine.SetLabel("-")
        self.stHomeTime1.SetLabel("-")

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

        # Inisasi Kolom Recipes
        self.lcRecipes.InsertColumn(0, "Color")
        self.lcRecipes.InsertColumn(1, "Time 1")
        self.lcRecipes.InsertColumn(2, "Description 1", width=200)
        self.lcRecipes.InsertColumn(3, "Time 2")
        self.lcRecipes.InsertColumn(4, "Description 2", width=200)
        self.lcRecipes.InsertColumn(5, "Time 3")
        self.lcRecipes.InsertColumn(6, "Description 3", width=200)
        self.lcRecipesUpdate()

        # Inisasi Kolom Records
        self.lcRecords.InsertColumn(0, "Tanggal")
        self.lcRecords.InsertColumn(1, "Operator 1")
        self.lcRecords.InsertColumn(2, "Operator 2")
        self.lcRecords.InsertColumn(3, "Shift")
        self.lcRecords.InsertColumn(4, "Line",)
        self.lcRecords.InsertColumn(5, "Color")
        self.lcRecords.InsertColumn(6, "No. Batch")
        self.lcRecords.InsertColumn(7, "Status batch")
        self.lcRecords.InsertColumn(8, "Waktu mulai")
        self.lcRecords.InsertColumn(9, "Waktu selesai")
        self.lcRecords.InsertColumn(10, "Total waktu")
        self.lcRecords.InsertColumn(11, "Validasi 1")
        self.lcRecords.InsertColumn(12, "Validasi 2")
        self.lcRecords.InsertColumn(13, "Validasi 3")

        # Inisasi Kolom Summary
        self.lcSum.InsertColumn(0, "Jumlah batch")
        self.lcSum.InsertColumn(1, "Under")
        self.lcSum.InsertColumn(2, "Ok")
        self.lcSum.InsertColumn(3, "Over")

        # Insiasi waktu mundur
        self.countdown = 0
        self.remain = 1
        self.stHomeElapsed.SetLabel(formatTime(self.countdown))

        # Flagging untuk waktu finish & start
        self.stopper = False

        # Inisiasi data recipes untuk di home
        self.dataRec = None

    def updateTime(self, event):
        # Format tanggal dan waktu bergerak
        now = datetime.now()
        nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
        nowTs = now.timestamp()

        # Update status bar yang di bawah
        self.sbMain.SetStatusText("COM3", 0)
        self.sbMain.SetStatusText("BAUD 9600", 1)
        self.sbMain.SetStatusText(nowStr, 2)

        # Update hitung mundur jika stopper statusnya True
        if self.stopper == True:

            if nowTs < self.tBatchTsEnd1:
                print("Step 1")
                self.btnHomeFinish.Disable()
                remaining = math.floor(self.tBatchTsEnd1 - nowTs)
                elapsed = self.gHome1.GetRange() - remaining
                self.stHomeTime1.SetLabel(formatTime(remaining))
                self.gHome1.SetValue(elapsed)
                # elapsed time
                self.countdown += 1
                self.stHomeElapsed.SetLabel(formatTime(self.countdown))    

            elif nowTs < self.tBatchTsEnd2:
                print("Step 2")
                self.btnHomeFinish.Disable()
                remaining = math.floor(self.tBatchTsEnd2 - nowTs)
                elapsed = self.gHome2.GetRange() - remaining
                self.stHomeTime2.SetLabel(formatTime(remaining))
                self.gHome2.SetValue(elapsed)
                # elapsed time
                self.stHomeElapsed.SetLabel(formatTime(self.countdown))
                self.countdown += 1

            elif nowTs < self.tBatchTsEnd3:
                print("Step 3")
                self.btnHomeFinish.Enable()
                remaining = math.floor(self.tBatchTsEnd3 - nowTs)
                elapsed = self.gHome3.GetRange() - remaining
                self.stHomeTime3.SetLabel(formatTime(remaining))
                self.gHome3.SetValue(elapsed)
                # elapsed time
                self.countdown += 1
                self.stHomeElapsed.SetLabel(formatTime(self.countdown))
                self.stHomeLatestBatch.SetLabel("LESS")
            
            else:
                if self.tBatchTsEnd3 == self.remain:
                    self.stHomeLatestBatch.SetLabel("OK")
                else:
                    self.stHomeLatestBatch.SetLabel("OVER")
                # Buat minus step 3
                self.remain -= 1 
                self.stHomeTime3.SetLabel(formatTime(self.remain))
                # Buat elapsed setelah step 3
                self.countdown += 1
                self.stHomeElapsed.SetLabel(formatTime(self.countdown))

    #### FRAME MAIN: TAB BERANDA ####

     # Kode untuk ganti operator
    # def btnHomeChangeOnButtonClickk(self, event):

    # Kode untuk pilih warna
    def btnHomeColOnClick(self, event):

        # Buka dialog pilih warna
        dialog = dialogColor(self)
        if dialog.ShowModal() == wx.ID_OK:
            # Manggil text warna
            color_choice = dialog.GetColorChoice()
            event.GetEventObject().SetLabel(color_choice)

            # Get data
            data = dialog.GetDataColor()
            self.dataRec = data
            self.color = self.dataRec[1]
            self.time1 = self.dataRec[2]
            self.time2 = self.dataRec[4]
            self.time3 = self.dataRec[6]
            self.desc1 = self.dataRec[3]
            self.desc2 = self.dataRec[5]
            self.desc3 = self.dataRec[7]
            self.stHomeTime1.SetLabel(formatTime(self.time1))
            self.stHomeTime2.SetLabel(formatTime(self.time2))
            self.stHomeTime3.SetLabel(formatTime(self.time3))
            self.stHomeDesc1.SetLabel(self.desc1)
            self.stHomeDesc2.SetLabel(self.desc2)
            self.stHomeDesc3.SetLabel(self.desc3)
            self.stHomeStdTime1.SetLabel(formatTime(self.time1))
            self.stHomeStdTime2.SetLabel(formatTime(self.time2))
            self.stHomeStdTime3.SetLabel(formatTime(self.time3))
            self.btnStart.Enable()
        dialog.Destroy()        

    # Start manual proses batch (harusnya pake sensor arduino)
    def btnStartOnButtonClick(self, event):
        self.btnHomeStatusLoad.SetBackgroundColour(wx.GREEN)
        
        self.countdown = 0
        self.stHomeTime1.SetLabel(formatTime(self.time1))
        self.stHomeTime2.SetLabel(formatTime(self.time2))
        self.stHomeTime3.SetLabel(formatTime(self.time3))

        self.gHome1.SetRange(self.dataRec[2])
        self.gHome2.SetRange(self.dataRec[4])
        self.gHome3.SetRange(self.dataRec[6])

        self.gHome1.SetValue(0)
        self.gHome2.SetValue(0)
        self.gHome3.SetValue(0)

        nowTs = datetime.now().timestamp()
        # Waktu berakhir step 1
        self.tBatchTsEnd1 = nowTs + self.dataRec[2]
        # Waktu berakhir step 2
        self.tBatchTsEnd2 = self.tBatchTsEnd1 + self.dataRec[4]
        # Waktu berakhir step 3
        self.tBatchTsEnd3 = self.tBatchTsEnd2 + self.dataRec[6]

        self.timer.Start(1000)
        self.stopper = True

    # Fungsi button selesai (finish)
    def btnHomeFinishOnButtonClick(self, event):
        self.tBatchTsEnd3 = 0
        wx.MessageBox(f"Process Finished", "Final Step", wx.OK)
        self.gHome1.SetValue(0)
        self.gHome2.SetValue(0)
        self.gHome3.SetValue(0)
        self.timer.Stop()
        self.btnHomeStatusLoad.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU)
        )
        self.stopper = False

    # Ambil foto dari webcam dan simpan dengan nama timestamp
    def btnHomeCam1OnButtonClick(self, event):

        # Inisiasi webcam, jangan lupa kamera nomor berapa 0 kamera utama, 1 kamera kedua, 2 kamera ketiga etc...
        cap = cv2.VideoCapture(0)

        # Cek jika sambungn ke webcam berhasil
        if not cap.isOpened():
            raise IOError("Tidak bisa membuka webcam")

        # Ambil satu foto / frame
        ret, frame = cap.read()

        if ret:
            # Tentukan nama foto berdasarkan tanggal dan waktu
            namaFoto = datetime.now().strftime("%Y%m%d-%H%M%S")

            # Cek apabila ada folder photos
            os.makedirs("photos", exist_ok=True)

            # Simpan foto yang ditangkap dalam format JPG
            cv2.imwrite(f"photos/{namaFoto}.jpg", frame)
            print("Photo captured and saved successfully.")

        else:
            wx.MessageBox("Failed to capture photo.", "Error", wx.OK | wx.ICON_ERROR)

        # Release the VideoCapture object
        cap.release()

    #### FRAME MAIN: TAB RECORDS ####

    #### FRAME MAIN: TAB SUMMARY ####

    #### FRAME MAIN: TAB SETTINGS ####

    #### FRAME MAIN: TAB SETTINGS: LIST BOOK: GENERAL ####
    
    # Fungsi Button Connect/Disconnect
    def btnHomeConnectOnButtonClick(self, event):
        if self.btnHomeConnect.GetLabel() == "Connect":
            self.btnHomeConnect.SetLabel("Disconnect")
        else:
            self.btnHomeConnect.SetLabel("Connect")


    #### FRAME MAIN: TAB SETTINGS: LIST BOOK: RECIPES ####

    # Ambil semua data resep dari database
    def getRecipes(self):
        c.execute("SELECT color,time_1,desc_1,time_2,desc_2,time_3,desc_3 FROM recipes")
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
                modified_value = (
                    formatTime(value)
                    if isinstance(value, int) and col_index in (1, 3, 5)
                    else value
                )
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

    # Fungsi edit recipes

    def btnRecEditOnButtonClick(self, event):
        # Dapatkan baris yang dipilih
        index = self.lcRecipes.GetFirstSelected()

        # Jika ada baris yang dipilih
        if not index == -1:

            # Dapatkan warna berdasarkan index baris yang dipilih
            colorName = self.lcRecipes.GetItemText(index)

        else:
            wx.MessageBox(
                f"Silahkan pilih resep untuk di edit", "Tidak ada resep yang dipilih", wx.OK
            )

        # Inisiasi dialog resep
        dialog = dialogRecipes(self, colorName=colorName)

        if dialog.ShowModal() == wx.ID_OK:
            self.lcRecipesUpdate()
            pass

        dialog.Destroy()

    # Fungsi delete recipes

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
                "Anda yakin akan menghapus resep ini?",
                "Hapus",
                wx.YES_NO | wx.ICON_QUESTION,
            )
            result = dialog.ShowModal()

            # Jika dikonfirmasi
            if result == wx.ID_YES:
                # Hapus data dari database MySQL
                # ... (kode untuk menghapus data dari database)

                # Hapus item dari list control
                c.execute("DELETE FROM recipes WHERE color = ?", (colorName,))
                conn.commit()
                self.lcRecipes.DeleteItem(index)

    #Fungsi duplicate recipes
    def btnRecDupOnButtonClick(self, event):
        # Dapatkan baris yang dipilih
        index = self.lcRecipes.GetFirstSelected()

        # Jika ada baris yang dipilih
        if not index == -1:

            # Dapatkan warna berdasarkan index baris yang dipilih
            colorName = self.lcRecipes.GetItemText(index)

        else:
            wx.MessageBox(
                f"Silahkan pilih resep untuk di duplikat", "Tidak ada resep yang dipilih", wx.OK
            )

        # Inisiasi dialog resep
        dialog = dialogRecipes(self, colorName=colorName)

        if dialog.ShowModal() == wx.ID_OK:
            self.lcRecipesUpdate()    
            pass

        dialog.Destroy()

        #### FRAME MAIN: TAB SETTINGS: LIST BOOK: OPERATORS ####
    
    # Inisiasi dialog register
        dialog = dialogRegister(self, opName="")
    
    # Ambil semua data operator dari database
    def getRegister(self):
        c.execute("SELECT nik, nama")
        data = c.fetchall()
        return data
    
    # Panggil data dari database operators, dan masukkan ke list control operators
    def lcOperatorsUpdate(self):

        # Hapus dulu
        self.lcOperators.DeleteAllItems()

        # ambil semua resep dari database
        data = self.getOperators()

        # baru update lagi
        for row_index, row_data in enumerate(data):
            self.lcOperators.InsertItem(row_index, str(row_data[0]))
            for col_index, value in enumerate(row_data[0:]):
                modified_value = (
                    formatTime(value)
                    if isinstance(value, int) and col_index in (0, 1, 2)
                    else value
                )
                self.lcOperators.SetItem(row_index, col_index, str(modified_value))

    # Buka dialog register (Buat baru, atau edit kalau namanya sudah ada)
    def btnOpBaruOnButtonClick(self, event):

        # Inisiasi dialog resep
        dialog = dialogRegister(self, opName="")

        if dialog.ShowModal() == wx.ID_OK:
            self.lcOperatorsUpdate()

        dialog.Destroy()

    # Fungsi button reset
    def btn_resetOnButtonClick(self, event):
        self.choicePort.SetLabel("")
        self.btnStatusLoad.SetLabel("")
        # Update status bar yang di bawah
        self.sbMain.SetStatusText("", 0)
        self.sbMain.SetStatusText("", 1)
        self.sbMain.SetStatusText("", 2)

#### DIALOG COLOR ####

class dialogColor(dgColor):
    def __init__(self, parent):

        # Insiasi parent class
        dgColor.__init__(self, parent)

        # Inisiasi warna
        c.execute("SELECT * FROM recipes")
        data = c.fetchall()

        self.lcColor.InsertColumn(0, "Colors")
        width = self.GetSize().width - 40
        self.lcColor.SetColumnWidth(0, width)
        for i, value in enumerate(data):
            self.lcColor.Append([value[1]])

        font = self.lcColor.GetFont()
        font.SetPointSize(font.GetPointSize() + 6)  # Increase font size
        self.lcColor.SetFont(font)

    def getRecipe(self, colorName):
        try:
            c.execute(f"SELECT * FROM recipes WHERE color = '{colorName}'")
            return c.fetchone()
        except sqlite3.Error as e:
            wx.MessageBox(f"Error fetching data: {e}.", "Error", wx.OK | wx.ICON_ERROR)
            return []

    def btnApplyOnButtonClick(self, event):

        index = self.lcColor.GetFirstSelected()
        if index != -1:  # Ensure there is at least one selection
            # Retrieve the text of the selected item(s)
            color = self.lcColor.GetItemText(index)
            self.EndModal(wx.ID_OK)
            self.data = self.getRecipe(color)
        else:
            wx.MessageBox(f"Please choose a color.", "No color selected", wx.OK)

    def GetColorChoice(self):
        index = self.lcColor.GetFirstSelected()
        return self.lcColor.GetItemText(index)
        
    def GetDataColor(self):
        index = self.lcColor.GetFirstSelected()
        color = self.lcColor.GetItemText(index)
        data = self.getRecipe(color)
        return data


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
            "color": color,
            "time_1": self.scTime1.GetValue(),
            "desc_1": self.tcDesc1.GetValue(),
            "time_2": self.scTime2.GetValue(),
            "desc_2": self.tcDesc2.GetValue(),
            "time_3": self.scTime3.GetValue(),
            "desc_3": self.tcDesc3.GetValue(),
        }
        print(data)
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
                c.execute(
                    update_sql,
                    (
                        data["time_1"],
                        data["desc_1"],
                        data["time_2"],
                        data["desc_2"],
                        data["time_3"],
                        data["desc_3"],
                        recipe_id,
                    ),
                )
                wx.MessageBox(
                    f"Recipes with color '{color}' updated successfully!",
                    "Recipes updated",
                    wx.OK | wx.ICON_INFORMATION,
                )
            else:
                # Simpan resep baru di database
                insert_sql = """
                    INSERT INTO recipes (color, time_1, desc_1, time_2, desc_2, time_3, desc_3)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """
                c.execute(
                    insert_sql,
                    (
                        data["color"],
                        data["time_1"],
                        data["desc_1"],
                        data["time_2"],
                        data["desc_2"],
                        data["time_3"],
                        data["desc_3"],
                    ),
                )
                wx.MessageBox(
                    f"Recipes with color '{color}' added successfully!",
                    "Recipes added",
                    wx.OK | wx.ICON_INFORMATION,
                )
            conn.commit()

            self.EndModal(wx.ID_OK)
        else:
            error_messages = []
            for field, errors in validator.errors.items():
                error_messages.append(f"- {field}: {','.join(errors)}")

            error_message = "\n".join(error_messages)
            wx.MessageBox(error_message, "Data invalid", wx.OK | wx.ICON_EXCLAMATION)


#### DIALOG LOGIN ####



#### DIALOG REGISTER ####
            
class dialogRegister(dgRegister):
    def __init__(self, parent, opName):

        # Insiasi parent class
        dgRegister.__init__(self, parent)

        # Inisiasi variabel name
        self.opName = opName

        if opName:
            print("Dialog register ada terima nama, ambil dari database...")
            data = self.getOperators(opName)
            if data:
                self.tcNik.SetValue(int(data[1]))
                self.tcOpName.SetValue(str(data[2]))
                # disable tcNik
                # self.tcNik.Disable()

    def getOperators(self, opName):
        try:
            c.execute(f"SELECT * FROM operators WHERE name = '{opName}'")
            return c.fetchone()
        except sqlite3.Error as e:
            wx.MessageBox(f"Error fetching data: {e}.", "Error", wx.OK | wx.ICON_ERROR)
            return []

    def tcNikUpdate(self, event):
        self.tcNik.SetLabel(formatTime(self.tcNik.GetValue()))

    def dgRegistSimpanOnButtonClick(self, event):
        schema = {
            "nik": {
                "type": "integer",
                "required": True,
                "minlength": 1,
                "maxlength": 20,
            },
            "name": {
                "type": "string",
                "required": True,
                "min": 1,
                "max": 3599,
            },
        }
        validator = cerberus.Validator(schema)
        name = str(self.tcOpName.GetValue()).upper()
        data = {
            "op_name": name,
            "nik": self.tcNik.GetValue(),
            "name": self.tcOpName.GetValue(),
        }
        print(data)
        is_valid = validator.validate(data)
        if is_valid:
            # Check if color exists
            c.execute("SELECT id FROM operators WHERE name = ?", (name,))
            existing_id = c.fetchone()

            if existing_id:

                # Update nama yang sudah ada di database
                operators_id = existing_id[0]
                update_sql = """
                    UPDATE operators
                    SET nik = ?, name = ?
                    WHERE id = ?
                """
                c.execute(
                    update_sql,
                    (
                        data["nik"],
                        data["name"],
                        operators_id,
                    ),
                )
                wx.MessageBox(
                    f"Operatos with name '{name}' updated successfully!",
                    "Operators updated",
                    wx.OK | wx.ICON_INFORMATION,
                )
            else:
                # Simpan nama operator baru di database
                insert_sql = """
                    INSERT INTO operators (nik, name)
                    VALUES (?, ?)
                """
                c.execute(
                    insert_sql,
                    (
                        data["nik"],
                        data["name"],
                    ),
                )
                wx.MessageBox(
                    f"Operators with name '{name}' added successfully!",
                    "Operators added",
                    wx.OK | wx.ICON_INFORMATION,
                )
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
