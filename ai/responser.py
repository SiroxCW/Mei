
def responser(messages, api_key):
    import openai
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.9,
        messages=messages)
    messages.append({"role": "system", "content": response.choices[0].message["content"]})
    return messages

