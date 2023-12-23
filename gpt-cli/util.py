import os, json, tiktoken

class Util:
    """
    Utility class for various helper functions.
    """

    def __init__(self, settings):
        self.settings = settings


    def read_conversation_history(self):
        """
        Read the conversation history from a file.

        Returns:
            list: The conversation history as a list of dictionaries.
        """
        if os.path.exists(self.settings.conversation_history_file):
            with open(self.settings.conversation_history_file, "r") as f:
                return json.load(f) 
        return [{"role": "system", "content": self.settings.system_message}]


    def write_conversation_history(self, conversation_history):
        """
        Write the conversation history to a file.

        Args:
            conversation_history (list): The conversation history as a list of dictionaries.
        """
        with open(self.settings.conversation_history_file, "w") as outfile:
            json.dump(conversation_history, outfile, indent=2)


    def count_tokens(self, text):
        """
        Count the number of tokens in the given text.

        Args:
            text (str): The text to count tokens for.

        Returns:
            int: The number of tokens in the text.
        """
        encoding = tiktoken.encoding_for_model(self.settings.get_model())
        return len(encoding.encode(text))


    def truncate_text(self, text, max_tokens):
        """
        Truncate the text to a maximum number of tokens.

        Args:
            text (str): The text to truncate.
            max_tokens (int): The maximum number of tokens.

        Returns:
            str: The truncated text.
        """
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
        """
        Read the contents of a file.

        Args:
            filepath (str): The path to the file.

        Returns:
            str: The contents of the file.
        """
        try:
            with open(filepath, "r", encoding='utf8') as f:
                return f.read()
        except Exception as e:
            print(f"An error occurred while reading '{filepath}': {str(e)}")
            return None


    def write_file(self, filepath, text):
        """
        Write the given text to a file.

        Args:
            filepath (str): The path to the file.
            text (str): The text to write.

        Returns:
            bool: True if the write operation was successful, False otherwise.
        """
        try:
            with open(filepath, "w") as file:
                file.write(text)
                return True
        except Exception as e:
            print(f"An error occurred while writing '{filepath}': {str(e)}")
            return False
