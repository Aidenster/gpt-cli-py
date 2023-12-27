import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.api_key = os.environ.get("API_KEY")
        self.fast_model = os.environ.get("FAST_MODEL", "gpt-3.5-turbo")
        self.smart_model = os.environ.get("SMART_MODEL", "gpt-4-0314")
        self.fast_max_tokens = int(os.environ.get("FAST_MAX_TOKENS", "4096"))
        self.smart_max_tokens = int(os.environ.get("SMART_MAX_TOKENS", "8192"))
        self.temperature = float(os.environ.get("TEMPERATURE", "0.3"))
        self.stream_response = os.environ.get("STREAM_RESPONSE", "true").lower() == "true"
        self.conversation_history_file = os.environ.get("CONVERSATION_HISTORY_FILE", "conversation_history.json")
        self.system_message = os.environ.get("SYSTEM_MESSAGE", "You are a helpful assistant.")
        self.use_smart_model = os.environ.get("USE_SMART_MODEL", "false").lower() == "true"
    
    def get_model(self):
        return self.smart_model if self.use_smart_model else self.fast_model
    
    def get_max_tokens(self):
        return self.smart_max_tokens if self.use_smart_model else self.fast_max_tokens