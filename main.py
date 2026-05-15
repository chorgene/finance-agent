import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

MODEL = "claude-sonnet-4-6"

messages = []


def add_message(message, role):
    messages.append({"role": role, "content": message})


def getResponse(message):
    add_message(message, "user")
    message = client.messages.create(model=MODEL, max_tokens=1000, messages=messages)

    text = ""
    for block in message.content:
        if block.type == "text":
            text = block.text
            add_message(text, "assistant")
            return text


def getStreamResponse(message):
    add_message(message, "user")

    full_message = ""

    with client.messages.stream(
        model=MODEL, max_tokens=1000, messages=messages
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_message += text

    add_message(full_message, "assistant")


while True:
    print("You: ", end="")
    user_input = input("")
    print("Assistant: ", end="")
    getStreamResponse(user_input)
    print()
