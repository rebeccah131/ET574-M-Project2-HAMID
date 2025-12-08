import wx 
import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 400))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Buttons
        self.load_btn = wx.Button(panel, label='Load CSV')
        self.load_btn.Bind(wx.EVT_BUTTON, self.load_csv)
        vbox.Add(self.load_btn, 0, wx.ALL | wx.CENTER, 10)

        self.bar_btn = wx.Button(panel, label='Show Bar Graph')
        self.bar_btn.Bind(wx.EVT_BUTTON, self.show_bar_graph)
        vbox.Add(self.bar_btn, 0, wx.ALL | wx.CENTER, 10)

        self.pie_btn = wx.Button(panel, label='Show Pie Chart')
        self.pie_btn.Bind(wx.EVT_BUTTON, self.show_pie_chart)
        vbox.Add(self.pie_btn, 0, wx.ALL | wx.CENTER, 10)

        