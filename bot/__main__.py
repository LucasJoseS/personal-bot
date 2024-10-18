from bot.lib.register import register
from os import environ

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key=environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")
config = genai.GenerationConfig(temperature=2)

print(model.generate_content(
    "NCM valido para BATOM, diga apenas o mais utilizado, diga apenas o número",

    safety_settings={
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    },

    generation_config=config
).text)
