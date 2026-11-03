# One way to do the your-turn: Bolt, a cheerful robot
import os
import anthropic

MODEL = "claude-haiku-5-5"
SYSTEM = (
    "You are Bolt, a cheerful robot who loves helping "
    "people learn Python. Answer in one or two short "
    "sentences, in plain text with no emoji."
)


def get_reply(client, messages):
    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        system=SYSTEM,
        messages=messages,
    )
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
    print("Chat with Bolt (type quit to stop)")
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
        print("Bolt:", reply)


if __name__ == "__main__":
    main()
