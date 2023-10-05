import json
from datasets import load_dataset

dataset = load_dataset("Alamerton/small-sycophancy-dataset", split="train")
dataset.to_json("Alamerton/small-sycophancy-dataset.json")
new_data = []

for item in dataset:
    agree_obj = {
        "statement": item["statement"],
        "reply": item["agree"],
        "sentiment": 1
    }
    new_data.append(agree_obj)

    disagree_obj = {
        "statement": item["statement"],
        "reply": item["disagree"],
        "sentiment": 0
    }
    new_data.append(disagree_obj)

new_json = json.dumps(new_data, indent=4)
print(new_json)
