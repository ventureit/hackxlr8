import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from plotly.graph_objs import *
py.sign_in('ConradAddo', 'IeAV06EfLXpYFu07d0g5')
fig = {
  "data": [
    {
      "values": [30, 70],
      'marker': {'colors': ['rgb(200, 50, 75)',
                            'rgb(250, 217, 40)',
                            ]},
      "labels": [
          'Data Wasted',
          'Data Used'
                ],
      "textposition": "inside",
      "domain": {"x": [0, .48]},
      "name": "Unused Mobile Data",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title": "Unused UK Mobile Data",
        "plot_bgcolor":"rgb(200, 50, 75)",
        "annotations": [
            {
                "font": {
                    "family": "Arial, sans-serif",
                    "color": 'rgb(200, 50, 75)',
                    "size": 30
                },
                "showarrow": False,
                "text": "<br><b>30% of UK mobile users don't use 3.4GB of their data plan.<b></br>"
                        "<b>This amounts to roughly £93 million of unused data which could be resold.<b>",
                "x": 0.5,
                "y": 0.0
            },
            {
                "font": {
                "family": "Arial, sans-serif",
                "color": 'rgb(200, 50, 75)',
                "size": 80
                },
                "showarrow": True,
                "text": "<b>3.4GB<b>",
                "x": 0.245,
                "y": 0.48
            }

        ]
    }
}

fig["layout"].update({"plot_bgcolor":"rgb(182, 215, 168)"})
py.iplot(fig, filename='donut')

plot_url = py.plot(fig)
