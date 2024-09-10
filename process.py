# 1. create batch in jsonl formate
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

path = "./batches/batch1.jsonl"

batch_input_file = client.files.create(
    file=open(path, "rb"),
    purpose="batch"
)

batch_input_file_id = batch_input_file.id

responses = client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
        "description": "nightly eval job"
    }
)

print(responses)
