import os
from openai import OpenAI
from util import Util
from settings import Settings
from commands import CommandHandler

settings = Settings()
util = Util(settings)
openai_client = OpenAI(api_key=settings.api_key)

def analyze_input(input, history):
    history.append({"role": "user", "content": input})
    response = ask_gpt(history)
    if response:
        history.append({"role": "assistant", "content": response})
        util.write_conversation_history(history)
    return response

def ask_gpt(history):
    sys_message_tokens = util.count_tokens(history[0]["content"])
    user_history_tokens = util.count_tokens(" ".join([entry["content"] for entry in history[1:]]))
    available_tokens = settings.get_max_tokens() - (sys_message_tokens + (len(history) * 4) + 3)

    if user_history_tokens >= available_tokens:
        user_history_text = util.truncate_text("|||".join([entry["content"] for entry in history[1:]]), available_tokens)
        new_history = [{"role": "system", "content": history[0]["content"]}] + [{"role": "user", "content": user_history_text}]
    else:
        new_history = history

    try:
        response = openai_client.chat.completions.create(model=settings.get_model(), messages=new_history, temperature=settings.temperature, stream=settings.stream_response)
        model_type = "smart" if settings.use_smart_model else "fast"

        if settings.stream_response:
            print(f"GPT ({model_type}): ", end='')
            collected_messages = []
            for chunk in response:
                chunk_message = chunk.choices[0].delta.content or ''
                collected_messages.append(chunk_message)
                print(chunk_message, end='')
            print("\n", end='')

            full_reply_content = ''.join([msg for msg in collected_messages])
            return full_reply_content
        else:
            print(f"GPT ({model_type}): " + response)
            return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    command_handler = CommandHandler(util, settings)

    print("Welcome to the GPT CLI!")
    print("Type 'exit' to quit.")

    conversation_history = util.read_conversation_history()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        command, argument, prompt, type = command_handler.process_input(user_input)

        if type == "command":
            output, conversation_history = command_handler.handle_command(command, argument, conversation_history)
            print(output)
            continue

        if type == "pre_prompt" or type == "both_prompt":
            output, conversation_history = command_handler.handle_command(f"pre_{command}" if type == "both_prompt" else command, argument, conversation_history)
            prompt = f"{output}\n{prompt}"

        response = analyze_input(prompt, conversation_history)
        if not response:
            continue

        if type == "post_prompt" or type == "both_prompt":
            output, conversation_history = command_handler.handle_command(f"post_{command}" if type == "both_prompt" else command, argument, conversation_history)
            print(output)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()