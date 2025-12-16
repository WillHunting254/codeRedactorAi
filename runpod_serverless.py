import runpod
from server import llm  # reuse loaded model
from vllm import SamplingParams

def handler(event):
    prompt = event.get("prompt", "")
    max_tokens = event.get("max_tokens", 300)
    temperature = event.get("temperature", 0.7)

    params = SamplingParams(
        max_tokens=max_tokens,
        temperature=temperature,
    )

    result = llm.generate(prompt, params)
    text = result[0].outputs[0].text

    return {"response": text}

runpod.serverless.start({"handler": handler})
