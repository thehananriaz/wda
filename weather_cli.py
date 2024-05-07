import pandas as pd
import sys
import argparse
import csv
from datetime import datetime
import json


def import_data(file_path):
    try:
        with open(file_path, "r") as file:
            data = []
            reader = csv.reader(file)
            first = next(reader)
            location = first[1]
            for i in range(0, 9):
                next(reader)
            for row in reader:
                tmp = float(row[1]) if row[1] else None
                data.append(
                    {"location": location, "date": row[0], "temperature": row[1]}
                )

            with open("data.json", "w") as json_file:
                json.dump(data, json_file)

            print(f"Imported data from {file_path}")
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")


# export cli command


def export_results(file_path, file_format="txt"):
    if file_format not in ["txt"]:
        print("only support txt.")
        return

    try:
        with open(file_path, "w", newline="") as file:
            with open("info.json", "r") as json_file:
                data = json.load(json_file)

            for key in data.keys():
                file.write(f"{key}: {data[key]}\n")
    except IOError:
        print(f"Error exporting results to {file_path}")


# analyz cli command
def analyze(start_date, end_date):

    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    if not data:
        print("No data found")
        return

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use year-month-day.")
        return
    print(data)
    filtered_data = [
        entry
        for entry in data
        if start_date <= datetime.strptime(entry["date"], "%Y%m%dT%H%M") <= end_date
    ]

    if not filtered_data:
        print("No data available for the specified time range.")
        return

    temperatures = [float(entry["temperature"]) for entry in filtered_data]
    # humidity = [float(entry["humidity"]) for entry in filtered_data]
    # wind_speed = [float(entry["wind_speed"]) for entry in filtered_data]
    avg_temp = sum(temperatures) / len(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    # avg_humidity = sum(humidity) / len(humidity)
    # trend_humidity = "increasing" if humidity[-1] > humidity[0] else "decreasing"
    # windiest_day = max(filtered_data, key=lambda x: float(x["wind_speed"]))
    print("Analysis results:")
    print(f"Average temperature: {avg_temp:.2f}°C")
    print(f"Minimum temperature: {min_temp:.2f}°C")
    print(f"Maximum temperature: {max_temp:.2f}°C")

    with open("info.json", "w") as json_file:
        json.dump(
            {
                "Average temperature": round(avg_temp, 2),
                "Minimum temperature": round(min_temp, 2),
                "Maximum temperature": round(max_temp, 2),
            },
            json_file,
        )
    # print(f"Average humidity: {avg_humidity:.2f}%")
    # print(f"Humidity trend: {trend_humidity}")
    # print(
    #     f"Windiest day: {windiest_day['date']} with {windiest_day['wind_speed']} km/h wind speed"
    # )


def main():
    parser = argparse.ArgumentParser(description="WEATHER CLI")
    # parser.add_argument('--import', help="Path to the input file")
    parser.add_argument("input", help="Path to the input file")
    parser.add_argument("--file", help="Path to the input file")
    parser.add_argument("--range", help="Time range in 'YYYY-MM-DD to YYYY-MM-DD'")
    parser.add_argument("--output", help="Path to the output file")

    args = parser.parse_args()

    print(args)

    if args.input == "import":
        if not args.file:
            print("Please provide a file path for import.")
        else:
            import_data(args.file)

    elif args.input == "analyze":
        if not args.range:
            print("Please provide a time range for analysis.")
        else:
            start_date, end_date = args.range.split(" to ")
            analyze(start_date, end_date)

    elif args.input == "export":
        if not args.output:
            print("Please provide a file path for export.")
        else:
            export_results(args.output)


main()
