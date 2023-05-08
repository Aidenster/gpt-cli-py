import re, os

class CommandHandler:
    def __init__(self, util):
        self.util = util
        self.pre_prompt_commands = ["read_file"]
        self.post_prompt_commands = ["write_file"]
        self.both_prompt_commands = ["modify_file"]

    def process_input(self, user_input):
        command_pattern = re.compile(r'{(.*?)}')
        command_match = command_pattern.match(user_input)
        if command_match:
            command = command_match.group(1).strip().lower()
            type = self.get_command_type(command)
            argument = None
            user_input = command_pattern.sub("", user_input).strip()
            if ":" in command:
                command, argument = command.split(":", maxsplit=1)
                type = self.get_command_type(command)
                argument = argument.strip()
            return command, argument, user_input, type
        return None, None, user_input, None
    
    def handle_command(self, command, argument, conversation_history):
        message = ""

        if command in ["reset_history", "clear_history", "reset_conversation", "clear_conversation", "reset", "clear"]:
            conversation_history = [{"role": "system", "content": self.util.system_message}]
            self.util.write_conversation_history(conversation_history)
            message = "Conversation history reset."
            os.system('cls' if os.name == 'nt' else 'clear')

        elif command == "read_file" or command == "pre_modify_file":
            file_content = self.util.read_file(argument)
            if not file_content:
                message = "File not found or empty."
            else:
                message = f"'{argument}' Contents:\n{file_content}"

        elif command == "write_file" or command == "post_modify_file":
            success = self.util.write_file(argument, conversation_history[-1]["content"])
            if success:
                message = f"File '{argument}' has been written successfully."
            else:
                message = f"Failed to write file '{argument}'."

        elif command == "count_tokens":
            file_content = self.util.read_file(argument)
            if not file_content:
                message = "File not found or empty."
            else:
                token_count = self.util.count_tokens(file_content)
                message += f"Token Count: {token_count}"

        else:
            message = "Unknown command."

        return message, conversation_history
    
    def get_command_type(self, command):
        if command in self.pre_prompt_commands:
            return "pre_prompt"
        elif command in self.post_prompt_commands:
            return "post_prompt"
        elif command in self.both_prompt_commands:
            return "both_prompt"
        elif command:
            return "command"
        else:
            return None
