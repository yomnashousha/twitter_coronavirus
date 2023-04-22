#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# plotting bar graphs
for k,v in reversed(items[:10]):
    plt.bar(k, v, color='blue')
    
# language identification
if "코로나바이러스" in args.key:
    language = "Korean"
else:
    language = "English"

# titling axes and graphs
if args.input_path == "reduced.lang":
    plt.xlabel("Language")
    plt.ylabel("Number of Tweets")
else:
    plt.xlabel("Country")
    plt.ylabel("Number of Tweets")

# graph as PNG file
if args.input_path == "reduced.lang":
     plt.savefig(args.key[1:] + '_lang.png')
else:
    plt.savefig(args.key[1:] + '_country.png')
