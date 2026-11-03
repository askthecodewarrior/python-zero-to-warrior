# Your turn: a chatbot with YOUR personality (lesson 54)
import os
import anthropic

MODEL = "claude-haiku-5-5"
# TODO 1: write your own personality in the three strings below
# (keep a space before the closing quote of the first two)
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
    # TODO 2: put your bot's name here and in the last print
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
