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




#export cli command 

def export_results(self, file_path, file_format='txt'):
        if file_format not in ['txt', 'csv']:
            print("Invalid export format. Supported formats: txt, csv.")
            return

        try:
            with open(file_path, 'w', newline='') as file:
                if file_format == 'txt':
                    file.write("Analysis Results:\n")
                    file.write(f"Average Temperature: {avg_temp:.2f}°C\n")
                    file.write(f"Minimum Temperature: {min_temp:.2f}°C\n")
                    file.write(f"Maximum Temperature: {max_temp:.2f}°C\n")
                    file.write(f"Average Humidity: {avg_humidity:.2f}%\n")
                    file.write(f"Humidity Trend: {trend_humidity}\n")
                    file.write(f"Windiest Day: {windiest_day['date']} with {windiest_day['wind_speed']} km/h wind speed\n")
                elif file_format == 'txt':
                    fieldnames = ['Metric', 'Value']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow({'Metric': 'Average Temperature', 'Value': avg_temp})
                    writer.writerow({'Metric': 'Minimum Temperature', 'Value': min_temp})
                    writer.writerow({'Metric': 'Maximum Temperature', 'Value': max_temp})
                    writer.writerow({'Metric': 'Average Humidity', 'Value': avg_humidity})
                    writer.writerow({'Metric': 'Humidity Trend', 'Value': trend_humidity})
                    writer.writerow({'Metric': 'Windiest Day', 'Value': f"{windiest_day['date']} with {windiest_day['wind_speed']} km/h wind speed"})
            print(f"Exported analysis results to {file_path}")
        except IOError:
            print(f"Error exporting results to {file_path}")





# cmd = sys.argv[1]

# if cmd == 'analyze':
#     if sys.argv[2] == '--range':
#         range_str = sys.argv[3].split(' ')
#         start_date = range_str[0]
#         end_date = range_str[2]
#         analyze(df, start_date, end_date)


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


