import pandas as pd
import plotly
import plotly.graph_objects as go


class Plots:
    pd.options.plotting.backend = "plotly"

    def popularity_plot(self,data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(data.keys()), y=list(data.values())))
        fig.update_layout(
            title='Popularity',
            xaxis_tickformat='%d %B %A<br>%Y'
        )
        fig.show()

    def sentiment_plot(self,data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(data.keys()), y=list(data.values())))
        fig.update_layout(
            title='Sentiment',
            xaxis_tickformat='%d %B %A<br>%Y'
        )
        fig.show()
