import openai
import os

openai.api_key = os.getenv('OPEN_API_KEY')

def takeAction(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = prompt
    )
    data = response.choices[0].message
    return (data, print(response.choices[0].message))
