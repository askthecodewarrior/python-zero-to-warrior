# My first message to Claude
import anthropic

client = anthropic.Anthropic()
question = "Give me one Python tip in one sentence."
response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=[{"role": "user", "content": question}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
