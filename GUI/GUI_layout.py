# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class myframe
###########################################################################

class myframe ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Face Detection Network", pos = wx.DefaultPosition, size = wx.Size( 734,457 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Find Person" ), wx.VERTICAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Directory of the Facial images of the person to find :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		sbSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_dirPicker3 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_CHANGE_DIR|wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST )
		sbSizer2.Add( self.m_dirPicker3, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge2.SetValue( 0 ) 
		sbSizer2.Add( self.m_gauge2, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer6 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Start Looking", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Build Timeline", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		sbSizer2.Add( gSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Live Feed" ), wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		sbSizer4.Add( self.m_panel3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Camera ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( gSizer2, 0, 0, 5 )
		
		
		gSizer1.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Training Set", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"SQL", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem2 )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem3 )
		
		self.m_menubar2.Append( self.m_menu2, u"File" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button16.Bind( wx.EVT_BUTTON, self.onscan )
		self.m_button17.Bind( wx.EVT_BUTTON, self.onstart )
		self.m_button18.Bind( wx.EVT_BUTTON, self.timeline )
		self.Bind( wx.EVT_MENU, self.training, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.sqldb, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.close1, id = self.m_menuItem3.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onscan( self, event ):
		event.Skip()
	
	def onstart( self, event ):
		event.Skip()
	
	def timeline( self, event ):
		event.Skip()
	
	def training( self, event ):
		event.Skip()
	
	def sqldb( self, event ):
		event.Skip()
	
	def close1( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Training Data", pos = wx.DefaultPosition, size = wx.Size( 533,124 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_dirPicker4 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer3.Add( self.m_dirPicker4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_gauge3 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge3.SetValue( 0 ) 
		bSizer3.Add( self.m_gauge3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button13.Bind( wx.EVT_BUTTON, self.settrdata )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def settrdata( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog3
###########################################################################

class MyDialog3 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SQL", pos = wx.DefaultPosition, size = wx.Size( 311,267 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Add Camera" ), wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer3.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Face direction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer3.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		
		sbSizer6.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button10, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Status : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer4.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer6.Add( gSizer4, 0, 0, 5 )
		
		
		bSizer5.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Create New Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Status : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer5.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( gSizer5, 0, 0, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button10.Bind( wx.EVT_BUTTON, self.onsqladd )
		self.m_button5.Bind( wx.EVT_BUTTON, self.onsqlnewdb )
		self.m_button12.Bind( wx.EVT_BUTTON, self.onsqlok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onsqladd( self, event ):
		event.Skip()
	
	def onsqlnewdb( self, event ):
		event.Skip()
	
	def onsqlok( self, event ):
		event.Skip()
	

