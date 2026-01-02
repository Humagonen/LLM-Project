import requests
import time
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_model(model_name, prompt):
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }

    start_time = time.time()
    response = requests.post(OLLAMA_URL, json=payload)
    elapsed = time.time() - start_time

    response.raise_for_status()
    result = response.json()

    return {
        "model": model_name,
        "response": result["response"],
        "time_seconds": round(elapsed, 2)
    }


if __name__ == "__main__":
    prompt = "Summarise the role of self-attention in transformers in 3 sentences."

    for model in ["qwen2.5:3b", "phi3:mini"]:
        output = run_model(model, prompt)
        print(f"\n--- {output['model']} ---")
        print(f"Time: {output['time_seconds']}s")
        print(output["response"])
