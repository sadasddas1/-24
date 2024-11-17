import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    json_data = []
    with open(INPUT_FILENAME, "r", newline='', encoding='utf-8') as csv_file:
        read = csv.DictReader(csv_file)
        for row in read:
            json_data.append(row)
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
