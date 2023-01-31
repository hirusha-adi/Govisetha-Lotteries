import os

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

class Govisetha:
    
    def __init__(self, filename_analyzed = "govisetha_analyzed.csv", filename_dataset = "govisetha_dataset.csv", filename_image = "govisetha_analyzed.png") -> None:
        self.url = "https://www.nlb.lk/results/govisetha"
        self.filename_analyzed = os.path.join(os.getcwd(), filename_analyzed if filename_analyzed.endswith(".csv") else f"{filename_analyzed}.csv")
        self.filename_dataset = os.path.join(os.getcwd(), filename_dataset if filename_dataset.endswith(".csv") else f"{filename_dataset}.csv")
        self.filename_image = os.path.join(os.getcwd(), filename_image if filename_image.endswith(".png") else f"{filename_image}.png")
        
        self.session = requests.Session()
        self.soup = None

    def scrapData(self, saveToFile = False):
        r = self.session.get(self.url)
        self.soup = BeautifulSoup(r.content, "html.parser")
        all_numbers_full = self.soup.find_all("ol", {"class": "B"})
        self.final_dataset  = [
            [item.text.strip() for item in one_number_set if item.text.strip()]
            for one_number_set in all_numbers_full
        ]
        if saveToFile: 
            df = pd.DataFrame(self.final_dataset)
            df.to_csv(self.filename_dataset, index=False, encoding='utf-8')

    def analyzeData(self, loadFromFile = False, data = None, saveToFile = True):
        if loadFromFile:
            df = pd.read_csv(self.filename_analyzed)
        else:
            val = data or self.final_dataset
            df = pd.DataFrame(val)
        values_only = df.values.flatten()
        counter = pd.Series(values_only).value_counts().to_dict()
        repeats_sorted = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        if saveToFile:
            df = pd.DataFrame(repeats_sorted, columns=['Value', 'Count'])
            df.to_csv(self.filename_analyzed, index=False)
                    
    def visualizeData(self, saveToFile = True, filename = None):
        df = pd.read_csv(self.filename_analyzed)

        plt.figure(figsize=(20,10))
        plt.bar(df['Value'], df['Count'], color="purple")

        plt.xticks(rotation=90)
        plt.xlabel("Value")
        plt.ylabel("Repeated Number of Times")
        plt.tight_layout()
        
        if saveToFile:
            plt.savefig(filename or self.filename_image)
        plt.show()



if __name__ == "__main__":
    x = Govisetha()
    x.scrapData()
    x.analyzeData()
    x.visualizeData()
    