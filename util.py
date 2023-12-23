import os, json, tiktoken

class Util:
    def __init__(self, settings):
        self.settings = settings

    def read_conversation_history(self):
        if os.path.exists(self.settings.conversation_history_file):
            with open(self.settings.conversation_history_file, "r") as f:
                return json.load(f) 
        return [{"role": "system", "content": self.settings.system_message}]

    def write_conversation_history(self, conversation_history):
        with open(self.settings.conversation_history_file, "w") as outfile:
            json.dump(conversation_history, outfile, indent=2)

    def count_tokens(self, text):
        encoding = tiktoken.encoding_for_model(self.settings.get_model())
        return len(encoding.encode(text))

    def truncate_text(self, text, max_tokens):
        encoding = tiktoken.encoding_for_model(self.settings.get_model())
        messages = text.split("|||")
        total_tokens = 0
        truncated_messages = []

        for message in reversed(messages):
            message_tokens = encoding.encode(message)
            if total_tokens + len(message_tokens) <= max_tokens:
                truncated_messages.insert(0, message)
                total_tokens += len(message_tokens)
            else:
                break

        return " ".join(truncated_messages)

    def read_file(self, filepath):
        try:
            with open(filepath, "r", encoding='utf8') as f:
                return f.read()
        except Exception as e:
            print(f"An error occurred while reading '{filepath}': {str(e)}")
            return None

    def write_file(self, filepath, text):
        try:
            with open(filepath, "w") as file:
                file.write(text)
                return True
        except Exception as e:
            print(f"An error occurred while writing '{filepath}': {str(e)}")
            return False
