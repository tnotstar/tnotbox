#!/usr/bin/env python3
# -*- coding: utf-8 -*-

FILENAME = "usagov_bitly_data2012-03-16-1331923249.txt"

def handcraft(fname):
    """Blah, blah, blah, ..."""

    from json import loads
    from collections import defaultdict, Counter

    records = [loads(line) for line in open(fname)]
    time_zones = [record["tz"] for record in records if "tz" in record]

    def get_counts(sequence):
        counts = defaultdict(int)
        for item in sequence:
            counts[item] += 1
        return counts
    counts = get_counts(time_zones)

    def top_counts(counts, n=10):
        pairs = [(count, tz) for tz, count in counts.items()]
        pairs.sort()
        return pairs[-n:]
    top_ten = top_counts(counts)

    counter = Counter(time_zones)
    counter.most_common(10)

def withpandas(fname):
    from json import loads
    from pandas import DataFrame
    from matplotlib.pyplot import show

    records = [loads(line) for line in open(fname)]
    frame = DataFrame(records)
    clean_tz = frame["tz"].fillna("Missing")
    clean_tz[clean_tz == ""] = "Unknown"
    tz_counts = clean_tz.value_counts()
    tz_counts[:10]

    tz_counts[:10].plot(kind="barh", rot=0)
    show()

if __name__ == "__main__":
    handcraft(FILENAME)
    withpandas(FILENAME)

# EOF