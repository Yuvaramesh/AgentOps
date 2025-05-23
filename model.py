import requests

api_key = "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"  # <--- Your actual API key here

headers = {
    "Authorization": f"Bearer {api_key}",
}

response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)

if response.status_code == 200:
    models = response.json()
    print("Available Groq Models:")
    for model in models.get("data", []):
        print(model.get("id"))
else:
    print(f"Error fetching models: {response.status_code} - {response.text}")
