import os
from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI()

# Assume you have these files locally:
original_file = "original_file.png"
mask_file = "original_file_mask.png"
output_file = "image_no_watermark.png"

if not (os.path.exists(original_file) and os.path.exists(mask_file)):
    print(f"❌ Error: Make sure {original_file} and {mask_file} are in this folder.")
    exit(1)

try:
    # 3. Request the edit
    response = client.images.edit(
        model="dall-e-2",
        image=open(original_file, "rb"),
        mask=open(mask_file, "rb"),
        # We describe the DESIRED final state, not the problem.
        prompt="A clean, professional office background with consistent lighting and no text or watermarks.",
        size="1024x1024",
        n=1,
    )

    image_url = response.data[0].url
    print(f"🔗 Image generated at: {image_url}")

    print(f"📥 Downloading and saving to {output_file}...")
    img_data = requests.get(image_url).content

    with open(output_file, "wb") as handler:
        handler.write(img_data)

    print(f"✅ Success! File saved as {output_file}")

except Exception as e:
    print(f"💥 An error occurred: {e}")
