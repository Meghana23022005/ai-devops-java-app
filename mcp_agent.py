import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_failure(log_file):
    with open(log_file, "r", errors="ignore") as f:
        logs = f.read()

    prompt = f"""
You are an AI DevOps assistant.

IMPORTANT:
- Focus ONLY on the LAST ERROR in the logs
- Identify the FAILED STAGE
- Ignore successful stages

Answer:
1. Which stage failed?
2. Exact error message
3. Root cause
4. Fix

Logs:
{logs[-4000:]}
"""

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    print("\n[MCP AI AGENT OUTPUT]\n")
    print(response.json()["response"])

if __name__ == "__main__":
    analyze_failure(sys.argv[1])
