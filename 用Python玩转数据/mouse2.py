import wx

class Frame1(wx.Frame):
	def __init__(self,superior):
		wx.Frame.__init__(self,superior)
		self.panel = wx.Panel(self)
		self.panel.Bind(wx.EVT_LEFT_UP,self.OnClick)
	
	def OnClick(self,event):
		posm = event.GetPosition()
		wx.StaticText(parent = self.panel,label='Hello,World',pos=(posm.x,posm.y))

if __name__ == '__main__':
	app = wx.App()
	frame = Frame1(None)
	frame.Show(True)
