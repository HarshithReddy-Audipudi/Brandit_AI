import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your API key
openai.api_key =""
# Call the OpenAI API with the updated model
response = openai.Completion.create(
    model="gpt-3.5-turbo",  # Replace "davinci" with "gpt-3.5-turbo"
    prompt="This is a test",  # Your input prompt
    max_tokens=5  # Limit the output tokens
)

# Print the response
print(response.choices[0].text.strip())  # Extract and print the generated text
