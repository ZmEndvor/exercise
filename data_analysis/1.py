import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series

path = '../pydata-book/datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]

time_zones = [res["tz"] for res in records if "tz" in res]


def get_counts(sequence):
    counts = {}
    for i in sequence:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts


def get_counts1(sequence):
    counts = defaultdict(int)
    for i in sequence:
        counts[i] += 1
    return counts


counts = get_counts(time_zones)


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


counts1 = Counter(time_zones)
print(counts1.most_common(10))

frame = DataFrame(records)
print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])
clean_tz = frame["tz"].fillna('Missing')
clean_tz[clean_tz == ""] = "Unknown"
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
tz_counts[:10].plot(kind="barh", rot=0)
