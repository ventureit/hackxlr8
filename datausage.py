import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

import plotly as py
import plotly.tools as tls

mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)
apikey = 'IeAV06EfLXpYFu07d0g5'
# xl = pd.ExcelFile('C:/Users/Cataconia/Documents/piggyme_datausage.xlsx')
# df = xl.parse('country')
# N = df.shape[0]
y1 = (20, 35, 30, 35, 27)
y2 = (25, 32, 34, 20, 25)
ylabels = ('UK', 'US', 'Australia', 'India', 'China')
N = len(y1)
ind = np.arange(N)
# y1 = df.iloc[:, 1]
# y2 = df.iloc[:, 2]
# y1 = np.y1

width = 0.35

p1 = ax.bar(ind, y1, width, color=(0.2588, 0.4433, 1.0))
p2 = ax.bar(ind, y2, width, color=(1.0, 0.5, 0.62), bottom=y1)
ax.set_xlabel('Country')
ax.set_ylabel('USD cents/minute')
ax.set_title('Mobile Termination Rates')

ax.set_xticks(ind + width/2.)
# ax.set_yticks(np.arange())
ax.set_xticklabels(ylabels)

plotly_fig = tls.mpl_to_plotly(mpl_fig)

plot_url = py.offline.plot(plotly_fig, filename='Mobile Termination Rates')
3.365
1.057
1.55

2.934
1.28
1.213
1.445
3.678
1.051
2.351
1.53
3.1649
1.41
3.415
1.554
1.287
4.729
2.597

1.287
2.17
2.444
2.98
2.584
1.338
1.668
1.226
1.497
1.432
1.288
7.244
1.157
1.403
0.07
2.10

