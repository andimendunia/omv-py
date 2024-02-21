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

###########################################################################
## Class frMain
###########################################################################

class frMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Open Mill Process Validator", pos = wx.DefaultPosition, size = wx.Size( 943,566 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.nbMain = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.nbMain.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		self.panHome = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panHome.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer162 = wx.BoxSizer( wx.VERTICAL )

		bSizer531 = wx.BoxSizer( wx.VERTICAL )

		bSizer83 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer761 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText66 = wx.StaticText( self.panHome, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )

		bSizer761.Add( self.m_staticText66, 0, wx.ALL, 5 )

		chHomeShiftChoices = [ wx.EmptyString, u"1", u"2", u"3", u"Saturday" ]
		self.chHomeShift = wx.Choice( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), chHomeShiftChoices, 0 )
		self.chHomeShift.SetSelection( 4 )
		bSizer761.Add( self.chHomeShift, 0, wx.ALL, 5 )


		bSizer83.Add( bSizer761, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer7611 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText661 = wx.StaticText( self.panHome, wx.ID_ANY, u"Group", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText661.Wrap( -1 )

		bSizer7611.Add( self.m_staticText661, 0, wx.ALL, 5 )

		chHomeGroupChoices = [ wx.EmptyString, u"A", u"B", u"C" ]
		self.chHomeGroup = wx.Choice( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), chHomeGroupChoices, 0 )
		self.chHomeGroup.SetSelection( 1 )
		bSizer7611.Add( self.chHomeGroup, 0, wx.ALL, 5 )


		bSizer83.Add( bSizer7611, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer7612 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText662 = wx.StaticText( self.panHome, wx.ID_ANY, u"Operator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText662.Wrap( -1 )

		bSizer7612.Add( self.m_staticText662, 0, wx.ALL, 5 )

		bSizer821 = wx.BoxSizer( wx.HORIZONTAL )

		chHomeOp1Choices = []
		self.chHomeOp1 = wx.ComboBox( self.panHome, wx.ID_ANY, u"MUTMAENAH", wx.DefaultPosition, wx.Size( 200,-1 ), chHomeOp1Choices, 0 )
		bSizer821.Add( self.chHomeOp1, 0, wx.ALL, 5 )

		chHomeOp2Choices = []
		self.chHomeOp2 = wx.ComboBox( self.panHome, wx.ID_ANY, u"SUSILAWATI", wx.DefaultPosition, wx.Size( 200,-1 ), chHomeOp2Choices, 0 )
		bSizer821.Add( self.chHomeOp2, 0, wx.ALL, 5 )


		bSizer7612.Add( bSizer821, 1, wx.EXPAND, 5 )


		bSizer83.Add( bSizer7612, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer82 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText72 = wx.StaticText( self.panHome, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		bSizer82.Add( self.m_staticText72, 0, wx.ALL, 5 )


		bSizer83.Add( bSizer82, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.lineMain = wx.StaticText( self.panHome, wx.ID_ANY, u"Line", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lineMain.Wrap( -1 )

		bSizer3.Add( self.lineMain, 0, wx.ALL, 5 )

		chHomeLineChoices = [ u" ", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9" ]
		self.chHomeLine = wx.Choice( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chHomeLineChoices, 0 )
		self.chHomeLine.SetSelection( 0 )
		bSizer3.Add( self.chHomeLine, 0, wx.ALL, 5 )


		bSizer83.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText36 = wx.StaticText( self.panHome, wx.ID_ANY, u"Batch no.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		bSizer40.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.tcHomeBatch = wx.TextCtrl( self.panHome, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		bSizer40.Add( self.tcHomeBatch, 0, wx.ALL, 5 )


		bSizer83.Add( bSizer40, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer401 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText361 = wx.StaticText( self.panHome, wx.ID_ANY, u"Last batch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )

		bSizer401.Add( self.m_staticText361, 0, wx.ALL, 5 )

		bSizer103 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel11 = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer105 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer106 = wx.BoxSizer( wx.HORIZONTAL )

		self.stHomeLatestBatch = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Under standard", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		self.stHomeLatestBatch.Wrap( -1 )

		bSizer106.Add( self.stHomeLatestBatch, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer105.Add( bSizer106, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )


		self.m_panel11.SetSizer( bSizer105 )
		self.m_panel11.Layout()
		bSizer105.Fit( self.m_panel11 )
		bSizer103.Add( self.m_panel11, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer401.Add( bSizer103, 1, wx.EXPAND, 5 )


		bSizer83.Add( bSizer401, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer531.Add( bSizer83, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer162.Add( bSizer531, 0, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 4, 0, 0 )

		bSizer472 = wx.BoxSizer( wx.VERTICAL )

		self.panColMain = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panColMain.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer123 = wx.BoxSizer( wx.VERTICAL )

		bSizer961 = wx.BoxSizer( wx.VERTICAL )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText55 = wx.StaticText( self.panColMain, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		bSizer80.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bmColor = wx.StaticBitmap( self.panColMain, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.bmColor, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )


		bSizer961.Add( bSizer80, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer822 = wx.BoxSizer( wx.VERTICAL )

		self.btnHomeCol = wx.Button( self.panColMain, wx.ID_ANY, u"WHITE", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		bSizer822.Add( self.btnHomeCol, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )

		self.btnStart = wx.Button( self.panColMain, wx.ID_ANY, u"Manual start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer822.Add( self.btnStart, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer822.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer961.Add( bSizer822, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer123.Add( bSizer961, 1, wx.ALL|wx.EXPAND, 5 )


		self.panColMain.SetSizer( bSizer123 )
		self.panColMain.Layout()
		bSizer123.Fit( self.panColMain )
		bSizer472.Add( self.panColMain, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer492 = wx.BoxSizer( wx.VERTICAL )

		bSizer53 = wx.BoxSizer( wx.VERTICAL )

		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		self.btnHomeConnect = wx.Button( self.panHome, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.btnHomeConnect, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer55.Add( bSizer56, 1, wx.EXPAND, 5 )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )


		bSizer55.Add( bSizer57, 0, wx.EXPAND, 5 )


		bSizer53.Add( bSizer55, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 3, 0, 0 )

		self.Port = wx.StaticText( self.panHome, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Port.Wrap( -1 )

		gSizer7.Add( self.Port, 1, wx.ALL, 5 )

		chHomePortChoices = []
		self.chHomePort = wx.Choice( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chHomePortChoices, 0 )
		self.chHomePort.SetSelection( 0 )
		gSizer7.Add( self.chHomePort, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnHomeReset = wx.Button( self.panHome, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.btnHomeReset, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( gSizer7, 0, wx.EXPAND, 5 )

		bSizer581 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer711 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer581.Add( gSizer711, 1, wx.EXPAND, 5 )

		self.ElapsedTime = wx.StaticText( self.panHome, wx.ID_ANY, u"Elapsed time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ElapsedTime.Wrap( -1 )

		bSizer581.Add( self.ElapsedTime, 1, wx.ALL|wx.EXPAND, 5 )

		self.stHomeElapsed = wx.StaticText( self.panHome, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stHomeElapsed.Wrap( -1 )

		bSizer581.Add( self.stHomeElapsed, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( bSizer581, 1, wx.EXPAND, 5 )

		bSizer551 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer551.Add( gSizer12, 1, wx.EXPAND, 5 )

		self.TimeTolerance = wx.StaticText( self.panHome, wx.ID_ANY, u"Time Tolerance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TimeTolerance.Wrap( -1 )

		bSizer551.Add( self.TimeTolerance, 1, wx.ALL|wx.EXPAND, 5 )

		self.inpHomeTimeTolerance = wx.StaticText( self.panHome, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpHomeTimeTolerance.Wrap( -1 )

		bSizer551.Add( self.inpHomeTimeTolerance, 0, wx.ALL, 5 )


		bSizer53.Add( bSizer551, 1, wx.EXPAND, 5 )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer58.Add( gSizer71, 1, wx.EXPAND, 5 )

		self.StatusLoad = wx.StaticText( self.panHome, wx.ID_ANY, u"Status Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StatusLoad.Wrap( -1 )

		bSizer58.Add( self.StatusLoad, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnHomeStatusLoad = wx.Button( self.panHome, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnHomeStatusLoad.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer58.Add( self.btnHomeStatusLoad, 1, wx.ALL, 5 )


		bSizer53.Add( bSizer58, 1, wx.EXPAND, 5 )


		bSizer492.Add( bSizer53, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer472.Add( bSizer492, 0, wx.EXPAND, 5 )


		gSizer5.Add( bSizer472, 1, wx.EXPAND, 5 )

		bSizer49 = wx.BoxSizer( wx.VERTICAL )

		self.panStep1 = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep1.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer421 = wx.BoxSizer( wx.VERTICAL )

		bSizer97 = wx.BoxSizer( wx.VERTICAL )

		bSizer831 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText56 = wx.StaticText( self.panStep1, wx.ID_ANY, u"Step", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		bSizer831.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bmStep1 = wx.StaticBitmap( self.panStep1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer831.Add( self.bmStep1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )


		bSizer97.Add( bSizer831, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer75 = wx.BoxSizer( wx.VERTICAL )

		self.stHomeStdTime1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"04:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stHomeStdTime1.Wrap( -1 )

		bSizer75.Add( self.stHomeStdTime1, 0, wx.ALL, 5 )

		self.stHomeDesc1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"Masukkan material sebanyak 15 kg. Kemudian prsoes roll selama 120 detik (2 menit).", wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE )
		self.stHomeDesc1.Wrap( 0 )

		bSizer75.Add( self.stHomeDesc1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer97.Add( bSizer75, 2, wx.ALL|wx.EXPAND, 10 )

		bSizer61112 = wx.BoxSizer( wx.VERTICAL )

		bSizer87 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnHomeCam1 = wx.BitmapButton( self.panStep1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnHomeCam1.SetBitmap( wx.NullBitmap )
		self.btnHomeCam1.SetBitmapDisabled( wx.NullBitmap )
		self.btnHomeCam1.SetBitmapCurrent( wx.NullBitmap )
		self.btnHomeCam1.SetBitmapPosition( wx.BOTTOM )
		bSizer87.Add( self.btnHomeCam1, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer87.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stHomeTime1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stHomeTime1.Wrap( -1 )

		bSizer87.Add( self.stHomeTime1, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer61112.Add( bSizer87, 1, wx.EXPAND, 5 )

		self.gHome1 = wx.Gauge( self.panStep1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gHome1.SetValue( 0 )
		bSizer61112.Add( self.gHome1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button16 = wx.Button( self.panStep1, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		bSizer61112.Add( self.m_button16, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer97.Add( bSizer61112, 1, wx.EXPAND, 5 )


		bSizer421.Add( bSizer97, 1, wx.ALL|wx.EXPAND, 5 )


		self.panStep1.SetSizer( bSizer421 )
		self.panStep1.Layout()
		bSizer421.Fit( self.panStep1 )
		bSizer49.Add( self.panStep1, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer49, 1, wx.EXPAND, 5 )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.panStep2 = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep2.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		bSizer98 = wx.BoxSizer( wx.VERTICAL )

		bSizer8311 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText57 = wx.StaticText( self.panStep2, wx.ID_ANY, u"Step", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		bSizer8311.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bmStep2 = wx.StaticBitmap( self.panStep2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8311.Add( self.bmStep2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )


		bSizer98.Add( bSizer8311, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer751 = wx.BoxSizer( wx.VERTICAL )

		self.stHomeStdTime2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"04:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stHomeStdTime2.Wrap( -1 )

		bSizer751.Add( self.stHomeStdTime2, 0, wx.ALL, 5 )

		self.stHomeDesc2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"Masukkan material sebanyak 15 kg, tambahkan pigment Regrind, Akselerator dan Sulfur. Kemudian proses roll selama 240 detik (4 menit)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
		self.stHomeDesc2.Wrap( 0 )

		bSizer751.Add( self.stHomeDesc2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer98.Add( bSizer751, 2, wx.ALL|wx.EXPAND, 10 )

		bSizer611121 = wx.BoxSizer( wx.VERTICAL )

		bSizer871 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnHomeCam2 = wx.BitmapButton( self.panStep2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnHomeCam2.SetBitmap( wx.NullBitmap )
		self.btnHomeCam2.SetBitmapDisabled( wx.NullBitmap )
		self.btnHomeCam2.SetBitmapCurrent( wx.NullBitmap )
		self.btnHomeCam2.SetBitmapPosition( wx.BOTTOM )
		bSizer871.Add( self.btnHomeCam2, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer871.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stHomeTime2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stHomeTime2.Wrap( -1 )

		bSizer871.Add( self.stHomeTime2, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer611121.Add( bSizer871, 1, wx.EXPAND, 5 )

		self.gHome2 = wx.Gauge( self.panStep2, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gHome2.SetValue( 0 )
		bSizer611121.Add( self.gHome2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button161 = wx.Button( self.panStep2, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		bSizer611121.Add( self.m_button161, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer98.Add( bSizer611121, 1, wx.EXPAND, 5 )


		bSizer51.Add( bSizer98, 1, wx.ALL|wx.EXPAND, 5 )


		self.panStep2.SetSizer( bSizer51 )
		self.panStep2.Layout()
		bSizer51.Fit( self.panStep2 )
		bSizer43.Add( self.panStep2, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer43, 1, wx.EXPAND, 5 )

		bSizer491 = wx.BoxSizer( wx.VERTICAL )

		self.panStep3 = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep3.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		bSizer99 = wx.BoxSizer( wx.VERTICAL )

		bSizer8312 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText58 = wx.StaticText( self.panStep3, wx.ID_ANY, u"Step", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		bSizer8312.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bmStep3 = wx.StaticBitmap( self.panStep3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8312.Add( self.bmStep3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )


		bSizer99.Add( bSizer8312, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		self.stHomeStdTime3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"04:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stHomeStdTime3.Wrap( -1 )

		bSizer79.Add( self.stHomeStdTime3, 0, wx.ALL, 5 )

		self.stHomeDesc3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"Masukkan campuran material sebanyak 45 kg. Tambahkan rework sebanyak 30%, lalu proses roll selama 660 detik. Jumlah total waktu yang dipakai 1020 detik (17 menit).\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
		self.stHomeDesc3.Wrap( 0 )

		bSizer79.Add( self.stHomeDesc3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer99.Add( bSizer79, 2, wx.ALL|wx.EXPAND, 10 )

		bSizer611122 = wx.BoxSizer( wx.VERTICAL )

		bSizer8711 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnHomeCam3 = wx.BitmapButton( self.panStep3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnHomeCam3.SetBitmap( wx.NullBitmap )
		self.btnHomeCam3.SetBitmapDisabled( wx.NullBitmap )
		self.btnHomeCam3.SetBitmapCurrent( wx.NullBitmap )
		self.btnHomeCam3.SetBitmapPosition( wx.BOTTOM )
		bSizer8711.Add( self.btnHomeCam3, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer8711.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stHomeTime3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stHomeTime3.Wrap( -1 )

		bSizer8711.Add( self.stHomeTime3, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer611122.Add( bSizer8711, 1, wx.EXPAND, 5 )

		self.gHome3 = wx.Gauge( self.panStep3, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gHome3.SetValue( 0 )
		bSizer611122.Add( self.gHome3, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnHomeFinish = wx.Button( self.panStep3, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		bSizer611122.Add( self.btnHomeFinish, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer99.Add( bSizer611122, 1, wx.EXPAND, 5 )


		bSizer52.Add( bSizer99, 1, wx.ALL|wx.EXPAND, 5 )


		self.panStep3.SetSizer( bSizer52 )
		self.panStep3.Layout()
		bSizer52.Fit( self.panStep3 )
		bSizer491.Add( self.panStep3, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer491, 1, wx.EXPAND, 5 )


		bSizer162.Add( gSizer5, 1, wx.ALL|wx.EXPAND, 5 )


		self.panHome.SetSizer( bSizer162 )
		self.panHome.Layout()
		bSizer162.Fit( self.panHome )
		self.nbMain.AddPage( self.panHome, u"Home", False )
		self.panRecords = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panRecords.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer69 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer70 = wx.BoxSizer( wx.VERTICAL )

		bSizer88 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText43 = wx.StaticText( self.panRecords, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		bSizer88.Add( self.m_staticText43, 0, wx.ALL, 5 )

		chRecordsShiftChoices = [ u" ", u"1", u"2", u"3", u"Saturday" ]
		self.chRecordsShift = wx.Choice( self.panRecords, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chRecordsShiftChoices, 0 )
		self.chRecordsShift.SetSelection( 0 )
		bSizer88.Add( self.chRecordsShift, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer70.Add( bSizer88, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer89 = wx.BoxSizer( wx.VERTICAL )

		self.startDt1 = wx.StaticText( self.panRecords, wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startDt1.Wrap( -1 )

		bSizer89.Add( self.startDt1, 0, wx.ALL, 5 )

		self.calRecordsStartDt1 = wx.adv.DatePickerCtrl( self.panRecords, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN )
		bSizer89.Add( self.calRecordsStartDt1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer70.Add( bSizer89, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer90 = wx.BoxSizer( wx.VERTICAL )

		self.finishDt1 = wx.StaticText( self.panRecords, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.finishDt1.Wrap( -1 )

		bSizer90.Add( self.finishDt1, 0, wx.ALL, 5 )

		self.calRecordsFinishDt1 = wx.adv.DatePickerCtrl( self.panRecords, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN )
		bSizer90.Add( self.calRecordsFinishDt1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer70.Add( bSizer90, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText70 = wx.StaticText( self.panRecords, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )

		bSizer91.Add( self.m_staticText70, 0, wx.ALL, 5 )

		self.btnRecordsApply = wx.Button( self.panRecords, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		bSizer91.Add( self.btnRecordsApply, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer70.Add( bSizer91, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer69.Add( bSizer70, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.lcRecords = wx.ListCtrl( self.panRecords, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
		bSizer71.Add( self.lcRecords, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer69.Add( bSizer71, 1, wx.ALL|wx.EXPAND, 5 )


		self.panRecords.SetSizer( bSizer69 )
		self.panRecords.Layout()
		bSizer69.Fit( self.panRecords )
		self.nbMain.AddPage( self.panRecords, u"Records", False )
		self.panSummary = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panSummary.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		bSizer93 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText44 = wx.StaticText( self.panSummary, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		bSizer93.Add( self.m_staticText44, 0, wx.ALL, 5 )

		chSumShiftChoices = [ u" ", u"1", u"2", u"3", u"Saturday" ]
		self.chSumShift = wx.Choice( self.panSummary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chSumShiftChoices, 0 )
		self.chSumShift.SetSelection( 0 )
		bSizer93.Add( self.chSumShift, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer46.Add( bSizer93, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer94 = wx.BoxSizer( wx.VERTICAL )

		self.startDt2 = wx.StaticText( self.panSummary, wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startDt2.Wrap( -1 )

		bSizer94.Add( self.startDt2, 0, wx.ALL, 5 )

		self.calSumStartDt2 = wx.adv.DatePickerCtrl( self.panSummary, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN )
		bSizer94.Add( self.calSumStartDt2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer46.Add( bSizer94, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer95 = wx.BoxSizer( wx.VERTICAL )

		self.finishDt2 = wx.StaticText( self.panSummary, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.finishDt2.Wrap( -1 )

		bSizer95.Add( self.finishDt2, 0, wx.ALL, 5 )

		self.calSumFinishDt2 = wx.adv.DatePickerCtrl( self.panSummary, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN )
		bSizer95.Add( self.calSumFinishDt2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer46.Add( bSizer95, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer96 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText71 = wx.StaticText( self.panSummary, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		bSizer96.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.btnSumApply = wx.Button( self.panSummary, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		bSizer96.Add( self.btnSumApply, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer46.Add( bSizer96, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer45.Add( bSizer46, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer47 = wx.BoxSizer( wx.VERTICAL )

		self.lcSum = wx.ListCtrl( self.panSummary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_VRULES )
		bSizer47.Add( self.lcSum, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer45.Add( bSizer47, 1, wx.ALL|wx.EXPAND, 5 )


		self.panSummary.SetSizer( bSizer45 )
		self.panSummary.Layout()
		bSizer45.Fit( self.panSummary )
		self.nbMain.AddPage( self.panSummary, u"Summary", False )
		self.panTimeTolerance = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panTimeTolerance.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer991 = wx.BoxSizer( wx.VERTICAL )

		self.m_listbook1 = wx.Listbook( self.panTimeTolerance, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.panSetBasic = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		bSizer1172 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText752 = wx.StaticText( self.panSetBasic, wx.ID_ANY, u"General", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText752.Wrap( -1 )

		bSizer1172.Add( self.m_staticText752, 0, wx.ALL, 5 )


		bSizer60.Add( bSizer1172, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.panSetBasic, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		bSizer127 = wx.BoxSizer( wx.VERTICAL )

		bSizer573 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8311 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Line count", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8311.Wrap( -1 )

		bSizer573.Add( self.m_staticText8311, 0, wx.ALL, 5 )

		self.scGenLineCount = wx.SpinCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 3599, 0 )
		bSizer573.Add( self.scGenLineCount, 0, wx.ALL, 5 )


		bSizer127.Add( bSizer573, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer572 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText83 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Time tolerance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		bSizer572.Add( self.m_staticText83, 0, wx.ALL, 5 )

		bSizer128 = wx.BoxSizer( wx.HORIZONTAL )

		self.scGenTimeTol = wx.SpinCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 3599, 1 )
		bSizer128.Add( self.scGenTimeTol, 0, wx.ALL, 5 )

		self.m_staticText463 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText463.Wrap( -1 )

		bSizer128.Add( self.m_staticText463, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer572.Add( bSizer128, 1, wx.EXPAND, 5 )


		bSizer127.Add( bSizer572, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer571 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText831 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Baud rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText831.Wrap( -1 )

		bSizer571.Add( self.m_staticText831, 0, wx.ALL, 5 )

		chGenBaudChoices = [ u" ", u"2400", u"4800", u"9600", u"19200", u"38400", u"57600", u"115200" ]
		self.chGenBaud = wx.Choice( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), chGenBaudChoices, 0 )
		self.chGenBaud.SetSelection( 2 )
		bSizer571.Add( self.chGenBaud, 0, wx.ALL, 5 )


		bSizer127.Add( bSizer571, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer11.Add( bSizer127, 1, wx.EXPAND, 5 )

		bSizer73 = wx.BoxSizer( wx.VERTICAL )

		self.btnGenSave = wx.Button( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer73.Add( self.btnGenSave, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer11.Add( bSizer73, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer66.Add( sbSizer11, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer60.Add( bSizer66, 1, wx.EXPAND, 5 )


		self.panSetBasic.SetSizer( bSizer60 )
		self.panSetBasic.Layout()
		bSizer60.Fit( self.panSetBasic )
		self.m_listbook1.AddPage( self.panSetBasic, u"General", False )
		self.panSetRecipes = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer119 = wx.BoxSizer( wx.VERTICAL )

		bSizer117 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText75 = wx.StaticText( self.panSetRecipes, wx.ID_ANY, u"Recipes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		bSizer117.Add( self.m_staticText75, 0, wx.ALL, 5 )


		bSizer119.Add( bSizer117, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer120 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer651 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnRecCreate = wx.Button( self.panSetRecipes, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer651.Add( self.btnRecCreate, 0, wx.ALL, 5 )

		self.btnRecEdit = wx.Button( self.panSetRecipes, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer651.Add( self.btnRecEdit, 0, wx.ALL, 5 )

		self.btnRecDelete = wx.Button( self.panSetRecipes, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer651.Add( self.btnRecDelete, 0, wx.ALL, 5 )


		bSizer120.Add( bSizer651, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer68 = wx.BoxSizer( wx.VERTICAL )

		self.btnRecRefresh = wx.Button( self.panSetRecipes, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.btnRecRefresh, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer120.Add( bSizer68, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer119.Add( bSizer120, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer1231 = wx.BoxSizer( wx.VERTICAL )

		self.lcRecipes = wx.ListCtrl( self.panSetRecipes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		bSizer1231.Add( self.lcRecipes, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer119.Add( bSizer1231, 1, wx.ALL|wx.EXPAND, 5 )


		self.panSetRecipes.SetSizer( bSizer119 )
		self.panSetRecipes.Layout()
		bSizer119.Fit( self.panSetRecipes )
		self.m_listbook1.AddPage( self.panSetRecipes, u"Recipes", True )
		self.panSetOperators = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer582 = wx.BoxSizer( wx.VERTICAL )

		bSizer1171 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText751 = wx.StaticText( self.panSetOperators, wx.ID_ANY, u"Operators", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText751.Wrap( -1 )

		bSizer1171.Add( self.m_staticText751, 0, wx.ALL, 5 )


		bSizer582.Add( bSizer1171, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer76 = wx.BoxSizer( wx.HORIZONTAL )

		btnOpCreate1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnOpCreate = wx.Button( self.panSetOperators, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		btnOpCreate1.Add( self.btnOpCreate, 0, wx.ALL, 5 )

		self.btnOpDelete = wx.Button( self.panSetOperators, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		btnOpCreate1.Add( self.btnOpDelete, 0, wx.ALL, 5 )


		bSizer76.Add( btnOpCreate1, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer701 = wx.BoxSizer( wx.VERTICAL )

		self.btnOpRefresh = wx.Button( self.panSetOperators, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer701.Add( self.btnOpRefresh, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer76.Add( bSizer701, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer582.Add( bSizer76, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer77 = wx.BoxSizer( wx.VERTICAL )

		self.lcOperators = wx.ListCtrl( self.panSetOperators, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		bSizer77.Add( self.lcOperators, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer582.Add( bSizer77, 1, wx.ALL|wx.EXPAND, 5 )


		self.panSetOperators.SetSizer( bSizer582 )
		self.panSetOperators.Layout()
		bSizer582.Fit( self.panSetOperators )
		self.m_listbook1.AddPage( self.panSetOperators, u"Operators", False )

		bSizer991.Add( self.m_listbook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.panTimeTolerance.SetSizer( bSizer991 )
		self.panTimeTolerance.Layout()
		bSizer991.Fit( self.panTimeTolerance )
		self.nbMain.AddPage( self.panTimeTolerance, u"Settings", True )

		bSizer36.Add( self.nbMain, 1, wx.ALL|wx.EXPAND, 10 )


		bSizer35.Add( bSizer36, 1, wx.EXPAND, 5 )


		bSizer29.Add( bSizer35, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()
		icoCamPath = "resources/camera.svg"
		svgCam = wx.svg.SVGimage.CreateFromFile(icoCamPath)
		bmCam = svgCam.ConvertToBitmap(width=24, height=24, scale=0.047)
		self.btnHomeCam1.SetBitmap(bmCam)
		self.btnHomeCam2.SetBitmap(bmCam)
		self.btnHomeCam3.SetBitmap(bmCam)

		icoColorPath = "resources/palette.svg"
		svgColor = wx.svg.SVGimage.CreateFromFile(icoColorPath)
		bmColor = svgColor.ConvertToBitmap(width=24, height=24, scale=0.047)
		self.bmColor.SetBitmap(bmColor)


		ico1Path = "resources/1.svg"
		svg1 = wx.svg.SVGimage.CreateFromFile(ico1Path)
		bm1 = svg1.ConvertToBitmap(width=12, height=24, scale=0.047)
		self.bmStep1.SetBitmap(bm1)

		ico2Path = "resources/2.svg"
		svg2 = wx.svg.SVGimage.CreateFromFile(ico2Path)
		bm2 = svg2.ConvertToBitmap(width=15, height=24, scale=0.047)
		self.bmStep2.SetBitmap(bm2)

		ico3Path = "resources/3.svg"
		svg3 = wx.svg.SVGimage.CreateFromFile(ico3Path)
		bm3 = svg3.ConvertToBitmap(width=16, height=24, scale=0.047)
		self.bmStep3.SetBitmap(bm3)


		self.sbMain = self.CreateStatusBar( 4, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.chHomeShift.Bind( wx.EVT_CHOICE, self.chHomeShiftOnChoice )
		self.chHomeGroup.Bind( wx.EVT_CHOICE, self.chHomeGroupOnChoice )
		self.chHomeOp1.Bind( wx.EVT_COMBOBOX, self.chHomeOp1OnCombobox )
		self.chHomeOp2.Bind( wx.EVT_COMBOBOX, self.chHomeOp2OnCombobox )
		self.chHomeLine.Bind( wx.EVT_CHOICE, self.chHomeLineOnChoice )
		self.btnHomeCol.Bind( wx.EVT_BUTTON, self.btnHomeColOnClick )
		self.btnStart.Bind( wx.EVT_BUTTON, self.btnStartOnButtonClick )
		self.btnHomeConnect.Bind( wx.EVT_BUTTON, self.btnHomeConnectOnButtonClick )
		self.chHomePort.Bind( wx.EVT_CHOICE, self.chHomePortOnChoice )
		self.btnHomeReset.Bind( wx.EVT_BUTTON, self.btnHomeResetOnButtonClick )
		self.btnHomeStatusLoad.Bind( wx.EVT_BUTTON, self.btnHomeStatusLoadOnButtonClick )
		self.btnHomeCam1.Bind( wx.EVT_BUTTON, self.btnHomeCam1OnButtonClick )
		self.btnHomeFinish.Bind( wx.EVT_BUTTON, self.btnHomeFinishOnButtonClick )
		self.chRecordsShift.Bind( wx.EVT_CHOICE, self.chRecordsShiftOnChoice )
		self.calRecordsStartDt1.Bind( wx.adv.EVT_DATE_CHANGED, self.calRecordsStartDt1OnDateChanged )
		self.calRecordsFinishDt1.Bind( wx.adv.EVT_DATE_CHANGED, self.calRecordsFinishDt1OnDateChanged )
		self.btnRecordsApply.Bind( wx.EVT_BUTTON, self.btnRecordsApplyOnButtonClick )
		self.chSumShift.Bind( wx.EVT_CHOICE, self.chSumShiftOnChoice )
		self.calSumStartDt2.Bind( wx.adv.EVT_DATE_CHANGED, self.calSumStartDt2OnDateChanged )
		self.calSumFinishDt2.Bind( wx.adv.EVT_DATE_CHANGED, self.calSumFinishDt2OnDateChanged )
		self.btnSumApply.Bind( wx.EVT_BUTTON, self.btnSumApplyOnButtonClick )
		self.chGenBaud.Bind( wx.EVT_CHOICE, self.chGenBaudOnChoice )
		self.btnGenSave.Bind( wx.EVT_BUTTON, self.btnGenSaveOnButtonClick )
		self.btnRecCreate.Bind( wx.EVT_BUTTON, self.btnRecCreateOnButtonClick )
		self.btnRecEdit.Bind( wx.EVT_BUTTON, self.btnRecEditOnButtonClick )
		self.btnRecDelete.Bind( wx.EVT_BUTTON, self.btnRecDeleteOnButtonClick )
		self.btnRecRefresh.Bind( wx.EVT_BUTTON, self.btnRecRefreshOnButtonClick )
		self.btnOpCreate.Bind( wx.EVT_BUTTON, self.btnOpCreateOnButtonClick )
		self.btnOpDelete.Bind( wx.EVT_BUTTON, self.btnOpDeleteOnButtonClick )
		self.btnOpRefresh.Bind( wx.EVT_BUTTON, self.btnOpRefreshOnButtonClick )
		self.lcOperators.Bind( wx.EVT_LIST_ITEM_SELECTED, self.lcOpOperatorsOnListItemSelected )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def chHomeShiftOnChoice( self, event ):
		event.Skip()

	def chHomeGroupOnChoice( self, event ):
		event.Skip()

	def chHomeOp1OnCombobox( self, event ):
		event.Skip()

	def chHomeOp2OnCombobox( self, event ):
		event.Skip()

	def chHomeLineOnChoice( self, event ):
		event.Skip()

	def btnHomeColOnClick( self, event ):
		event.Skip()

	def btnStartOnButtonClick( self, event ):
		event.Skip()

	def btnHomeConnectOnButtonClick( self, event ):
		event.Skip()

	def chHomePortOnChoice( self, event ):
		event.Skip()

	def btnHomeResetOnButtonClick( self, event ):
		event.Skip()

	def btnHomeStatusLoadOnButtonClick( self, event ):
		event.Skip()

	def btnHomeCam1OnButtonClick( self, event ):
		event.Skip()

	def btnHomeFinishOnButtonClick( self, event ):
		event.Skip()

	def chRecordsShiftOnChoice( self, event ):
		event.Skip()

	def calRecordsStartDt1OnDateChanged( self, event ):
		event.Skip()

	def calRecordsFinishDt1OnDateChanged( self, event ):
		event.Skip()

	def btnRecordsApplyOnButtonClick( self, event ):
		event.Skip()

	def chSumShiftOnChoice( self, event ):
		event.Skip()

	def calSumStartDt2OnDateChanged( self, event ):
		event.Skip()

	def calSumFinishDt2OnDateChanged( self, event ):
		event.Skip()

	def btnSumApplyOnButtonClick( self, event ):
		event.Skip()

	def chGenBaudOnChoice( self, event ):
		event.Skip()

	def btnGenSaveOnButtonClick( self, event ):
		event.Skip()

	def btnRecCreateOnButtonClick( self, event ):
		event.Skip()

	def btnRecEditOnButtonClick( self, event ):
		event.Skip()

	def btnRecDeleteOnButtonClick( self, event ):
		event.Skip()

	def btnRecRefreshOnButtonClick( self, event ):
		event.Skip()

	def btnOpCreateOnButtonClick( self, event ):
		event.Skip()

	def btnOpDeleteOnButtonClick( self, event ):
		event.Skip()

	def btnOpRefreshOnButtonClick( self, event ):
		event.Skip()

	def lcOpOperatorsOnListItemSelected( self, event ):
		event.Skip()


###########################################################################
## Class dgColor
###########################################################################

class dgColor ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Color Selector", pos = wx.DefaultPosition, size = wx.Size( 300,400 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.lcColor = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST|wx.LC_SINGLE_SEL )
		bSizer63.Add( self.lcColor, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		bSizer63.Add( self.btnApply, 0, wx.ALIGN_RIGHT|wx.ALL|wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )


		bSizer2.Add( bSizer63, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnApply.Bind( wx.EVT_BUTTON, self.btnApplyOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btnApplyOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class dgRecipes
###########################################################################

class dgRecipes ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Recipes", pos = wx.DefaultPosition, size = wx.Size( 757,495 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		bSizer77 = wx.BoxSizer( wx.VERTICAL )

		bSizer103 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		bSizer103.Add( self.m_staticText62, 0, wx.ALL, 5 )

		self.tcColor = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer103.Add( self.tcColor, 0, wx.ALL, 5 )


		bSizer77.Add( bSizer103, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer60.Add( bSizer77, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 1" ), wx.VERTICAL )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		bSizer104 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText471 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText471.Wrap( -1 )

		bSizer104.Add( self.m_staticText471, 0, wx.ALL, 5 )


		bSizer104.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stTime1 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTime1.Wrap( -1 )

		bSizer104.Add( self.stTime1, 0, wx.ALL, 5 )


		bSizer101.Add( bSizer104, 1, wx.EXPAND, 5 )

		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

		self.scTime1 = wx.SpinCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.SP_ARROW_KEYS, 0, 3599, 0 )
		bSizer57.Add( self.scTime1, 1, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		bSizer57.Add( self.m_staticText46, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer101.Add( bSizer57, 0, wx.EXPAND, 5 )


		sbSizer11.Add( bSizer101, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer102 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText461 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText461.Wrap( -1 )

		bSizer102.Add( self.m_staticText461, 0, wx.ALL, 5 )

		self.tcDesc1 = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer102.Add( self.tcDesc1, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer11.Add( bSizer102, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer66.Add( sbSizer11, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 2" ), wx.VERTICAL )

		bSizer1011 = wx.BoxSizer( wx.VERTICAL )

		bSizer1041 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4711 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4711.Wrap( -1 )

		bSizer1041.Add( self.m_staticText4711, 0, wx.ALL, 5 )


		bSizer1041.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stTime2 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTime2.Wrap( -1 )

		bSizer1041.Add( self.stTime2, 0, wx.ALL, 5 )


		bSizer1011.Add( bSizer1041, 1, wx.EXPAND, 5 )

		bSizer571 = wx.BoxSizer( wx.HORIZONTAL )

		self.scTime2 = wx.SpinCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.SP_ARROW_KEYS, 0, 3599, 0 )
		bSizer571.Add( self.scTime2, 1, wx.ALL, 5 )

		self.m_staticText462 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, u"seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText462.Wrap( -1 )

		bSizer571.Add( self.m_staticText462, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1011.Add( bSizer571, 0, wx.EXPAND, 5 )


		sbSizer111.Add( bSizer1011, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer1021 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4611 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4611.Wrap( -1 )

		bSizer1021.Add( self.m_staticText4611, 0, wx.ALL, 5 )

		self.tcDesc2 = wx.TextCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1021.Add( self.tcDesc2, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer111.Add( bSizer1021, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer66.Add( sbSizer111, 1, wx.EXPAND, 5 )

		sbSizer112 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 3" ), wx.VERTICAL )

		bSizer1012 = wx.BoxSizer( wx.VERTICAL )

		bSizer1042 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4712 = wx.StaticText( sbSizer112.GetStaticBox(), wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4712.Wrap( -1 )

		bSizer1042.Add( self.m_staticText4712, 0, wx.ALL, 5 )


		bSizer1042.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stTime3 = wx.StaticText( sbSizer112.GetStaticBox(), wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTime3.Wrap( -1 )

		bSizer1042.Add( self.stTime3, 0, wx.ALL, 5 )


		bSizer1012.Add( bSizer1042, 1, wx.EXPAND, 5 )

		bSizer572 = wx.BoxSizer( wx.HORIZONTAL )

		self.scTime3 = wx.SpinCtrl( sbSizer112.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.SP_ARROW_KEYS, 0, 3599, 0 )
		bSizer572.Add( self.scTime3, 1, wx.ALL, 5 )

		self.m_staticText463 = wx.StaticText( sbSizer112.GetStaticBox(), wx.ID_ANY, u"seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText463.Wrap( -1 )

		bSizer572.Add( self.m_staticText463, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1012.Add( bSizer572, 0, wx.EXPAND, 5 )


		sbSizer112.Add( bSizer1012, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer1022 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4612 = wx.StaticText( sbSizer112.GetStaticBox(), wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4612.Wrap( -1 )

		bSizer1022.Add( self.m_staticText4612, 0, wx.ALL, 5 )

		self.tcDesc3 = wx.TextCtrl( sbSizer112.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1022.Add( self.tcDesc3, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer112.Add( bSizer1022, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer66.Add( sbSizer112, 1, wx.EXPAND, 5 )


		bSizer60.Add( bSizer66, 1, wx.EXPAND, 5 )

		bSizer73 = wx.BoxSizer( wx.VERTICAL )

		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer73.Add( self.btnSave, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer60.Add( bSizer73, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer60 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.scTime1.Bind( wx.EVT_SPINCTRL, self.scTime1Update )
		self.scTime1.Bind( wx.EVT_TEXT, self.scTime1Update )
		self.scTime1.Bind( wx.EVT_TEXT_ENTER, self.scTime1Update )
		self.scTime2.Bind( wx.EVT_SPINCTRL, self.scTime2Update )
		self.scTime2.Bind( wx.EVT_TEXT, self.scTime2Update )
		self.scTime3.Bind( wx.EVT_SPINCTRL, self.scTime3Update )
		self.scTime3.Bind( wx.EVT_TEXT, self.scTime3Update )
		self.scTime3.Bind( wx.EVT_TEXT_ENTER, self.scTime3Update )
		self.btnSave.Bind( wx.EVT_BUTTON, self.btnSaveOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def scTime1Update( self, event ):
		event.Skip()



	def scTime2Update( self, event ):
		event.Skip()


	def scTime3Update( self, event ):
		event.Skip()



	def btnSaveOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class dgLogin
###########################################################################

class dgLogin ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 309,464 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer72 = wx.BoxSizer( wx.VERTICAL )

		bSizer73 = wx.BoxSizer( wx.VERTICAL )


		bSizer73.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, u"Open Mill Validator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		bSizer73.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer73.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer72.Add( bSizer73, 1, wx.EXPAND, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		bSizer74.Add( self.m_staticText62, 0, wx.ALL, 5 )

		m_choice8Choices = [ wx.EmptyString, u"1", u"2", u"3" ]
		self.m_choice8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice8Choices, 0 )
		self.m_choice8.SetSelection( 0 )
		bSizer74.Add( self.m_choice8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Group", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		bSizer74.Add( self.m_staticText61, 0, wx.ALL, 5 )

		m_choice7Choices = [ wx.EmptyString, u"A", u"B", u"C" ]
		self.m_choice7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 0 )
		bSizer74.Add( self.m_choice7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Operator 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		bSizer74.Add( self.m_staticText63, 0, wx.ALL, 5 )

		m_comboBox4Choices = []
		self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices, 0 )
		bSizer74.Add( self.m_comboBox4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText64 = wx.StaticText( self, wx.ID_ANY, u"Operator 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		bSizer74.Add( self.m_staticText64, 0, wx.ALL, 5 )

		m_comboBox5Choices = []
		self.m_comboBox5 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox5Choices, 0 )
		bSizer74.Add( self.m_comboBox5, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer72.Add( bSizer74, 3, wx.ALL|wx.EXPAND, 5 )

		bSizer77 = wx.BoxSizer( wx.VERTICAL )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer77.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer72.Add( bSizer77, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer72 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


