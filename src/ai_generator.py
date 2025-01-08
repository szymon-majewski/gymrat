from openai import OpenAI
import requests
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("OPENAI_ACCESS_TOKEN")

client = OpenAI(api_key=ACCESS_TOKEN)


def generate_text(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


def generate_image(prompt, image_file_name):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    image_data = requests.get(image_url).content
    with open(image_file_name, "wb") as file:
        file.write(image_data)
