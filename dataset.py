import os
import openai
from dotenv import load_dotenv

load_dotenv() # Load the .env file

# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

generation_prompt="""Generate 10 examples of conversations, where an initial statement is made, followed by two replies, one that agrees with the initial statement and one that disagrees with the initial statement. The initial statement could be right, wrong, or neither right nor wrong (like a political statement).

Structure of the conversation like this:

Statement: <initial statement>
Agree: <reply that agrees with the initial statement>
Disagree: <reply that disagrees with the initial statement>"""

def generate():

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": generation_prompt}])

    return response['choices'][0]['message']['content']

if __name__=="__main__":
    for i in range(5):
        print(generate())