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