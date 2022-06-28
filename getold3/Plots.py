import pandas as pd
import plotly
import plotly.graph_objects as go


class Plots:
    pd.options.plotting.backend = "plotly"

    def __init__(self):
        self.fig = go.Figure()
        self.config = dict({'scrollZoom': True})

    def popularity_plot(self,data):
        self.fig.add_trace(go.Scatter(x=list(data.keys()), y=list(data.values())))
        self.fig.update_layout(
            title='Popularity',
            xaxis_tickformat='%d-%m-%Y',
            yaxis_rangemode = 'nonnegative'
        )
        self.fig.show(config=self.config)

    def sentiment_plot(self,data):
        self.fig.add_trace(go.Scatter(x=list(data.keys()), y=list(data.values())))
        self.fig.update_layout(
            title='Sentiment',
            xaxis_tickformat='%d-%m-%Y',
            yaxis_rangemode= 'nonnegative'
        )
        self.fig.show(condig=self.config)
