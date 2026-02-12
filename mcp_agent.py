import sys
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_failure(log_file):
    with open(log_file, "r", errors="ignore") as f:
        logs = f.read()

    prompt = f"""
You are an AI DevOps assistant.
Focus ONLY on the last failure.

Answer:
1) Which stage failed?
2) Exact error line
3) Root cause
4) Fix

Logs:
{logs[-4000:]}
"""

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    print("\n[DEVOPS AI AGENT OUTPUT]\n")

    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=60)
        data = r.json()
    except Exception as e:
        print("ERROR: Could not connect to Ollama.")
        print("Fix: Start Ollama and run: ollama run mistral")
        print("Details:", e)
        return

    if "response" in data:
        print(data["response"])
    elif "error" in data:
        print("OLLAMA ERROR:", data["error"])
        print("Fix: Run: ollama run mistral")
    else:
        print("Unexpected Ollama output:")
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    analyze_failure(sys.argv[1])
