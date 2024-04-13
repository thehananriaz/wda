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



def main():
    parser = argparse.ArgumentParser(description="WEATHER CLI")
    parser.add_argument('--file', help="Path to the input file")
    parser.add_argument('--range', help="Time range in format 'YYYY-MM-DD to YYYY-MM-DD'")
    parser.add_argument('--output', help="Path to the output file")
 
    args = parser.parse_args()

    analyzer = analyze()

    if args.command == 'import':
        if not args.file:
            print("Please provide a file path for import.")
        else:
            analyzer.import_data(args.file)

    elif args.command == 'analyze':
        if not args.range:
            print("Please provide a time range for analysis.")
        else:
            start_date, end_date = args.range.split(' to ')
            analyzer.analyze(start_date, end_date)

    elif args.command == 'export':
        if not args.output:
            print("Please provide a file path for export.")
        else:
            analyzer.export_results(args.output, args.format)


