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

###########################################################################
## Class dgColors
###########################################################################

class dgColors ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Colors Selector", pos = wx.DefaultPosition, size = wx.Size( 671,400 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		lbDgColSelectChoices = [ u"WHITE", u"COLOR", u"CLEAR", u"BLACK & COLOR", u"LOGO", u"REGRIND", u"WHITE REGRIND" ]
		self.lbDgColSelect = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbDgColSelectChoices, 0 )
		self.lbDgColSelect.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer2.Add( self.lbDgColSelect, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnDgColSelect = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnDgColSelect, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnDgColSelect.Bind( wx.EVT_BUTTON, self.btn_colorOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btn_colorOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class dgRecipe
###########################################################################

class dgRecipe ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Recipe", pos = wx.DefaultPosition, size = wx.Size( 659,439 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		gSizer17 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer77 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		bSizer77.Add( self.m_staticText62, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer77.Add( self.m_textCtrl19, 0, wx.ALL, 5 )


		gSizer17.Add( bSizer77, 1, wx.EXPAND, 5 )

		bSizer78 = wx.BoxSizer( wx.VERTICAL )


		bSizer78.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnDgRecApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78.Add( self.btnDgRecApply, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer17.Add( bSizer78, 1, wx.EXPAND, 5 )


		bSizer60.Add( gSizer17, 0, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer60.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer64 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"STEP 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		bSizer64.Add( self.m_staticText49, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		bSizer62.Add( self.m_staticText46, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer8.Add( bSizer62, 0, wx.EXPAND, 5 )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		bSizer63.Add( self.m_staticText47, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer63.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer8.Add( bSizer63, 0, wx.EXPAND, 5 )


		bSizer64.Add( gSizer8, 1, wx.EXPAND, 5 )


		bSizer60.Add( bSizer64, 0, wx.EXPAND, 5 )

		bSizer65 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"STEP 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		bSizer65.Add( self.m_staticText50, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer81 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer621 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText461 = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText461.Wrap( -1 )

		bSizer621.Add( self.m_staticText461, 0, wx.ALL, 5 )

		self.m_textCtrl71 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer621.Add( self.m_textCtrl71, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer81.Add( bSizer621, 0, wx.EXPAND, 5 )

		bSizer631 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText471 = wx.StaticText( self, wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText471.Wrap( -1 )

		bSizer631.Add( self.m_staticText471, 0, wx.ALL, 5 )

		self.m_textCtrl81 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer631.Add( self.m_textCtrl81, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer81.Add( bSizer631, 0, wx.EXPAND, 5 )


		bSizer65.Add( gSizer81, 0, wx.EXPAND, 5 )


		bSizer60.Add( bSizer65, 1, wx.EXPAND, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"STEP 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		bSizer74.Add( self.m_staticText59, 0, wx.ALL, 5 )

		gSizer82 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer622 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText462 = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText462.Wrap( -1 )

		bSizer622.Add( self.m_staticText462, 0, wx.ALL, 5 )

		self.m_textCtrl72 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer622.Add( self.m_textCtrl72, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer82.Add( bSizer622, 0, wx.EXPAND, 5 )

		bSizer632 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText472 = wx.StaticText( self, wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText472.Wrap( -1 )

		bSizer632.Add( self.m_staticText472, 0, wx.ALL, 5 )

		self.m_textCtrl82 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer632.Add( self.m_textCtrl82, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer82.Add( bSizer632, 0, wx.EXPAND, 5 )


		bSizer74.Add( gSizer82, 1, wx.EXPAND, 5 )


		bSizer60.Add( bSizer74, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer60 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class frMain
###########################################################################

class frMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Open Mill Process Validator", pos = wx.DefaultPosition, size = wx.Size( 1169,712 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.nbMain = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nbMain.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		self.panHome = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panHome.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer162 = wx.BoxSizer( wx.VERTICAL )

		bSizer531 = wx.BoxSizer( wx.VERTICAL )

		self.panForm = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panForm.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		page_group1 = wx.BoxSizer( wx.VERTICAL )

		self.groupMain = wx.StaticText( self.panForm, wx.ID_ANY, u"Group", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.groupMain.Wrap( -1 )

		page_group1.Add( self.groupMain, 0, wx.ALL, 5 )

		choiceGroupMainChoices = [ u"A", u"B", u"C" ]
		self.choiceGroupMain = wx.Choice( self.panForm, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGroupMainChoices, 0 )
		self.choiceGroupMain.SetSelection( 0 )
		page_group1.Add( self.choiceGroupMain, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( page_group1, 0, wx.ALL|wx.EXPAND, 5 )

		page_op1 = wx.BoxSizer( wx.VERTICAL )

		self.op1Main = wx.StaticText( self.panForm, wx.ID_ANY, u"Operator 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.op1Main.Wrap( -1 )

		page_op1.Add( self.op1Main, 0, wx.ALL, 5 )

		cbHomeOp1Choices = [ u"riski", u"lia", u"dianah", u"jelsi", u"bella", u"dio", u"edwin", u"mustofa" ]
		self.cbHomeOp1 = wx.ComboBox( self.panForm, wx.ID_ANY, u"dianah", wx.DefaultPosition, wx.DefaultSize, cbHomeOp1Choices, 0 )
		self.cbHomeOp1.SetSelection( 2 )
		page_op1.Add( self.cbHomeOp1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( page_op1, 1, wx.ALL|wx.EXPAND, 5 )

		page_op2 = wx.BoxSizer( wx.VERTICAL )

		self.cbHomeOp2 = wx.StaticText( self.panForm, wx.ID_ANY, u"Operator 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbHomeOp2.Wrap( -1 )

		page_op2.Add( self.cbHomeOp2, 0, wx.ALL, 5 )

		cbHomeOp2Choices = []
		self.cbHomeOp2 = wx.ComboBox( self.panForm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbHomeOp2Choices, 0 )
		page_op2.Add( self.cbHomeOp2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( page_op2, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.lineMain = wx.StaticText( self.panForm, wx.ID_ANY, u"Line", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lineMain.Wrap( -1 )

		bSizer3.Add( self.lineMain, 0, wx.ALL, 5 )

		choiceLineMainChoices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9" ]
		self.choiceLineMain = wx.ComboBox( self.panForm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, choiceLineMainChoices, 0 )
		self.choiceLineMain.SetSelection( 0 )
		bSizer3.Add( self.choiceLineMain, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText36 = wx.StaticText( self.panForm, wx.ID_ANY, u"No Batch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		bSizer40.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.panForm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer40, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.latestBatch1 = wx.Panel( self.panForm, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.latestBatch1.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer65 = wx.BoxSizer( wx.VERTICAL )

		self.latestBatch = wx.StaticText( self.latestBatch1, wx.ID_ANY, u"Latest batch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.latestBatch.Wrap( -1 )

		bSizer65.Add( self.latestBatch, 0, wx.ALL, 5 )


		bSizer65.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.resultLatestBatch = wx.StaticText( self.latestBatch1, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.resultLatestBatch.Wrap( -1 )

		bSizer65.Add( self.resultLatestBatch, 0, wx.EXPAND, 5 )


		bSizer65.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.latestBatch1.SetSizer( bSizer65 )
		self.latestBatch1.Layout()
		bSizer65.Fit( self.latestBatch1 )
		bSizer41.Add( self.latestBatch1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( bSizer41, 0, wx.ALL|wx.EXPAND, 5 )


		self.panForm.SetSizer( bSizer30 )
		self.panForm.Layout()
		bSizer30.Fit( self.panForm )
		bSizer531.Add( self.panForm, 0, wx.ALL|wx.EXPAND, 0 )


		bSizer162.Add( bSizer531, 0, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 4, 0, 0 )

		bSizer472 = wx.BoxSizer( wx.VERTICAL )

		self.panColMain = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panColMain.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer123 = wx.BoxSizer( wx.VERTICAL )

		self.ColMain = wx.StaticText( self.panColMain, wx.ID_ANY, u"COLOR", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_DEFAULT )
		self.ColMain.Wrap( -1 )

		self.ColMain.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ColMain.SetBackgroundColour( wx.Colour( 75, 66, 55 ) )

		bSizer123.Add( self.ColMain, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer123.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnHomeCol = wx.Button( self.panColMain, wx.ID_ANY, u"WHITE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnHomeCol.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer123.Add( self.btnHomeCol, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


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

		self.btnConnect = wx.Button( self.panHome, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.btnConnect, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer55.Add( bSizer56, 1, wx.EXPAND, 5 )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		self.btnReset = wx.Button( self.panHome, wx.ID_ANY, u" Reset ", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer57.Add( self.btnReset, 1, wx.ALL, 5 )


		bSizer55.Add( bSizer57, 0, wx.EXPAND, 5 )


		bSizer53.Add( bSizer55, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.BaudRate = wx.StaticText( self.panHome, wx.ID_ANY, u"Baud Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BaudRate.Wrap( -1 )

		gSizer7.Add( self.BaudRate, 0, wx.ALL, 5 )

		choiceBaudRateChoices = []
		self.choiceBaudRate = wx.Choice( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceBaudRateChoices, 0 )
		self.choiceBaudRate.SetSelection( 0 )
		gSizer7.Add( self.choiceBaudRate, 1, wx.ALL|wx.EXPAND, 5 )

		self.Port = wx.StaticText( self.panHome, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Port.Wrap( -1 )

		gSizer7.Add( self.Port, 1, wx.ALL, 5 )

		choicePortChoices = []
		self.choicePort = wx.Choice( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePortChoices, 0 )
		self.choicePort.SetSelection( 0 )
		gSizer7.Add( self.choicePort, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( gSizer7, 0, wx.EXPAND, 5 )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer58.Add( gSizer71, 1, wx.EXPAND, 5 )

		self.StatusLoad = wx.StaticText( self.panHome, wx.ID_ANY, u"Status Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StatusLoad.Wrap( -1 )

		bSizer58.Add( self.StatusLoad, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnStatusLoad = wx.Button( self.panHome, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnStatusLoad.SetBackgroundColour( wx.Colour( 81, 203, 32 ) )

		bSizer58.Add( self.btnStatusLoad, 1, wx.ALL, 5 )


		bSizer53.Add( bSizer58, 1, wx.EXPAND, 5 )

		bSizer581 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer711 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer581.Add( gSizer711, 1, wx.EXPAND, 5 )

		self.TotalTimeAct = wx.StaticText( self.panHome, wx.ID_ANY, u"Total Time Act", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TotalTimeAct.Wrap( -1 )

		bSizer581.Add( self.TotalTimeAct, 1, wx.ALL|wx.EXPAND, 5 )

		self.inpTotalTimeAct = wx.StaticText( self.panHome, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpTotalTimeAct.Wrap( -1 )

		bSizer581.Add( self.inpTotalTimeAct, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( bSizer581, 1, wx.EXPAND, 5 )

		bSizer551 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer551.Add( gSizer12, 1, wx.EXPAND, 5 )

		self.TimeTolerance = wx.StaticText( self.panHome, wx.ID_ANY, u"Time Tolerance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TimeTolerance.Wrap( -1 )

		bSizer551.Add( self.TimeTolerance, 1, wx.ALL|wx.EXPAND, 5 )

		self.inpTimeTolerance = wx.StaticText( self.panHome, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpTimeTolerance.Wrap( -1 )

		bSizer551.Add( self.inpTimeTolerance, 0, wx.ALL, 5 )


		bSizer53.Add( bSizer551, 1, wx.EXPAND, 5 )


		bSizer501.Add( bSizer53, 1, wx.EXPAND, 5 )


		bSizer492.Add( bSizer501, 1, wx.EXPAND, 5 )


		bSizer472.Add( bSizer492, 0, wx.EXPAND, 5 )


		gSizer5.Add( bSizer472, 1, wx.EXPAND, 5 )

		bSizer49 = wx.BoxSizer( wx.VERTICAL )

		self.panStep1 = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep1.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer421 = wx.BoxSizer( wx.VERTICAL )

		self.Step1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"STEP 1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Step1.Wrap( -1 )

		self.Step1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Step1.SetBackgroundColour( wx.Colour( 75, 66, 55 ) )

		bSizer421.Add( self.Step1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer421.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer75 = wx.BoxSizer( wx.VERTICAL )

		self.processStep1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"Masukkan material sebanyak 15 kg. Kemudian prsoes roll selama 120 detik (2 menit).\n\n\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.processStep1.Wrap( 150 )

		bSizer75.Add( self.processStep1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer471 = wx.BoxSizer( wx.VERTICAL )


		bSizer75.Add( bSizer471, 1, wx.EXPAND, 5 )


		bSizer421.Add( bSizer75, 1, wx.EXPAND, 5 )


		bSizer421.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer61112 = wx.BoxSizer( wx.VERTICAL )

		self.btnCam1 = wx.BitmapButton( self.panStep1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnCam1.SetBitmap( wx.Bitmap( u"resources/cam_32x32.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCam1.SetBitmapDisabled( wx.NullBitmap )
		self.btnCam1.SetBitmapCurrent( wx.NullBitmap )
		bSizer61112.Add( self.btnCam1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Next1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"NEXT", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Next1.Wrap( -1 )

		self.Next1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Next1.SetBackgroundColour( wx.Colour( 66, 62, 55 ) )

		bSizer61112.Add( self.Next1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.actTime1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.actTime1.Wrap( -1 )

		self.actTime1.SetForegroundColour( wx.Colour( 115, 107, 96 ) )

		bSizer61112.Add( self.actTime1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stdTime1 = wx.StaticText( self.panStep1, wx.ID_ANY, u"04.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stdTime1.Wrap( -1 )

		bSizer61112.Add( self.stdTime1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer421.Add( bSizer61112, 1, wx.EXPAND, 5 )


		self.panStep1.SetSizer( bSizer421 )
		self.panStep1.Layout()
		bSizer421.Fit( self.panStep1 )
		bSizer49.Add( self.panStep1, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer49, 1, wx.EXPAND, 5 )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.panStep2 = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep2.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.Step2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"STEP 2", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Step2.Wrap( -1 )

		self.Step2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Step2.SetBackgroundColour( wx.Colour( 75, 66, 55 ) )

		bSizer51.Add( self.Step2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer751 = wx.BoxSizer( wx.VERTICAL )

		self.processStep2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"Masukkan material sebanyak 15 kg, tambahkan pigment Regrind, Akselerator dan Sulfur. Kemudian proses roll selama 240 detik (4 menit)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.processStep2.Wrap( 150 )

		bSizer751.Add( self.processStep2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer461 = wx.BoxSizer( wx.VERTICAL )


		bSizer751.Add( bSizer461, 1, wx.EXPAND, 5 )


		bSizer51.Add( bSizer751, 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer61111 = wx.BoxSizer( wx.VERTICAL )

		self.btnCam2 = wx.BitmapButton( self.panStep2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnCam2.SetBitmap( wx.Bitmap( u"resources/cam_32x32.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCam2.SetBitmapDisabled( wx.NullBitmap )
		bSizer61111.Add( self.btnCam2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Next2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"NEXT", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Next2.Wrap( -1 )

		self.Next2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Next2.SetBackgroundColour( wx.Colour( 66, 62, 55 ) )

		bSizer61111.Add( self.Next2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.actTime2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.actTime2.Wrap( -1 )

		self.actTime2.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer61111.Add( self.actTime2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer61111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stdTime2 = wx.StaticText( self.panStep2, wx.ID_ANY, u"04.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stdTime2.Wrap( -1 )

		bSizer61111.Add( self.stdTime2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer51.Add( bSizer61111, 1, wx.EXPAND, 5 )


		self.panStep2.SetSizer( bSizer51 )
		self.panStep2.Layout()
		bSizer51.Fit( self.panStep2 )
		bSizer43.Add( self.panStep2, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer43, 1, wx.EXPAND, 5 )

		bSizer491 = wx.BoxSizer( wx.VERTICAL )

		self.panStep3 = wx.Panel( self.panHome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panStep3.SetBackgroundColour( wx.Colour( 237, 231, 217 ) )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.Step3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"STEP 3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Step3.Wrap( -1 )

		self.Step3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Step3.SetBackgroundColour( wx.Colour( 75, 66, 55 ) )

		bSizer52.Add( self.Step3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer52.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )


		bSizer52.Add( bSizer79, 1, wx.EXPAND, 5 )

		self.processStep3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"Masukkan campuran material sebanyak 45 kg. Tambahkan rework sebanyak 30%, lalu proses roll selama 660 detik. Jumlah total waktu yang dipakai 1020 detik (17 menit).\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.processStep3.Wrap( 170 )

		bSizer52.Add( self.processStep3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer52.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer6111 = wx.BoxSizer( wx.VERTICAL )

		self.btnCam3 = wx.BitmapButton( self.panStep3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btnCam3.SetBitmap( wx.Bitmap( u"resources/cam_32x32.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCam3.SetBitmapDisabled( wx.NullBitmap )
		bSizer6111.Add( self.btnCam3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Next3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"FINISH", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Next3.Wrap( -1 )

		self.Next3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Next3.SetBackgroundColour( wx.Colour( 66, 62, 55 ) )

		bSizer6111.Add( self.Next3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.actNext3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"00.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.actNext3.Wrap( -1 )

		self.actNext3.SetForegroundColour( wx.Colour( 115, 107, 96 ) )

		bSizer6111.Add( self.actNext3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.stdTime3 = wx.StaticText( self.panStep3, wx.ID_ANY, u"04.00", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.stdTime3.Wrap( -1 )

		bSizer6111.Add( self.stdTime3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer52.Add( bSizer6111, 1, wx.EXPAND, 5 )


		self.panStep3.SetSizer( bSizer52 )
		self.panStep3.Layout()
		bSizer52.Fit( self.panStep3 )
		bSizer491.Add( self.panStep3, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( bSizer491, 1, wx.EXPAND, 5 )


		bSizer162.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.panHome.SetSizer( bSizer162 )
		self.panHome.Layout()
		bSizer162.Fit( self.panHome )
		self.nbMain.AddPage( self.panHome, u"Home", False )
		self.panRecords = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panRecords.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer69 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer70 = wx.BoxSizer( wx.VERTICAL )

		self.groupHistory = wx.StaticText( self.panRecords, wx.ID_ANY, u"Group", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.groupHistory.Wrap( -1 )

		bSizer70.Add( self.groupHistory, 0, wx.ALL, 5 )

		choiceGroupHisChoices = [ u"A", u"B", u"C", u"Saturday" ]
		self.choiceGroupHis = wx.Choice( self.panRecords, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGroupHisChoices, 0 )
		self.choiceGroupHis.SetSelection( 0 )
		bSizer70.Add( self.choiceGroupHis, 0, wx.ALL, 5 )

		self.m_staticText43 = wx.StaticText( self.panRecords, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		bSizer70.Add( self.m_staticText43, 0, wx.ALL, 5 )

		m_choice6Choices = [ u"1", u"2", u"3" ]
		self.m_choice6 = wx.Choice( self.panRecords, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		bSizer70.Add( self.m_choice6, 0, wx.ALL, 5 )

		self.startDt1 = wx.StaticText( self.panRecords, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startDt1.Wrap( -1 )

		bSizer70.Add( self.startDt1, 0, wx.ALL, 5 )

		self.calStartDt1 = wx.adv.DatePickerCtrl( self.panRecords, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer70.Add( self.calStartDt1, 0, wx.ALL|wx.EXPAND, 5 )

		self.finishDt1 = wx.StaticText( self.panRecords, wx.ID_ANY, u"Finish Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.finishDt1.Wrap( -1 )

		bSizer70.Add( self.finishDt1, 0, wx.ALL, 5 )

		self.calFinishDt1 = wx.adv.DatePickerCtrl( self.panRecords, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer70.Add( self.calFinishDt1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.panRecords, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer70.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.btnSave1 = wx.Button( self.panRecords, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer70.Add( self.btnSave1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer69.Add( bSizer70, 0, wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_listCtrl1 = wx.ListCtrl( self.panRecords, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
		bSizer71.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer69.Add( bSizer71, 1, wx.EXPAND, 5 )


		self.panRecords.SetSizer( bSizer69 )
		self.panRecords.Layout()
		bSizer69.Fit( self.panRecords )
		self.nbMain.AddPage( self.panRecords, u"Records", False )
		self.panSummary = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panSummary.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText44 = wx.StaticText( self.panSummary, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		bSizer46.Add( self.m_staticText44, 0, wx.ALL, 5 )

		m_choice7Choices = [ u"1", u"2", u"3", u"Saturday" ]
		self.m_choice7 = wx.Choice( self.panSummary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 0 )
		bSizer46.Add( self.m_choice7, 0, wx.ALL, 5 )

		self.startDt2 = wx.StaticText( self.panSummary, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startDt2.Wrap( -1 )

		bSizer46.Add( self.startDt2, 0, wx.ALL, 5 )

		self.calStartDt2 = wx.adv.DatePickerCtrl( self.panSummary, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer46.Add( self.calStartDt2, 0, wx.ALL, 5 )

		self.finishDt2 = wx.StaticText( self.panSummary, wx.ID_ANY, u"Finish Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.finishDt2.Wrap( -1 )

		bSizer46.Add( self.finishDt2, 0, wx.ALL, 5 )

		self.calFinishDt2 = wx.adv.DatePickerCtrl( self.panSummary, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer46.Add( self.calFinishDt2, 0, wx.ALL, 5 )

		self.mstaticline2 = wx.StaticLine( self.panSummary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer46.Add( self.mstaticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.btnSave2 = wx.Button( self.panSummary, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.btnSave2, 0, wx.ALL, 5 )


		bSizer45.Add( bSizer46, 0, wx.EXPAND, 5 )

		bSizer47 = wx.BoxSizer( wx.VERTICAL )

		self.tabSummary = wx.grid.Grid( self.panSummary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

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
		self.tabSummary.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer47.Add( self.tabSummary, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer45.Add( bSizer47, 0, wx.EXPAND, 5 )


		self.panSummary.SetSizer( bSizer45 )
		self.panSummary.Layout()
		bSizer45.Fit( self.panSummary )
		self.nbMain.AddPage( self.panSummary, u"Summary", False )
		self.panRecipes = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panRecipes.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer119 = wx.BoxSizer( wx.VERTICAL )

		bSizer120 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer121 = wx.BoxSizer( wx.VERTICAL )

		m_choice21Choices = [ u"White", u"Color", u"Regrind" ]
		self.m_choice21 = wx.Choice( self.panRecipes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice21Choices, 0 )
		self.m_choice21.SetSelection( 0 )
		bSizer121.Add( self.m_choice21, 0, wx.ALL, 15 )


		bSizer120.Add( bSizer121, 1, wx.EXPAND, 5 )

		bSizer122 = wx.BoxSizer( wx.VERTICAL )

		self.btnRecNewCreate = wx.Button( self.panRecipes, wx.ID_ANY, u"+ Create New", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer122.Add( self.btnRecNewCreate, 0, wx.ALIGN_RIGHT|wx.ALL, 15 )


		bSizer120.Add( bSizer122, 1, wx.EXPAND, 5 )


		bSizer119.Add( bSizer120, 0, wx.EXPAND, 5 )

		bSizer1231 = wx.BoxSizer( wx.VERTICAL )

		self.lcRecStep = wx.ListCtrl( self.panRecipes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer1231.Add( self.lcRecStep, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer119.Add( bSizer1231, 1, wx.EXPAND, 5 )

		bSizer124 = wx.BoxSizer( wx.VERTICAL )

		self.btnRecSave = wx.Button( self.panRecipes, wx.ID_ANY, u"Save Changes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer124.Add( self.btnRecSave, 0, wx.ALIGN_RIGHT|wx.ALL, 15 )


		bSizer119.Add( bSizer124, 0, wx.EXPAND, 5 )


		self.panRecipes.SetSizer( bSizer119 )
		self.panRecipes.Layout()
		bSizer119.Fit( self.panRecipes )
		self.nbMain.AddPage( self.panRecipes, u"Recipes", True )
		self.panOperator = wx.Panel( self.nbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panOperator.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		bSizer582 = wx.BoxSizer( wx.VERTICAL )

		self.m_toolBar1 = wx.ToolBar( self.panOperator, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.btnOpRefresh = wx.Button( self.m_toolBar1, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toolBar1.AddControl( self.btnOpRefresh )
		self.btnOpDelete = wx.Button( self.m_toolBar1, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toolBar1.AddControl( self.btnOpDelete )
		self.m_toolBar1.Realize()

		bSizer582.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )

		self.lcOpNames = wx.ListCtrl( self.panOperator, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer582.Add( self.lcOpNames, 1, wx.ALL|wx.EXPAND, 5 )


		self.panOperator.SetSizer( bSizer582 )
		self.panOperator.Layout()
		bSizer582.Fit( self.panOperator )
		self.nbMain.AddPage( self.panOperator, u"Operators", False )

		bSizer36.Add( self.nbMain, 1, wx.ALL|wx.EXPAND, 10 )


		bSizer35.Add( bSizer36, 1, wx.EXPAND, 5 )


		bSizer29.Add( bSizer35, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()
		self.sbMain = self.CreateStatusBar( 4, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.cbHomeOp2.Bind( wx.EVT_CHAR, self.op2MainOnChar )
		self.choiceLineMain.Bind( wx.EVT_COMBOBOX, self.choiceLineMainOnCombobox )
		self.btnHomeCol.Bind( wx.EVT_BUTTON, self.btnHomeColOnClick )
		self.btnConnect.Bind( wx.EVT_BUTTON, self.btn_connectOnButtonClick )
		self.btnReset.Bind( wx.EVT_BUTTON, self.btn_resetOnButtonClick )
		self.btnStatusLoad.Bind( wx.EVT_BUTTON, self.btn_indicatorOnButtonClick )
		self.btnSave1.Bind( wx.EVT_BUTTON, self.btn_save1OnButtonClick )
		self.btnOpRefresh.Bind( wx.EVT_BUTTON, self.btnOpRefreshOnClick )
		self.btnOpDelete.Bind( wx.EVT_BUTTON, self.btnOpDeleteOnClick )
		self.lcOpNames.Bind( wx.EVT_LIST_ITEM_SELECTED, self.lcOpNamesOnListItemSelected )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def op2MainOnChar( self, event ):
		event.Skip()

	def choiceLineMainOnCombobox( self, event ):
		event.Skip()

	def btnHomeColOnClick( self, event ):
		event.Skip()

	def btn_connectOnButtonClick( self, event ):
		event.Skip()

	def btn_resetOnButtonClick( self, event ):
		event.Skip()

	def btn_indicatorOnButtonClick( self, event ):
		event.Skip()

	def btn_save1OnButtonClick( self, event ):
		event.Skip()

	def btnOpRefreshOnClick( self, event ):
		event.Skip()

	def btnOpDeleteOnClick( self, event ):
		event.Skip()

	def lcOpNamesOnListItemSelected( self, event ):
		event.Skip()


###########################################################################
## Class frLogin
###########################################################################

class frLogin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )

		bSizer1.Add( self.password, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inpPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.inpPassword, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnLogin, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnLogin.Bind( wx.EVT_BUTTON, self.btn_loginOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btn_loginOnButtonClick( self, event ):
		event.Skip()


