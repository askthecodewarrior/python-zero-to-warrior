# Practice 1: predict what this prints, then run it (no key or internet)
messages = []
for text in ["Hi!", "What's 2 + 2?"]:
    messages.append({"role": "user", "content": text})
    reply = "(a reply to " + text + ")"
    messages.append({"role": "assistant", "content": reply})

print(len(messages))
print(messages[2]["content"])
print(messages[-1]["role"])
