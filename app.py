import os
import time  
from google import genai 
from google.genai import types 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)
chat = client.chats.create(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="você é um chatbot que fala exclusivamente sobre the witcher",
        temperature=0.1,
        max_output_tokens=1000
    )
)

while True:
    entrada = input("")
    start = time.time()
    if entrada.lower == "sair":
        break
    response = chat.send_message_stream(entrada)
    for i, chunk in enumerate(response):
        if i == 0:
            first_token_time = time.time()
        print(chunk.text, end=" ")
    end = time.time()
    
    print(f"Latencia ate o primeiro token: {first_token_time - start:.2f} s")
    print(f"Tempo total de resposta: {end - start:.2f} s")