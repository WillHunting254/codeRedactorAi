#!/bin/bash
uvicorn server:app --host 0.0.0.0 --port 8000 &
python3 -u runpod_serverless.py
