# 🤖 AgentOps Groq Conversable Agent

A Python project demonstrating how to create a conversational AI agent using [AgentOps](https://app.agentops.ai/), [Autogen](https://github.com/autogenai/autogen), and Groq’s LLM API. The agent interacts via chat and leverages the Groq `llama3-8b-8192` model for generating responses.

---

## ✨ Features

* Initialize and configure AgentOps session with Groq API keys.
* Use `ConversableAgent` and `UserProxyAgent` from Autogen for chat simulation.
* Query the Groq LLM endpoint with conversational prompts.
* Clean session management with AgentOps.
* Easily extensible to other Groq models and AgentOps configurations.

---

## 🛠️ Requirements

* Python 3.8 or above
* See [`requirements.txt`](./requirements.txt) for Python dependencies

---

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/agentops-groq-agent.git
   cd agentops-groq-agent
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your environment variables for API keys:

   ```bash
   export AGENTOPS_API_KEY="your_agentops_api_key_here"
   export GROQ_API_KEY="your_groq_api_key_here"
   ```

   On Windows (PowerShell):

   ```powershell
   setx AGENTOPS_API_KEY "your_agentops_api_key_here"
   setx GROQ_API_KEY "your_groq_api_key_here"
   ```
---

## 💬 Usage

Run the main script to start a chat interaction where the agent responds to a prompt:

```bash
python agentsops.py
```

The script initiates a conversation with the prompt:

![image](https://github.com/user-attachments/assets/387ef573-1108-476b-b627-a70adbb310ae)

You will see the agent’s response printed in the console.

![image](https://github.com/user-attachments/assets/4286a74b-7c11-4e02-ade0-a417d81aceed)

---

## 📂 Code Overview

* **agentsops.py**: Main script initializing AgentOps, setting up Groq API integration, and creating conversational agents.
* Uses Autogen’s `ConversableAgent` and `UserProxyAgent` classes for simulating the conversation.
* Utilizes Groq LLM models via OpenAI-compatible API endpoints.

---

## 🧩 Available Models

Some Groq models you can experiment with (ensure your API key has access):

* `llama-3.3-70b-versatile` (recommended for chat completion)
* `llama3-8b-8192`
* `gemma2-9b-it`
* `playai-tts`
* `meta-llama/llama-guard-4-12b`
* `mistral-saba-24b`
* `whisper-large-v3-turbo`
* And more (see Groq API for full list)

---

## 🛠️ Troubleshooting

* **401 Invalid API Key**: Check your API keys in environment variables and ensure they are correct.
* **Model decommissioned**: Some models may be deprecated. Use the recommended models listed above.
* Ensure your network can reach `https://api.groq.com`.

---


## 🧑‍💻 Author

**Yuva Sri Ramesh**
[Portfolio](https://yuva-sri-ramesh-portfolio.vercel.app) | [LinkedIn](https://www.linkedin.com/in/yuva-sri-ramesh/) | [GitHub](https://github.com/Yuva-Sri-Ramesh)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).


