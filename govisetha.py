import csv
import os
import typing as t

import requests
from bs4 import BeautifulSoup


class Govisetha:

    def __init__(self, url: str, filename_data: str, filename_stats: str) -> None:
        # Args
        self.url = url 
        self.filename_data = filename_data 
        self.filename_stats = filename_stats
        
        # Program Varibales
        # ...
    
    def scrapData(self, url: t.Optional[str] = None, filename_data: t.Optional[str] = None) -> None:
        return
    
    def analyzeData(self, url: t.Optional[str] = None, filename_data: t.Optional[str] = None, filename_stats=t.Optional[str] = None, data: t.Optional[str] = None) -> None:
        return
    
    
    