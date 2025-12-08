import wx 
import pandas as pd
import numpy as np
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

        panel.SetSizer(vbox)

        self.df = None  # Placeholder for the DataFrame

        self.Centre()
        self.Show()

    def load_csv(self, event):
        with wx.FileDialog(self, "Open CSV file", wildcard="CSV files (*.csv)|*.csv",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            path = fileDialog.GetPath()
            try:
                self.df = pd.read_csv(path)
                wx.MessageBox(f"CSV loaded successfully!\nRows: {len(self.df)}, Columns: {len(self.df.columns)}",
                              "Info", wx.OK | wx.ICON_INFORMATION)
            except Exception as e:
                wx.MessageBox(f"Failed to load CSV:\n{e}", "Error", wx.OK | wx.ICON_ERROR)

    def show_bar_graph(self, event):
        if self.df is None:
            wx.MessageBox("Please load a CSV first!", "Error", wx.OK | wx.ICON_ERROR)
            return
        
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        if len(numeric_cols) == 0:
            wx.MessageBox("No numeric columns available for bar graph.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Simple bar graph: mean of numeric columns
        means = self.df[numeric_cols].mean()
        means.plot(kind='bar', color='skyblue')
        plt.title("Bar Graph of Numeric Columns (Mean Values)")
        plt.ylabel("Mean")
        plt.xlabel("Columns")
        plt.show()

    def show_pie_chart(self, event):
        if self.df is None:
            wx.MessageBox("Please load a CSV first!", "Error", wx.OK | wx.ICON_ERROR)
            return

        numeric_cols = self.df.select_dtypes(include=np.number).columns
        if len(numeric_cols) == 0:
            wx.MessageBox("No numeric columns available for pie chart.", "Error", wx.OK | wx.ICON_ERROR)
            return

 # Simple pie chart: sum of numeric columns
        sums = self.df[numeric_cols].sum()
        sums.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title("Pie Chart of Numeric Columns (Sum Values)")
        plt.ylabel("")
        plt.show()

if __name__ == "__main__":
    app = wx.App()
    DataVisualizer(None, title="Dataset Visualizer")
    app.MainLoop()
