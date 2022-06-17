
import pandas as pd
import plotly
import plotly.graph_objects as go
class Plots:
    pd.options.plotting.backend = "plotly"
    data = ""

    def __init__(self,data):
        self.data = data

    def popularity_plot(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(self.data.keys()),y=list(self.data.values())))
        fig.update_layout(
            title='Popularity',
            xaxis_tickformat='%d %B %A<br>%Y'
        )
        fig.show()

    def sentiment_plot(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(self.data.keys()),y=list(self.data.values())))
        fig.update_layout(
            title='Sentiment',
            xaxis_tickformat='%d %B %A<br>%Y'
        )
        fig.show()

