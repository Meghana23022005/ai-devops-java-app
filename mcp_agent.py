import sys
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_failure(log_file):
    with open(log_file, "r", errors="ignore") as f:
        lines = f.readlines()

    # Send only last 200 lines (faster + stable)
    log_excerpt = "".join(lines[-200:])

    prompt = f"""
You are a senior DevOps engineer.

Analyze ONLY the failure from the last 200 lines.

Strictly answer in this format:

Stage Failed:
Error Line:
Root Cause:
Fix:

Be precise. Do not guess. Do not add extra explanation.

Logs:
{log_excerpt}
"""

    payload = {
        "model": "phi3", 
        "prompt": prompt,
        "stream": False
    }

    print("\n[DEVOPS AI AGENT OUTPUT]\n")

    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=600)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print("ERROR: Could not connect to Ollama.")
        print("Fix: Ensure Ollama is running and model is loaded.")
        print("Run:")
        print("  ollama pull phi3")
        print("  ollama run phi3")
        print("Details:", e)
        return

    if "response" in data:
        print(data["response"])
    elif "error" in data:
        print("OLLAMA ERROR:", data["error"])
    else:
        print("Unexpected Ollama output:")
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mcp_agent.py <logfile>")
        sys.exit(1)

    analyze_failure(sys.argv[1])
