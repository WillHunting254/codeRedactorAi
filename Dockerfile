FROM vllm/vllm-openai:latest

WORKDIR /app

# Only install small dependencies
RUN pip install --no-cache-dir runpod fastapi uvicorn

# Copy your app files
COPY . /app

CMD ["python3", "-u", "handler.py"]

