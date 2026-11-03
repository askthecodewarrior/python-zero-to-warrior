# Practice 2: the chatbot, and how many tokens each reply used
import os
import anthropic

MODEL = "claude-haiku-5-5"
SYSTEM = (
    "You are Captain Byte, a friendly pirate who helps "
    "beginners learn Python. Answer in one or two short "
    "sentences, in plain text with no emoji."
)


def get_reply(client, messages):
    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        system=SYSTEM,
        messages=messages,
    )
    usage = response.usage
    print(f"(tokens: {usage.input_tokens} in, {usage.output_tokens} out)")
    for block in response.content:
        if block.type == "text":
            return block.text
    return ""


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY first.")
        return
    client = anthropic.Anthropic()
    messages = []
    print("Chat with Captain Byte (type quit to stop)")
    while True:
        text = input("You: ")
        if text == "quit":
            print("Goodbye!")
            break
        messages.append({"role": "user", "content": text})
        try:
            reply = get_reply(client, messages)
        except anthropic.AuthenticationError:
            print("That API key didn't work.")
            break
        except anthropic.APIError as e:
            print("Error:", e)
            messages.pop()
            continue
        messages.append({"role": "assistant", "content": reply})
        print("Captain Byte:", reply)


if __name__ == "__main__":
    main()
