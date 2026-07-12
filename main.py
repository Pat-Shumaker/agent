import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

# Load api key
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("api key not retrieved")

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

messages=[
    {
        "role": "user",
        "content": args.user_prompt,
    },
]

response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )

if not response.usage:
    raise RuntimeError("Failed API request")

prompt_usage = response.usage.prompt_tokens
response_usage = response.usage.completion_tokens

if args.verbose == True:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {prompt_usage}\nResponse tokens: {response_usage}")
print(response.choices[0].message.content)

def main():
    pass


if __name__ == "__main__":
    main()
