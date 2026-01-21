import urllib.request # For making HTTP requests
import json  # For parsing JSON data
from datetime import datetime  # For handling date and time

file_name = "Covid_Data.txt"

def get_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())

    cases = data["cases"]
    deaths = data["deaths"]
    recovered = data["recovered"]
    active = data["active"]

    return cases,deaths,recovered,active

def save_data(cases,deaths,recovered,active):
    with open(file_name, "a") as file:
        file.write(
            f"Date: {datetime.now()}\n"   #Formatted String, insert variables or expressions directly inside a string
            f"Total Cases: {cases}\n"
            f"Deaths : {deaths}\n"
            f"Recovered : {recovered}\n"
            f"Active  : {active}\n"
        )

def read_data():
    print("Covid History Data")
    with open(file_name, "r") as file:
        print(file.read())

def main():
    cases,deaths,recovered,active = get_data()
    save_data(cases,deaths,recovered,active)
    read_data()

if __name__ == "__main__":
    main()