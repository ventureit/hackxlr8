import plotly.plotly as py
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from plotly.graph_objs import *

py.sign_in('ConradAddo', 'IeAV06EfLXpYFu07d0g5')
apikey = 'IeAV06EfLXpYFu07d0g5'
xdata = (1.2, 2.1, 1, 1.5, 0.6, 2.2, 3),
trace1 = go.Bar(
    x=(1.84, 2.67, 1.54, 2.22, 0.74, 2.71, 3.83),
    y=('UK', 'US', 'Australia', 'Turkey', 'Mexico', 'Switzerland', 'South Korea'),
    name='Gigabytes used 2014'

)
trace2 = go.Bar(

    x=(1.84, 2.67, 1.54, 2.22, 0.74, 2.71, 3.83),
    y=('UK', 'US', 'Australia', 'Turkey', 'Mexico', 'Switzerland', 'South Korea'),
    name='Gigabytes used 2017',
    )

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack',
    title='Data usage is increasing gradually worldwide'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='stacked-bar')

plot_url = py.plot(fig)
