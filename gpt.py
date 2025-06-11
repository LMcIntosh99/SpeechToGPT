from openai import OpenAI
import config

client = OpenAI(
    # This is the default and can be omitted
    api_key=config.gpt_api_key,
)


# Function to query ChatGPT
def ask_chatgpt(prompt):
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a helpful assistant, taking requests and orders from a speech-to-text script.",
        input=prompt,
    )

    return response.output_text
