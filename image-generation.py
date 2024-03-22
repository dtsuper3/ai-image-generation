import requests
import os
from dotenv import load_dotenv
import random
import string
# from utils.image_to_svg import imageToSVG

load_dotenv()
STABILITY_API_KEY = os.getenv('STABILITY_API_KEY')

def generate_random_filename(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"Bearer {STABILITY_API_KEY}",
        "accept": "image/*"
    },
    files={
        "none": ''
    },
    data={
        "prompt": "taj mahal in coral blue color",
        "output_format": "png",
    },
)

if response.status_code == 200:
    filename=generate_random_filename(10)
    with open(f"./{filename}.png", 'wb') as file:
        file.write(response.content)
    # imageToSVG(f"./{filename}.png",filename)
else:
    raise Exception(str(response.json()))