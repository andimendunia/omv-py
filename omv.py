# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid
import sqlite3

###########################################################################
## Class dgColSelector
###########################################################################

conn = sqlite3.connect('omv.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS names (name TEXT)''')
conn.commit()

class frMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Open Mill Process Validator", pos = wx.DefaultPosition, size = wx.Size( 692,474 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Bahnschrift Light Condensed" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		self.conn = sqlite3.connect('omv.db')
		self.cursor = self.conn.cursor()

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_notebook9 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook9.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_notebook9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		self.pageMain = wx.Panel( self.m_notebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pageMain.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.pageMain.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer162 = wx.BoxSizer( wx.VERTICAL )

		bSizer531 = wx.BoxSizer( wx.VERTICAL )

		self.pageStep = wx.Panel( self.pageMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pageStep.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer73 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText40 = wx.StaticText( self.pageStep, wx.ID_ANY, u"01/02/2024", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText40.Wrap( -1 )

		self.m_staticText40.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Britannic Bold" ) )
		self.m_staticText40.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer73.Add( self.m_staticText40, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText42 = wx.StaticText( self.pageStep, wx.ID_ANY, u"11:12:43", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Britannic Bold" ) )
		self.m_staticText42.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer74.Add( self.m_staticText42, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer73.Add( bSizer74, 1, wx.EXPAND, 5 )


		bSizer30.Add( bSizer73, 1, wx.EXPAND, 5 )

		page_group1 = wx.BoxSizer( wx.VERTICAL )

		self.groupMain = wx.StaticText( self.pageStep, wx.ID_ANY, u"Group", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.groupMain.Wrap( -1 )

		self.groupMain.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		page_group1.Add( self.groupMain, 0, wx.ALL, 5 )

		choiceGroupMainChoices = [ u"A", u"B", u"C" ]
		self.choiceGroupMain = wx.Choice( self.pageStep, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGroupMainChoices, 0 )
		self.choiceGroupMain.SetSelection( 0 )
		self.choiceGroupMain.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		page_group1.Add( self.choiceGroupMain, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( page_group1, 0, wx.ALL|wx.EXPAND, 5 )

		page_op1 = wx.BoxSizer( wx.VERTICAL )

		self.op1Main = wx.StaticText( self.pageStep, wx.ID_ANY, u"Operator 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.op1Main.Wrap( -1 )

		self.op1Main.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		page_op1.Add( self.op1Main, 0, wx.ALL, 5 )

		cbOp1MainChoices = [ u"riski", u"lia", u"dianah", u"jelsi", u"bella", u"dio", u"edwin", u"mustofa" ]
		self.cbOp1Main = wx.ComboBox( self.pageStep, wx.ID_ANY, u"lia", wx.DefaultPosition, wx.DefaultSize, cbOp1MainChoices, 0 )
		self.cbOp1Main.SetSelection( 1 )
		self.cbOp1Main.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		page_op1.Add( self.cbOp1Main, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( page_op1, 1, wx.ALL|wx.EXPAND, 5 )

		page_op2 = wx.BoxSizer( wx.VERTICAL )

		self.op2Main = wx.StaticText( self.pageStep, wx.ID_ANY, u"Operator 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.op2Main.Wrap( -1 )

		self.op2Main.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		page_op2.Add( self.op2Main, 0, wx.ALL, 5 )

		cbOp2MainChoices = []
		self.cbOp2Main = wx.ComboBox( self.pageStep, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbOp2MainChoices, 0 )
		self.cbOp2Main.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		page_op2.Add( self.cbOp2Main, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( page_op2, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.lineMain = wx.StaticText( self.pageStep, wx.ID_ANY, u"Line", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lineMain.Wrap( -1 )

		self.lineMain.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer3.Add( self.lineMain, 0, wx.ALL, 5 )

		choiceLineMainChoices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9" ]
		self.choiceLineMain = wx.ComboBox( self.pageStep, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, choiceLineMainChoices, 0 )
		self.choiceLineMain.SetSelection( 0 )
		self.choiceLineMain.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer3.Add( self.choiceLineMain, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText36 = wx.StaticText( self.pageStep, wx.ID_ANY, u"No Batch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		self.m_staticText36.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer40.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.pageStep, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer40.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer40, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.latestBatch1 = wx.Panel( self.pageStep, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.latestBatch1.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer65 = wx.BoxSizer( wx.VERTICAL )

		self.latestBatch = wx.StaticText( self.latestBatch1, wx.ID_ANY, u"Latest batch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.latestBatch.Wrap( -1 )

		self.latestBatch.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer65.Add( self.latestBatch, 0, wx.ALL, 5 )


		bSizer65.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.resultLatestBatch = wx.StaticText( self.latestBatch1, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.resultLatestBatch.Wrap( -1 )

		self.resultLatestBatch.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer65.Add( self.resultLatestBatch, 0, wx.EXPAND, 5 )


		bSizer65.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.latestBatch1.SetSizer( bSizer65 )
		self.latestBatch1.Layout()
		bSizer65.Fit( self.latestBatch1 )
		bSizer41.Add( self.latestBatch1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( bSizer41, 0, wx.ALL|wx.EXPAND, 5 )


		self.pageStep.SetSizer( bSizer30 )
		self.pageStep.Layout()
		bSizer30.Fit( self.pageStep )
		bSizer531.Add( self.pageStep, 1, wx.ALL|wx.EXPAND, 0 )


		bSizer162.Add( bSizer531, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 4, 0, 0 )

		bSizer472 = wx.BoxSizer( wx.VERTICAL )

		self.panColMain = wx.Panel( self.pageMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panColMain.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.panColMain.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer123 = wx.BoxSizer( wx.VERTICAL )

		self.ColMain = wx.StaticText( self.panColMain, wx.ID_ANY, u"COLOR", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_DEFAULT )
		self.ColMain.Wrap( -1 )

		self.ColMain.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.ColMain.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ColMain.SetBackgroundColour( wx.Colour( 75, 66, 55 ) )

		bSizer123.Add( self.ColMain, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer123.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnColMain = wx.Button( self.panColMain, wx.ID_ANY, u"WHITE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnColMain.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.btnColMain.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer123.Add( self.btnColMain, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer123.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panColMain.SetSizer( bSizer123 )
		self.panColMain.Layout()
		bSizer123.Fit( self.panColMain )
		bSizer472.Add( self.panColMain, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer492 = wx.BoxSizer( wx.VERTICAL )

		bSizer501 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer53 = wx.BoxSizer( wx.VERTICAL )

		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		self.btnConnect = wx.Button( self.pageMain, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.btnConnect, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer55.Add( bSizer56, 1, wx.EXPAND, 5 )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		self.btnReset = wx.Button( self.pageMain, wx.ID_ANY, u" Reset ", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer57.Add( self.btnReset, 1, wx.ALL, 5 )


		bSizer55.Add( bSizer57, 0, wx.EXPAND, 5 )


		bSizer53.Add( bSizer55, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.BaudRate = wx.StaticText( self.pageMain, wx.ID_ANY, u"Baud Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BaudRate.Wrap( -1 )

		self.BaudRate.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer7.Add( self.BaudRate, 0, wx.ALL, 5 )

		choiceBaudRateChoices = []
		self.choiceBaudRate = wx.Choice( self.pageMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceBaudRateChoices, 0 )
		self.choiceBaudRate.SetSelection( 0 )
		gSizer7.Add( self.choiceBaudRate, 1, wx.ALL|wx.EXPAND, 5 )

		self.Port = wx.StaticText( self.pageMain, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Port.Wrap( -1 )

		self.Port.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer7.Add( self.Port, 1, wx.ALL, 5 )

		choicePortChoices = []
		self.choicePort = wx.Choice( self.pageMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePortChoices, 0 )
		self.choicePort.SetSelection( 0 )
		gSizer7.Add( self.choicePort, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( gSizer7, 0, wx.EXPAND, 5 )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer58.Add( gSizer71, 1, wx.EXPAND, 5 )

		self.StatusLoad = wx.StaticText( self.pageMain, wx.ID_ANY, u"Status Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StatusLoad.Wrap( -1 )

		self.StatusLoad.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer58.Add( self.StatusLoad, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnStatusLoad = wx.Button( self.pageMain, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnStatusLoad.SetBackgroundColour( wx.Colour( 81, 203, 32 ) )

		bSizer58.Add( self.btnStatusLoad, 1, wx.ALL, 5 )


		bSizer53.Add( bSizer58, 1, wx.EXPAND, 5 )

		bSizer581 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer711 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer581.Add( gSizer711, 1, wx.EXPAND, 5 )

		self.TotalTimeAct = wx.StaticText( self.pageMain, wx.ID_ANY, u"Total Time Act", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TotalTimeAct.Wrap( -1 )

		self.TotalTimeAct.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer581.Add( self.TotalTimeAct, 1, wx.ALL|wx.EXPAND, 5 )

		self.inpTotalTimeAct = wx.StaticText( self.pageMain, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpTotalTimeAct.Wrap( -1 )

		self.inpTotalTimeAct.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer581.Add( self.inpTotalTimeAct, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( bSizer581, 1, wx.EXPAND, 5 )

		bSizer551 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer551.Add( gSizer12, 1, wx.EXPAND, 5 )

		self.TimeTolerance = wx.StaticText( self.pageMain, wx.ID_ANY, u"Time Tolerance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TimeTolerance.Wrap( -1 )

		self.TimeTolerance.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer551.Add( self.TimeTolerance, 1, wx.ALL|wx.EXPAND, 5 )

		self.inpTimeTolerance = wx.StaticText( self.pageMain, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpTimeTolerance.Wrap( -1 )

		self.inpTimeTolerance.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer551.Add( self.inpTimeTolerance, 0, wx.ALL, 5 )


		bSizer53.Add( bSizer551, 1, wx.EXPAND, 5 )


		bSizer501.Add( bSizer53, 1, wx.EXPAND, 5 )


		bSizer492.Add( bSizer501, 1, wx.EXPAND, 5 )


		bSizer472.Add( bSizer492, 0, wx.EXPAND, 5 )


		gSizer5.Add( bSizer472, 1, wx.EXPAND, 5 )

		bSizer49 = wx.BoxSizer( wx.VERTICAL )

		self.panStep1 = wx.Panel( self.pageMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep1.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer421 = wx.BoxSizer( wx.VERTICAL )

		self.Step1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"STEP 1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Step1.Wrap( -1 )

		self.Step1.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.Step1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Step1.SetBackgroundColour( wx.Colour( 75, 66, 55 ) )

		bSizer421.Add( self.Step1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer421.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer75 = wx.BoxSizer( wx.VERTICAL )

		self.processStep1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"Masukkan material sebanyak 15 kg. Kemudian prsoes roll selama 120 detik (2 menit).\n\n\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.processStep1.Wrap( 150 )

		self.processStep1.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer75.Add( self.processStep1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer471 = wx.BoxSizer( wx.VERTICAL )


		bSizer75.Add( bSizer471, 1, wx.EXPAND, 5 )


		bSizer421.Add( bSizer75, 1, wx.EXPAND, 5 )


		bSizer421.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer61112 = wx.BoxSizer( wx.VERTICAL )

		self.btnCam1 = wx.BitmapButton( self.panStep1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnCam1.SetBitmap( wx.Bitmap( u"C:\\Users\\DELL\\Downloads\\omv\\icon camera.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCam1.SetBitmapDisabled( wx.Bitmap( u"C:\\Users\\DELL\\Downloads\\omv\\icon camera.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCam1.SetBitmapCurrent( wx.NullBitmap )
		bSizer61112.Add( self.btnCam1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Next1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"NEXT", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Next1.Wrap( -1 )

		self.Next1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.Next1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Next1.SetBackgroundColour( wx.Colour( 66, 62, 55 ) )

		bSizer61112.Add( self.Next1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.actTime1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.actTime1.Wrap( -1 )

		self.actTime1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.actTime1.SetForegroundColour( wx.Colour( 115, 107, 96 ) )

		bSizer61112.Add( self.actTime1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stdTime1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"04.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stdTime1.Wrap( -1 )

		self.stdTime1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer61112.Add( self.stdTime1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer421.Add( bSizer61112, 1, wx.EXPAND, 5 )


		self.panStep1.SetSizer( bSizer421 )
		self.panStep1.Layout()
		bSizer421.Fit( self.panStep1 )
		bSizer49.Add( self.panStep1, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer49, 1, wx.EXPAND, 5 )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.panStep2 = wx.Panel( self.pageMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep2.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.Step2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"STEP 2", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Step2.Wrap( -1 )

		self.Step2.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.Step2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Step2.SetBackgroundColour( wx.Colour( 75, 66, 55 ) )

		bSizer51.Add( self.Step2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer751 = wx.BoxSizer( wx.VERTICAL )

		self.processStep2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"Masukkan material sebanyak 15 kg, tambahkan pigment Regrind, Akselerator dan Sulfur. Kemudian proses roll selama 240 detik (4 menit)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.processStep2.Wrap( 150 )

		self.processStep2.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer751.Add( self.processStep2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer461 = wx.BoxSizer( wx.VERTICAL )


		bSizer751.Add( bSizer461, 1, wx.EXPAND, 5 )


		bSizer51.Add( bSizer751, 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer61111 = wx.BoxSizer( wx.VERTICAL )

		self.btnCam2 = wx.BitmapButton( self.panStep2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnCam2.SetBitmap( wx.Bitmap( u"C:\\Users\\DELL\\Downloads\\omv\\icon camera.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCam2.SetBitmapDisabled( wx.NullBitmap )
		bSizer61111.Add( self.btnCam2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Next2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"NEXT", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Next2.Wrap( -1 )

		self.Next2.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.Next2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Next2.SetBackgroundColour( wx.Colour( 66, 62, 55 ) )

		bSizer61111.Add( self.Next2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.actTime2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.actTime2.Wrap( -1 )

		self.actTime2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.actTime2.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer61111.Add( self.actTime2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer61111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stdTime2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"04.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stdTime2.Wrap( -1 )

		self.stdTime2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer61111.Add( self.stdTime2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer51.Add( bSizer61111, 1, wx.EXPAND, 5 )


		self.panStep2.SetSizer( bSizer51 )
		self.panStep2.Layout()
		bSizer51.Fit( self.panStep2 )
		bSizer43.Add( self.panStep2, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer43, 1, wx.EXPAND, 5 )

		bSizer491 = wx.BoxSizer( wx.VERTICAL )

		self.panStep3 = wx.Panel( self.pageMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep3.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.Step3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"STEP 3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Step3.Wrap( -1 )

		self.Step3.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.Step3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Step3.SetBackgroundColour( wx.Colour( 75, 66, 55 ) )

		bSizer52.Add( self.Step3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer52.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )


		bSizer52.Add( bSizer79, 1, wx.EXPAND, 5 )

		self.processStep3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"Masukkan campuran material sebanyak 45 kg. Tambahkan rework sebanyak 30%, lalu proses roll selama 660 detik. Jumlah total waktu yang dipakai 1020 detik (17 menit).\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.processStep3.Wrap( 170 )

		self.processStep3.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer52.Add( self.processStep3, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer52.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer6111 = wx.BoxSizer( wx.VERTICAL )

		self.btnCam3 = wx.BitmapButton( self.panStep3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnCam3.SetBitmap( wx.Bitmap( u"C:\\Users\\DELL\\Downloads\\omv\\icon camera.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCam3.SetBitmapDisabled( wx.NullBitmap )
		bSizer6111.Add( self.btnCam3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Next3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"FINISH", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Next3.Wrap( -1 )

		self.Next3.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.Next3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Next3.SetBackgroundColour( wx.Colour( 66, 62, 55 ) )

		bSizer6111.Add( self.Next3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.actNext3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.actNext3.Wrap( -1 )

		self.actNext3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.actNext3.SetForegroundColour( wx.Colour( 115, 107, 96 ) )

		bSizer6111.Add( self.actNext3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stdTime3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"04.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stdTime3.Wrap( -1 )

		self.stdTime3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer6111.Add( self.stdTime3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer52.Add( bSizer6111, 1, wx.EXPAND, 5 )


		self.panStep3.SetSizer( bSizer52 )
		self.panStep3.Layout()
		bSizer52.Fit( self.panStep3 )
		bSizer491.Add( self.panStep3, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer491, 1, wx.EXPAND, 5 )


		bSizer162.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.pageMain.SetSizer( bSizer162 )
		self.pageMain.Layout()
		bSizer162.Fit( self.pageMain )
		self.m_notebook9.AddPage( self.pageMain, u"Main", False )
		self.pageHistory = wx.Panel( self.m_notebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pageHistory.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer69 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer70 = wx.BoxSizer( wx.VERTICAL )

		self.groupHistory = wx.StaticText( self.pageHistory, wx.ID_ANY, u"Group", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.groupHistory.Wrap( -1 )

		self.groupHistory.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer70.Add( self.groupHistory, 0, wx.ALL, 5 )

		choiceGroupHisChoices = [ u"A", u"B", u"C", u"Saturday" ]
		self.choiceGroupHis = wx.Choice( self.pageHistory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGroupHisChoices, 0 )
		self.choiceGroupHis.SetSelection( 0 )
		bSizer70.Add( self.choiceGroupHis, 0, wx.ALL, 5 )

		self.m_staticText43 = wx.StaticText( self.pageHistory, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		bSizer70.Add( self.m_staticText43, 0, wx.ALL, 5 )

		m_choice6Choices = [ u"1", u"2", u"3" ]
		self.m_choice6 = wx.Choice( self.pageHistory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		bSizer70.Add( self.m_choice6, 0, wx.ALL, 5 )

		self.startDt1 = wx.StaticText( self.pageHistory, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startDt1.Wrap( -1 )

		self.startDt1.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer70.Add( self.startDt1, 0, wx.ALL, 5 )

		self.calStartDt1 = wx.adv.DatePickerCtrl( self.pageHistory, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		self.calStartDt1.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer70.Add( self.calStartDt1, 0, wx.ALL|wx.EXPAND, 5 )

		self.finishDt1 = wx.StaticText( self.pageHistory, wx.ID_ANY, u"Finish Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.finishDt1.Wrap( -1 )

		self.finishDt1.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer70.Add( self.finishDt1, 0, wx.ALL, 5 )

		self.calFinishDt1 = wx.adv.DatePickerCtrl( self.pageHistory, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		self.calFinishDt1.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer70.Add( self.calFinishDt1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.pageHistory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer70.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.btnSave1 = wx.Button( self.pageHistory, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnSave1.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer70.Add( self.btnSave1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer69.Add( bSizer70, 0, wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.tabHistory = wx.grid.Grid( self.pageHistory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabHistory.CreateGrid( 1000, 11 )
		self.tabHistory.EnableEditing( True )
		self.tabHistory.EnableGridLines( True )
		self.tabHistory.EnableDragGridSize( False )
		self.tabHistory.SetMargins( 0, 0 )

		# Columns
		self.tabHistory.SetColSize( 0, 160 )
		self.tabHistory.SetColSize( 1, 160 )
		self.tabHistory.SetColSize( 2, 160 )
		self.tabHistory.SetColSize( 3, 160 )
		self.tabHistory.SetColSize( 4, 160 )
		self.tabHistory.SetColSize( 5, 160 )
		self.tabHistory.SetColSize( 6, 160 )
		self.tabHistory.SetColSize( 7, 160 )
		self.tabHistory.SetColSize( 8, 160 )
		self.tabHistory.SetColSize( 9, 160 )
		self.tabHistory.SetColSize( 10, 160 )
		self.tabHistory.EnableDragColMove( False )
		self.tabHistory.EnableDragColSize( True )
		self.tabHistory.SetColLabelValue( 0, u"Group" )
		self.tabHistory.SetColLabelValue( 1, u"Operator 1" )
		self.tabHistory.SetColLabelValue( 2, u"Operator 2" )
		self.tabHistory.SetColLabelValue( 3, u"Color" )
		self.tabHistory.SetColLabelValue( 4, u"Start Date" )
		self.tabHistory.SetColLabelValue( 5, u"Finish Date" )
		self.tabHistory.SetColLabelValue( 6, u"Total Duration Batch" )
		self.tabHistory.SetColLabelValue( 7, u"Status" )
		self.tabHistory.SetColLabelValue( 8, u"Validation Step 1" )
		self.tabHistory.SetColLabelValue( 9, u"Validation Step 2" )
		self.tabHistory.SetColLabelValue( 10, u"Validation Step 3" )
		self.tabHistory.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
		self.tabHistory.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabHistory.AutoSizeRows()
		self.tabHistory.EnableDragRowSize( False )
		self.tabHistory.SetRowLabelSize( 1 )
		self.tabHistory.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabHistory.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabHistory.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer71.Add( self.tabHistory, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer69.Add( bSizer71, 1, wx.EXPAND, 5 )


		self.pageHistory.SetSizer( bSizer69 )
		self.pageHistory.Layout()
		bSizer69.Fit( self.pageHistory )
		self.m_notebook9.AddPage( self.pageHistory, u"History", False )
		self.pageSummary = wx.Panel( self.m_notebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pageSummary.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText44 = wx.StaticText( self.pageSummary, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		bSizer46.Add( self.m_staticText44, 0, wx.ALL, 5 )

		m_choice7Choices = [ u"1", u"2", u"3", u"Saturday" ]
		self.m_choice7 = wx.Choice( self.pageSummary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 0 )
		bSizer46.Add( self.m_choice7, 0, wx.ALL, 5 )

		self.startDt2 = wx.StaticText( self.pageSummary, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startDt2.Wrap( -1 )

		bSizer46.Add( self.startDt2, 0, wx.ALL, 5 )

		self.calStartDt2 = wx.adv.DatePickerCtrl( self.pageSummary, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer46.Add( self.calStartDt2, 0, wx.ALL, 5 )

		self.finishDt2 = wx.StaticText( self.pageSummary, wx.ID_ANY, u"Finish Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.finishDt2.Wrap( -1 )

		bSizer46.Add( self.finishDt2, 0, wx.ALL, 5 )

		self.calFinishDt2 = wx.adv.DatePickerCtrl( self.pageSummary, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer46.Add( self.calFinishDt2, 0, wx.ALL, 5 )

		self.mstaticline2 = wx.StaticLine( self.pageSummary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer46.Add( self.mstaticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.btnSave2 = wx.Button( self.pageSummary, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.btnSave2, 0, wx.ALL, 5 )


		bSizer45.Add( bSizer46, 0, wx.EXPAND, 5 )

		bSizer47 = wx.BoxSizer( wx.VERTICAL )

		self.tabSummary = wx.grid.Grid( self.pageSummary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabSummary.CreateGrid( 6, 4 )
		self.tabSummary.EnableEditing( True )
		self.tabSummary.EnableGridLines( True )
		self.tabSummary.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.tabSummary.EnableDragGridSize( False )
		self.tabSummary.SetMargins( 0, 0 )

		# Columns
		self.tabSummary.SetColSize( 0, 150 )
		self.tabSummary.SetColSize( 1, 150 )
		self.tabSummary.SetColSize( 2, 150 )
		self.tabSummary.SetColSize( 3, 150 )
		self.tabSummary.EnableDragColMove( False )
		self.tabSummary.EnableDragColSize( False )
		self.tabSummary.SetColLabelValue( 0, u" " )
		self.tabSummary.SetColLabelValue( 1, u"A" )
		self.tabSummary.SetColLabelValue( 2, u"B" )
		self.tabSummary.SetColLabelValue( 3, u"C" )
		self.tabSummary.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
		self.tabSummary.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabSummary.SetRowSize( 0, 100 )
		self.tabSummary.SetRowSize( 1, 100 )
		self.tabSummary.SetRowSize( 2, 100 )
		self.tabSummary.SetRowSize( 3, 100 )
		self.tabSummary.SetRowSize( 4, 100 )
		self.tabSummary.SetRowSize( 5, 100 )
		self.tabSummary.EnableDragRowSize( False )
		self.tabSummary.SetRowLabelValue( 0, u"OK" )
		self.tabSummary.SetRowLabelValue( 1, u"OK (Finish Pressed)" )
		self.tabSummary.SetRowLabelValue( 2, u"LESS" )
		self.tabSummary.SetRowLabelValue( 3, u"LESS (Finish Pressed)" )
		self.tabSummary.SetRowLabelValue( 4, u"OVER" )
		self.tabSummary.SetRowLabelValue( 5, u"OVER (Finish Pressed)" )
		self.tabSummary.SetRowLabelSize( 1 )
		self.tabSummary.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabSummary.SetLabelFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		# Cell Defaults
		self.tabSummary.SetDefaultCellFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tabSummary.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabSummary.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.tabSummary.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer47.Add( self.tabSummary, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer45.Add( bSizer47, 0, wx.EXPAND, 5 )


		self.pageSummary.SetSizer( bSizer45 )
		self.pageSummary.Layout()
		bSizer45.Fit( self.pageSummary )
		self.m_notebook9.AddPage( self.pageSummary, u"Summary", False )
		self.panRecipes = wx.Panel( self.m_notebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panRecipes.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer119 = wx.BoxSizer( wx.VERTICAL )

		bSizer120 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer121 = wx.BoxSizer( wx.VERTICAL )

		m_choice21Choices = [ u"White", u"Color", u"Regrind" ]
		self.m_choice21 = wx.Choice( self.panRecipes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice21Choices, 0 )
		self.m_choice21.SetSelection( 0 )
		bSizer121.Add( self.m_choice21, 0, wx.ALL, 15 )


		bSizer120.Add( bSizer121, 1, wx.EXPAND, 5 )

		bSizer122 = wx.BoxSizer( wx.VERTICAL )

		self.m_button29 = wx.Button( self.panRecipes, wx.ID_ANY, u"+ Create New", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer122.Add( self.m_button29, 0, wx.ALIGN_RIGHT|wx.ALL, 15 )


		bSizer120.Add( bSizer122, 1, wx.EXPAND, 5 )


		bSizer119.Add( bSizer120, 0, wx.EXPAND, 5 )

		bSizer1231 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid6 = wx.grid.Grid( self.panRecipes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SUNKEN )

		# Grid
		self.m_grid6.CreateGrid( 3, 3 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.SetColSize( 0, 235 )
		self.m_grid6.SetColSize( 1, 235 )
		self.m_grid6.SetColSize( 2, 235 )
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelValue( 0, u"Step 1" )
		self.m_grid6.SetColLabelValue( 1, u"Step 2" )
		self.m_grid6.SetColLabelValue( 2, u"Step 3" )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.SetRowSize( 0, 150 )
		self.m_grid6.SetRowSize( 1, 60 )
		self.m_grid6.SetRowSize( 2, 60 )
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelValue( 0, u"Description" )
		self.m_grid6.SetRowLabelValue( 1, u"Time" )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_grid6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1231.Add( self.m_grid6, 0, wx.ALL, 15 )


		bSizer119.Add( bSizer1231, 1, wx.EXPAND, 5 )

		bSizer124 = wx.BoxSizer( wx.VERTICAL )

		self.m_button30 = wx.Button( self.panRecipes, wx.ID_ANY, u"Save Changes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer124.Add( self.m_button30, 0, wx.ALIGN_RIGHT|wx.ALL, 15 )


		bSizer119.Add( bSizer124, 0, wx.EXPAND, 5 )


		self.panRecipes.SetSizer( bSizer119 )
		self.panRecipes.Layout()
		bSizer119.Fit( self.panRecipes )
		self.m_notebook9.AddPage( self.panRecipes, u"Recipes", False )
		self.panOperator = wx.Panel( self.m_notebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panOperator.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer582 = wx.BoxSizer( wx.VERTICAL )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer68 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid5 = wx.grid.Grid( self.panOperator, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid5.CreateGrid( 18, 1 )
		self.m_grid5.EnableEditing( True )
		self.m_grid5.EnableGridLines( True )
		self.m_grid5.EnableDragGridSize( False )
		self.m_grid5.SetMargins( 0, 0 )

		# Columns
		self.m_grid5.SetColSize( 0, 203 )
		self.m_grid5.EnableDragColMove( False )
		self.m_grid5.EnableDragColSize( True )
		self.m_grid5.SetColLabelValue( 0, u"Operator Name" )
		self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid5.EnableDragRowSize( True )
		self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer68.Add( self.m_grid5, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer6.Add( bSizer68, 1, wx.EXPAND, 5 )

		bSizer691 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl5 = wx.TextCtrl( self.panOperator, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer691.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

		self.load_data()

		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button26 = wx.Button( self.panOperator, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_button26, 1, wx.ALL, 5 )

		self.m_button27 = wx.Button( self.panOperator, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_button27, 1, wx.ALL, 5 )


		bSizer691.Add( bSizer711, 1, wx.EXPAND, 5 )


		gSizer6.Add( bSizer691, 1, wx.EXPAND, 5 )


		bSizer66.Add( gSizer6, 1, wx.EXPAND, 5 )


		bSizer582.Add( bSizer66, 1, wx.EXPAND, 5 )


		self.panOperator.SetSizer( bSizer582 )
		self.panOperator.Layout()
		bSizer582.Fit( self.panOperator )
		self.m_notebook9.AddPage( self.panOperator, u"Operators", True )

		bSizer36.Add( self.m_notebook9, 1, wx.ALL|wx.EXPAND, 10 )


		bSizer35.Add( bSizer36, 1, wx.EXPAND, 5 )


		bSizer29.Add( bSizer35, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.op2Main.Bind( wx.EVT_CHAR, self.op2MainOnChar )
		self.choiceLineMain.Bind( wx.EVT_COMBOBOX, self.choiceLineMainOnCombobox )
		self.btnColMain.Bind( wx.EVT_BUTTON, self.btn_colorOnButtonClick )
		self.btnConnect.Bind( wx.EVT_BUTTON, self.btn_connectOnButtonClick )
		self.btnReset.Bind( wx.EVT_BUTTON, self.btn_resetOnButtonClick )
		self.btnStatusLoad.Bind( wx.EVT_BUTTON, self.btn_indicatorOnButtonClick )
		self.btnSave1.Bind( wx.EVT_BUTTON, self.btn_save1OnButtonClick )
		self.m_button27.Bind(wx.EVT_BUTTON, self.create_operator)

	def load_data(self):
		# self.m_grid5.CreateGrid(0,0)
		self.cursor.execute("SELECT * FROM names")
		rows = self.cursor.fetchall()

		self.m_grid5.ClearGrid()

		self.m_grid5.AppendCols(len(rows[0]))
		self.m_grid5.AppendRows(len(rows))

		for i, row in enumerate(rows):
			for j, value in enumerate(row):
				self.m_grid5.SetCellValue(i, j, str(value))

	def create_operator(self, event):
		cursor.execute("INSERT INTO names (name) VALUES (?)", (self.m_textCtrl5.GetValue(),))
		conn.commit()

		cursor.close()
		conn.close()

		self.load_data()
        

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def op2MainOnChar( self, event ):
		event.Skip()

	def choiceLineMainOnCombobox( self, event ):
		event.Skip()

	def btn_colorOnButtonClick( self, event ):
		event.Skip()

	def btn_connectOnButtonClick( self, event ):
		event.Skip()

	def btn_resetOnButtonClick( self, event ):
		event.Skip()

	def btn_indicatorOnButtonClick( self, event ):
		event.Skip()

	def btn_save1OnButtonClick( self, event ):
		event.Skip()



	
if __name__ == '__main__':
	app = wx.App()
	frame = frMain(None)
	frame.Show()
	app.MainLoop()
