import os
from openai import OpenAI


def takeAction(prompt):
    client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = prompt,
    temperature = 0.5
    )
    data = response.choices[0].message.content
    print(data)
    return data
