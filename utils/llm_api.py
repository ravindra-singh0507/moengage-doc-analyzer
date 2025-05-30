import os
from openai import OpenAI

# Get the key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Explicitly initialize the OpenAI client
client = OpenAI(api_key=api_key)

def get_llm_analysis(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content
