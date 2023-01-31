import requests
import os
from bs4 import BeautifulSoup


URL = "https://www.nlb.lk/results/govisetha"

r = requests.get(URL)
c = r.content

soup = BeautifulSoup(c, "html.parser")

all_numbers_full = soup.find_all("ol", {"class": "B"})

final_dataset = []

for one_number_set in all_numbers_full:
        temp = []
        for item in one_number_set:
            value = item.text.strip()
            if value:
                temp.append(value)
        final_dataset.append(temp)

write_to = os.path.join(os.getcwd(), "data.csv")

if os.path.isfile(write_to):
    os.remove(write_to)
    
with open(write_to, "w", encoding="utf-8") as _file:
    for one_lottery in final_dataset:
        _file.write(','.join(one_lottery))
        _file.write("\n")

