import wx
import os
from Excel_operations import Excel_Operations

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(450, 220))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="C Files Analyzer")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM,
                  border=15)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="Directory(.c files)")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        self.tc1 = wx.TextCtrl(panel)
        sizer.Add(self.tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)

        text3 = wx.StaticText(panel, label="Directory(.xls files)")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=10)

        self.tc2 = wx.TextCtrl(panel)
        sizer.Add(self.tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        button1 = wx.Button(panel, label="Browse...")
        button1.Bind(wx.EVT_BUTTON, self.brwse_cFiles)
        sizer.Add(button1, pos=(2, 4), flag=wx.TOP | wx.RIGHT, border=5)

        button2 = wx.Button(panel, label="Browse...")
        button2.Bind(wx.EVT_BUTTON, self.brwse_xlFiles)
        sizer.Add(button2, pos=(3, 4), flag=wx.TOP | wx.RIGHT, border=5)

        button3 = wx.Button(panel, label="Analyze")
        button3.Bind(wx.EVT_BUTTON, self.OnOK)
        sizer.Add(button3, pos=(4, 3))

        button4 = wx.Button(panel, label="Cancel")
        button4.Bind(wx.EVT_BUTTON, self.OnCancel)
        sizer.Add(button4, pos=(4, 4), span=(1, 1),
                  flag=wx.BOTTOM | wx.RIGHT, border=5)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)

    def brwse_cFiles(self,e):
        """
                Show the DirDialog and print the user's choice to stdout
                """
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           # | wx.DD_DIR_MUST_EXIST
                           # | wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.path_c = dlg.GetPath()
            self.tc1.SetValue(self.path_c)
        dlg.Destroy()

    def brwse_xlFiles(self,e):
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           # | wx.DD_DIR_MUST_EXIST
                           # | wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.path_x = dlg.GetPath()
            self.file_name = os.path.basename(os.path.normpath(self.path_x))
            self.path_x = self.path_x + '\\' + self.file_name + '.xls'  # 'D:\\VISsim\\nanda\\test.xls'#path for excel file
            self.tc2.SetValue(self.path_x)
        dlg.Destroy()

    def OnOK(self,e):
        Excel_Operations(self.path_x, self.path_c, self.file_name)

    def OnCancel(self,e):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title="Code Analyzer")
    app.MainLoop()