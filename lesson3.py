from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import os
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(  
  base_url = "https://hpacleb1997-1272-resource.openai.azure.com/openai/v1", 
  api_key=token_provider,
)

response = openai_client.responses.create(
    model="DeepSeek-V4-Flash",
    input="Explain machine learning in simple terms."
)

print(f"Response: {response.output_text}")
print(f"Response ID: {response.id}")
print(f"Tokens used: {response.usage.total_tokens}")
print(f"Status: {response.status}")
