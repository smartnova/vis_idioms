scatterplot = dict(
  name='Scatterplot',
  what='Table: two quantitative value attributes',
  how=dict(explanation='Express values with horizontal and vertical spatial position and point marks',
           used=dict(mark='point',
                     quantitative=['position on common scale (horizontal)',
                                   'position on common scale (vertical)'],
                     category=['point'])),
  why=dict(find=['trends', 'outliers', 'distribution', 'correlation'],
           locate='cate clusters'),
  scale=dict(items='hundreds')
)

import json
with open('71-scatterplot.json', 'w') as w:
  json.dump(scatterplot, w)
