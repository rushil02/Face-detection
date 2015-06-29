from GUI import GUI_layout
from Sql import sqldb
from Detection import face_recognition
import wx

class db1(GUI_layout.MyDialog2):
    def __init__(self, parent):
        GUI_layout.MyDialog2.__init__( self, parent)
        self.Show()

    def settrdata(self,event):
        tr_dir = self.m_dirPicker4.GetPath()
        print tr_dir
        face_recognition.pathpass(tr_dir)
        self.Close(True)
        #facerecognition script function call to store a global variable as dir

class db2(GUI_layout.MyDialog3):
    def __init__(self, parent):
        GUI_layout.MyDialog3.__init__( self, parent)
        self.Show()

    def onsqladd(self, event):
        lat = self.m_textCtrl6.GetValue()
        lon = self.m_textCtrl7.GetValue()
        face = self.m_textCtrl8.GetValue()
        sqldb.add_cam(lat, lon, face)

    def onsqlnewdb( self, event ):
        sqldb.create_sqldb()

    def onsqlok( self, event ):
        self.Close(True)
        

class fd(GUI_layout.myframe):
    def __init__(self,parent):
        GUI_layout.myframe.__init__( self, parent)
        self.Show()

    def training(self, event):
        obdb1 = db1(None)

    def sqldb( self, event):
        obdb2 = db2(None)

    def close1( self, event):
        face_recognition.stop()
        self.Close(True)

    def onscan( self,parent):
        tr_dir = self.m_dirPicker3.GetPath()
        face_recognition.train()

    def onstart( self, event ):
        face_recognition.start()
	
    def timeline( self, event ):
        pass
        
app = wx.App(False)
frame = fd(None)
app.MainLoop()