#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

# imports
import os
import json
import matplotlib
import datetime as dt
from collections import Counter, defaultdict
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates

# load data from input paths
total = defaultdict(Counter)
for filename in os.listdir('outputs/'):
    if filename.startswith('geoTwitter') and filename.endswith('.lang'):
        path = os.path.join('outputs', filename)
        with open(path) as f:
            data = json.load(f)
            date_str = filename.split('.')[0][10:]
            date = dt.datetime.strptime(date_str, '%y-%m-%d')
            total[date].update(data)

# organize data by keys and dates
new_dict = defaultdict(lambda: defaultdict(int))
for day, lang_counts in total.items():
    for key in args.keys:
        for lang in lang_counts.get(key, {}).values():
            new_dict[key][day] += lang

# plot data
fig, ax = plt.subplots()
for key, data in new_dict.items():
    dates = sorted(data.keys())
    values = [data[date] for date in dates]
    ax.plot(dates, values, label='#' + key[1:])
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1, bymonth=range(0, 13, 3)))

# add title and axis labels
ax.set_xlabel('Date')
ax.set_ylabel('Number of Tweets')
ax.legend()

# save plot
tags = [key[1:] for key in args.keys]
plt.savefig('line_plot.png')
