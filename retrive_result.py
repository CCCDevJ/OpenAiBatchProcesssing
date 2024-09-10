# 3. To get result of batch

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Pass Result ID of batch processed
# Pass Document ID if need to get Batch Document Data
file_response = client.files.content("file-SRL3Mkg0s18WOqhtU6GROT6w")
print(file_response.text)
