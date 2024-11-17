import json
INPUT_FILE = "input.json"
def task() -> float:
    with open(INPUT_FILE, "r") as file:
        data = json.load(file)
        total = sum(entry['score'] * entry['weight'] for entry in data)
        return round(total, 3)





print(task())
