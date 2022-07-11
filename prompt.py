def natural_language_prompt(prompt):
    print("sending prompt:", prompt)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1012,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response.get("choices", [{"text": ""}])[0].get("text","")
    print("natural_language_prompt got_response ", response_text)
    return response_text

def code_example_prompt(prompt):
    print("sending prompt:", prompt)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.17,
        presence_penalty=0.17
    )
    response_text = response.get("choices", [{"text": ""}])[0].get("text","")
    print("code_example_prompt got_response ", response_text)
    return response_text

def discerning_natural_language_prompt(prompt):
    print("sending prompt:", prompt)
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1012,
        top_p=1,
        frequency_penalty=0.24,
        presence_penalty=0.23
    )
    response_text = response.get("choices", [{"text": ""}])[0].get("text","")
    print("discerning_natural_language_prompt got_response ",response_text)
    return response_text