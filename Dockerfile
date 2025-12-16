FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

# System deps
RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    apt-get clean

# Install Python deps
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Copy app code
COPY . /app
WORKDIR /app

# Expose FastAPI port
EXPOSE 8000

# Start script
CMD ["bash", "start.sh"]
