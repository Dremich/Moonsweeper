from openai import OpenAI


def takeAction(prompt):
    client = OpenAI(api_key = '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')
    response = client.Chat.completions.create(
    model="gpt-3.5-turbo",
    messages = prompt,
    temperature = 0.3
    )
    data = response.choices[0].message
    return (data, print(response.choices[0].message))
