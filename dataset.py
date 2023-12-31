import os
import openai
from dotenv import load_dotenv
import json
from datasets import load_dataset

load_dotenv()  # Load the .env file

# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

generation_prompt = """Generate 40 examples of conversations, where an initial statement is made, followed by two replies, one that agrees with the initial statement and one that disagrees with the initial statement. The initial statement could be right, wrong, or neither right nor wrong.

Structure of the conversation like this:
[
  {
    "statement": "<initial statement>",
    "agree": "<reply that agrees with the initial statement>",
    "disagree": "<reply that disagrees with the initial statement>"
  },
  {
    "statement": "<initial statement>",
    "agree": "<reply that agrees with the initial statement>",
    "disagree": "<reply that disagrees with the initial statement>"
  }
]"""


def format_dataset(dataset):
    print("formatting dataset...")
    formatted_dataset = []

    for item in dataset:
        agree_obj = {
            "statement": item["statement"],
            "reply": item["agree"],
            "sentiment": 1,
        }
        formatted_dataset.append(agree_obj)

        disagree_obj = {
            "statement": item["statement"],
            "reply": item["disagree"],
            "sentiment": 0,
        }
        formatted_dataset.append(disagree_obj)

    return formatted_dataset


def generate_dataset(n_call, filename="dataset.json"):
    print("generating dataset...")
    dataset = []

    for i in range(n_call):
        print(f"api call {i+1}/{n_call}")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": generation_prompt}],
        )
        try:
            data = json.loads(response["choices"][0]["message"]["content"])
        except:
            print("response skipped")
            continue
        dataset.extend(data)

    formatted_dataset = format_dataset(dataset)

    print(f"writing dataset to {filename}...")
    with open(filename, "w") as f:
        json.dump(formatted_dataset, f, indent=2)


def upload_dataset(filename="dataset.json", repo_id="daspartho/agree_disagree"):
    print(f"uploading {filename} to {repo_id}...")
    dataset = load_dataset("json", data_files=filename)
    dataset.push_to_hub(repo_id)


if __name__ == "__main__":
    generate_dataset(n_call=25)
    upload_dataset()
