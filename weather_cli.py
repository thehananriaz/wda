import pandas as pd
import sys
import argparse
import csv
from datetime import datetime



#import file cli
# data = pd.read_csv(r"raw_weather_data.csv")
# df = pd.DataFrame(data, columns= ["Mintemp","MaxTemp"])

def import_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
            print(f"Imported data from {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")




