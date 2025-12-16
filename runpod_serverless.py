import runpod
from vllm import LLM, SamplingParams

# Load model once per worker
llm = LLM(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    quantization="awq"
)

def handler(event):
    input_data = event.get("input", {})
    prompt = input_data.get("prompt", "")
    max_tokens = min(input_data.get("max_tokens", 256), 256)
    temperature = min(input_data.get("temperature", 0.7), 1.0)

    params = SamplingParams(
        max_tokens=max_tokens,
        temperature=temperature
    )

    outputs = llm.generate(prompt, params)
    text = outputs[0].outputs[0].text

    return {
        "output": text
    }

runpod.serverless.start({
    "handler": handler
})
