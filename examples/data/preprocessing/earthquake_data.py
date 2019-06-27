import os
import pandas as pd
import calendar
import datetime as dt
import requests

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime={start}&endtime={end}&minmagnitude=2.0&orderby=time"

for yr in range(2000, 2019):
    for m in range(1, 13):
        if os.path.isfile('{yr}_{m}.csv'.format(yr=yr, m=m)):
            continue
        _, ed = calendar.monthrange(yr, m)
        start = dt.datetime(yr, m, 1)
        end = dt.datetime(yr, m, ed, 23, 59, 59)
        with open('{yr}_{m}.csv'.format(yr=yr, m=m), 'w', encoding='utf-8') as f:
            f.write(requests.get(URL.format(start=start, end=end)).content.decode('utf-8'))

dfs = []
for i in range(2000, 2019):
    for m in range(1, 13):
        if not os.path.isfile('%d_%d.csv' % (i, m)):
            continue
        df = pd.read_csv('%d_%d.csv' % (i, m), dtype={'nst': 'float64'})
        dfs.append(df)
df = pd.concat(dfs, sort=True)
df.to_parquet('../earthquakes.parq', 'fastparquet')
