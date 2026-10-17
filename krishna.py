from openai import OpenAI
import base64

client = OpenAI()

prompt = """
Create a highly realistic, HD devotional portrait of Lord Krishna.
Krishna has a serene divine expression, blue skin, beautiful traditional
Indian clothing, ornate golden jewelry, a peacock feather crown, and a
flute. He is standing in a peaceful Vrindavan setting with soft golden
divine light, flowers, trees and a subtle spiritual atmosphere.
Photorealistic, cinematic lighting, extremely detailed face and clothing,
natural skin texture, high resolution, devotional and respectful artwork.
No cartoon, no anime, no text, no watermark.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1024"
)

image_bytes = base64.b64decode(result.data[0].b64_json)

with open("krishna_hd.png", "wb") as f:
    f.write(image_bytes)

print("✅ Krishna ji ki HD image ban gayi!")
print("📁 File: krishna_hd.png")