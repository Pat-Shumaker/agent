import os
from dotenv import load_dotenv
from openai import OpenAI

# Load api key
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if isinstance(api_key, str):
    pass
else:
    raise RuntimeError("api key not retrieved")

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages=[
    {
        "role": "user",
        "content": "one sentence test",
    }
]

response = client.chat.completions.create(model="openrouter/free",
                               messages=messages)

print(response.choices[0].message.content)

def main():
    pass


if __name__ == "__main__":
    main()
