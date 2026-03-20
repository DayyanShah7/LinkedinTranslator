import os
import requests
from dotenv import load_dotenv
from prompts import build_prompt

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = os.getenv("HF_MODEL", "katanemo/Arch-Router-1.5B:hf-inference")

if not HF_API_KEY:
    raise ValueError("HF_API_KEY not found in .env file")

API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json",
}


def generate_linkedin_post(user_text: str, mode: str = "linkedin_cringe") -> str:
    prompt = build_prompt(user_text, mode)

    payload = {
        "model": HF_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You rewrite plain text into exaggerated LinkedIn-style posts. "
                    "Be funny, dramatic, polished, and absurdly professional."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "max_tokens": 220,
        "temperature": 0.9,
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)

    if response.status_code != 200:
        raise Exception(f"Hugging Face router error {response.status_code}: {response.text}")

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()