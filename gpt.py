from openai import OpenAI
import config

# Initialize the OpenAI client with the API key from config.py
client = OpenAI(
    api_key=config.gpt_api_key,
)


# Function to query ChatGPT
def ask_chatgpt(prompt):
    """
    Sends a prompt to the GPT-4o model and returns the text response.

    Args:
        prompt (str): The text prompt to send to the ChatGPT model.

    Returns:
        str: The text output from the ChatGPT model.
    """
    response = client.responses.create(
        model="gpt-4o",  # Specifies the model to use (GPT-4o)
        instructions="You are a helpful assistant, taking requests and orders from a speech-to-text script.",  # System instructions for the model
        input=prompt,
    )

    return response.output_text