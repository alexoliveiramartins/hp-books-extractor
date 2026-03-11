import json
import ollama

output_path = "./output/spells.jsonl"

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[{"role": "user", "content": prompt}]
)
