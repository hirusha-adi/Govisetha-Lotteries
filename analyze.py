import csv, os
from collections import Counter

filename = "data.csv"

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    loaded_dataset = [row[:] for row in reader]

values_only = []
for line in loaded_dataset:
    for number in line:
        values_only.append(number)

values_only_unique = set(values_only)

print(len(values_only))    
print(len(values_only_unique))    

data = {}
for unique_value in values_only_unique:
    data[unique_value] = values_only.count(unique_value)

repeats_sorted = sorted(data.items(), key=lambda x:x[1], reverse=True)

if os.path.isfile("repeats.csv"):
    os.remove("repeats.csv")

with open("repeats.csv", "w", encoding="utf-8") as _file:
    for repeat in repeats_sorted:
        _file.write(f"{repeat[0]},{repeat[1]}\n")
        print(repeat)
            