import json
import pandas as pd

def export_to_json(data, filename='output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def export_to_excel(data, filename):
    flat_data = []
    for card in data:
        flat_card = {
            "Name": card.get("name", ""),
            "Annual Fee": card.get("Annual Fee", ""),
            "Rewards": card.get("Rewards", ""),
            "Lounge Access": card.get("Lounge Access", ""),
            # add more fields as needed
        }
        flat_data.append(flat_card)

    df = pd.DataFrame(flat_data)
    df.to_excel(filename, index=False)


def export_to_txt(data, filename='output.txt'):
    with open(filename, 'w') as f:
        for item in data:
            for key, val in item.items():
                f.write(f"{key}: {val}\n")
            f.write("\n")
