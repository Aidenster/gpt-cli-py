# GPT-CLI

A command line interface (CLI) for interacting with OpenAI GPT models. This project allows users to communicate with GPT models using text input and receive generated responses. The CLI provides various settings and options for customizing the behavior of the model and includes a command handler for executing various commands and prompts before and after generating responses from the GPT model.

## Features

- Interact with OpenAI GPT models using a command line interface.
- Customize model settings such as temperature and maximum tokens.
- Execute various commands for reading and writing files, counting tokens, and modifying files.
- Save and load conversation history.
- Stream responses from the GPT model.

## Usage

1. Run the GPT-CLI script:

```
python gpt-cli.py
```

2. Interact with the GPT model by typing your input and pressing Enter.

3. To execute a command, type the command in curly braces `{}` followed by the command name and optional arguments. For example:

```
{read_file:example.txt}
```

4. To exit the CLI, type `exit` and press Enter.

## Commands

The following commands are supported:

- `reset_history`, `clear_history`, `reset_conversation`, `clear_conversation`, `reset`, `clear`: Reset the conversation history.
- `read_file`: Read the contents of a file.
- `write_file`: Write the last response from the GPT model to a file.
- `count_tokens`: Count the number of tokens in a file.
- `modify_file`: Modify a file's content using the GPT model.
- `smart`: Switch to using GPT-4.
- `fast`: Switch to using GPT-3.5.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue to report bugs or suggest improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.