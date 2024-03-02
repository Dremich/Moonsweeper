import openai
import os

# openai.api_key = os.getenv('OPEN_API_KEY')
openai.api_key = "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"

def takeAction(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = prompt,
    temperature = 0.3
    )
    data = response.choices[0].message
    return (data, print(response.choices[0].message))
