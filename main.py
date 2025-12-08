import wx 
import pandas as pd
import matplotlib.pyplot as plt

x_axis = "age"
y_axis = "blood_pressure"

class ChronicKidneyDisApp(wx.Frame):
    def __init__(self, parent=None, title="Chronic Kidney Disease Dataset"):
        super().__init__(parent, title=title, size=(855, 555))
        self.SetMinSize((780, 500))
        panel = wx.Panel(self)
        
        button = wx.Button(panel, label="Open Chronic Kidney Disease Dataset")
        font = button.GetFont()
        font.PointSize += 2
        button.SetFont(font)
        button.Bind(wx.EVT_BUTTON, self.on_open)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.AddStretchSpacer(2)  # more whitespace below
        panel.SetSizer(sizer)