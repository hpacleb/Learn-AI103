import asyncio
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = AsyncOpenAI(  
  base_url = "https://hpacleb1997-1272-resource.openai.azure.com/openai/v1", 
  api_key=token_provider(),
)


async def ask(prompt):
    response = await client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )
    return response.output_text

async def main():
    # Issue three requests concurrently instead of one after another
    prompts = [
        "Explain quantum computing briefly.",
        "Summarize the benefits of async I/O.",
        "Give a one-sentence definition of machine learning."
    ]
    results = await asyncio.gather(*(ask(p) for p in prompts))
    for prompt, output in zip(prompts, results):
        print(f"Q: {prompt}\nA: {output}\n")

asyncio.run(main())
