from fastapi import FastAPI
from pydantic import BaseModel
from vllm import LLM, SamplingParams

app = FastAPI()

# Load model once on startup
llm = LLM(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    quantization="awq"
)

class Prompt(BaseModel):
    prompt: str
    max_tokens: int = 300
    temperature: float = 0.7

@app.post("/generate")
async def generate(data: Prompt):
    params = SamplingParams(
        max_tokens=data.max_tokens,
        temperature=data.temperature,
    )

    outputs = llm.generate(data.prompt, params)
    text = outputs[0].outputs[0].text

    return {"response": text}
