import os
import openai
from dotenv import load_dotenv
import json

load_dotenv() # Load the .env file

# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

generation_prompt="""Generate 40 examples of conversations, where an initial statement is made, followed by two replies, one that agrees with the initial statement and one that disagrees with the initial statement. The initial statement could be right, wrong, or neither right nor wrong.

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

def generate():

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": generation_prompt}])

    return json.loads(response['choices'][0]['message']['content'])

if __name__=="__main__":
    print(json.dumps(generate(), indent = 2))