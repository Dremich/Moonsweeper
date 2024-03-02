import openai

openai.api_key = ''

def takeAction (preprompt, instructions, initial_state):

    prompt = ''
    with open(preprompt, 'r') as file:
      for line in file:
        prompt += line.strip()

    instruct = ''
    with open(instructions, 'r') as file:
      for line in file:
        instruct += line.strip()

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "system", "content": instruct},
        {"role": "user", "content": initial_state},
      ]
    )
    return print(response)
initialize('/content/preprompt.txt', '/content/instructions.txt', ['n', 0 ,1,2,4,5])
