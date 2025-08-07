# cohere_text_generator.py
# This script uses the Cohere API to generate text based on a given prompt.

import cohere

# Initialize Cohere Client with your API key
co = cohere.Client('U8bkVHbsy2ewDW7Deh2CRFSOhpV7Z00s4EBt7Hlb')

# Prompt to generate text
prompt = "Write a short paragraph about the future of artificial intelligence."

# Call the Cohere generate endpoint
response = co.generate(
    model='command',  # Use 'command' or 'command-nightly' for better performance
    prompt=prompt,
    max_tokens=100
)

# Print the generated text
print("Generated Text:\n", response.generations[0].text)

