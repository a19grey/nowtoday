from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def call_openai_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is creative and can generate engaging content for a modeern audience"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2050
    )
    return response.choices[0].message.content.strip()
