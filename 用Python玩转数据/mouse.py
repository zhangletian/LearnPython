import wx

class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(None,title='Hello,World!')
		frame.Show()
		return True

if __name__=='__main__':
	app = MyApp()
	app.MainLoop()
