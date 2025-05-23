from autogen import ConversableAgent, UserProxyAgent
import os
import agentops

# Set API Keys correctly (once, or set externally in your environment)
os.environ["AGENTOPS_API_KEY"] = "3d7a786f-2620-4534-b948-588ac00262bb"
os.environ["GROQ_API_KEY"] = "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"

# Initialize AgentOps
agentops.init(tags=["autogen-groq-agentops"])

# Use the environment variable correctly here
config_list = [
    {
        "model": "llama-3.3-70b-versatile",
        "api_key": os.environ["GROQ_API_KEY"],   # <== Correct access
        "base_url": "https://api.groq.com/openai/v1",
        "api_type": "openai",
    }
]

llm_config = {
    "config_list": config_list
}

assistant = ConversableAgent("agent", llm_config=llm_config)
user = UserProxyAgent("user", code_execution_config=False)

assistant.initiate_chat(user, message="Simple code to add two numbers in Python")

agentops.end_session("Done")
