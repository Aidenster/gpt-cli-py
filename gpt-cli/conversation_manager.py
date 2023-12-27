import json

class ConversationManager:
    def __init__(self):
        self.conversations = {}

    def start_conversation(self, conversation_id):
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []

    def add_message(self, conversation_id, message):
        if conversation_id in self.conversations:
            self.conversations[conversation_id].append(message)

    def get_conversation(self, conversation_id):
        return self.conversations.get(conversation_id, [])

    def end_conversation(self, conversation_id):
        if conversation_id in self.conversations:
            del self.conversations[conversation_id]
    
    def load_conversation(self, filename):
        """
        Load a conversation from a JSON file.

        Args:
            filename (str): The name of the file to load the conversation from.

        Returns:
            list: The loaded conversation as a list of dictionaries.
        """
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return []

    def save_conversation(self, filename, conversation):
        """
        Save a conversation to a JSON file.

        Args:
            filename (str): The name of the file to save the conversation to.
            conversation (list): The conversation to save as a list of dictionaries.
        """
        with open(filename, "w") as f:
            json.dump(conversation, f, indent=2)