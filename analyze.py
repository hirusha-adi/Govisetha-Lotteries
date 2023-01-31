import os 
import pandas as pd

filename = "data.csv"

df = pd.read_csv(filename)

values_only = df.values.flatten()

counter = pd.Series(values_only).value_counts().to_dict()

repeats_sorted = sorted(counter.items(), key=lambda x:x[1], reverse=True)

if os.path.isfile("repeats.csv"):
    os.remove("repeats.csv")

df = pd.DataFrame(repeats_sorted, columns=['Value', 'Count'])
df.to_csv('repeats.csv', index=False)
