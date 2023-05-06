import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.api_key = os.environ.get("API_KEY")
        self.model = os.environ.get("MODEL", "gpt-3.5-turbo")
        self.temperature = float(os.environ.get("TEMPERATURE", "0.3"))
        self.max_tokens = int(os.environ.get("MAX_TOKENS","4096"))
        self.stream_response = os.environ.get("STREAM_RESPONSE", "true").lower() == "true"
        self.conversation_history_file = os.environ.get("CONVERSATION_HISTORY_FILE", "conversation_history.json")
        self.system_message = os.environ.get("SYSTEM_MESSAGE", "You are a helpful assistant.")
