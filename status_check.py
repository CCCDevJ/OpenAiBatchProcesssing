# 2. Check Status of batch


# Status	Description
# validating	the input file is being validated before the batch can begin
# failed	the input file has failed the validation process
# in_progress	the input file was successfully validated and the batch is currently being run
# finalizing	the batch has completed and the results are being prepared
# completed	the batch has been completed and the results are ready
# expired	the batch was not able to be completed within the 24-hour time window
# cancelling	the batch is being cancelled (may take up to 10 minutes)
# cancelled	the batch was cancelled

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

# Pass Batch ID to get status
response = client.batches.retrieve("batch_MM3nhdq0WwxXioVxXmpWz498")
print(response)
