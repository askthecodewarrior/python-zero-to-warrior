# Lesson 54: Build an AI Chatbot in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners. This project shows how to code AI in
Python: your program talks to Claude, Anthropic's AI model, through the Claude API, and you build a chatbot with a
personality and a memory.
Video: https://youtu.be/c59iR2g0Z_8 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

**The Claude API is pay-as-you-go.** You need your own API key from the Claude Console
([platform.claude.com](https://platform.claude.com/)): add credits on the billing page, then create a key on the API
keys page. Every request uses a little of your credits, priced per token (a small piece of text). The model in these
files is `claude-haiku-5-5`, Claude Haiku 5.5, the fastest and cheapest current Claude model; on the day the video
was made it cost $0.10 per million tokens in and $0.50 per million out, so a short chat costs a tiny fraction of a
cent. Prices change: [the pricing page](https://platform.claude.com/docs/en/about-claude/pricing). For harder work you
can put a bigger model's name in `MODEL`, like `claude-opus-5-5`, and it costs more per token.

**Treat your key like a password.** Never put it in your code, never share it, never commit it to GitHub.

## Before you start
1. Install the anthropic package in a virtual environment (lesson 48), in your python-course folder:
   ```
   python3 -m venv .venv               # Mac
   source .venv/bin/activate
   pip install anthropic

   python -m venv .venv                # Windows
   .venv\Scripts\activate
   pip install anthropic
   ```
   If you set the project up with uv, it's `uv add anthropic`. The prompt starts with `(.venv)` while the venv is on.
2. Put your key in the `ANTHROPIC_API_KEY` environment variable, in the same terminal you run the programs from:
   ```
   export ANTHROPIC_API_KEY="your-key-here"      # Mac (Terminal): no spaces around the =
   $env:ANTHROPIC_API_KEY="your-key-here"        # Windows (PowerShell)
   ```
   Put your real key between the quotes. It lasts until you close that terminal, so in a new terminal you set it
   again. The anthropic package reads `ANTHROPIC_API_KEY` on its own.

## What's in this lesson
- **`first_chat.py`: one message.** `anthropic.Anthropic()` makes the client (it finds your key in the environment
  variable). `client.messages.create()` sends the request with a `model`, `max_tokens` (the most the reply may use;
  the model's thinking counts too) and `messages`, a list of dictionaries where `role` says who's talking (`user` is
  you). The reply comes back as a list of content blocks, and the words are in the block whose `type` is `"text"`,
  so the loop looks for that block instead of taking the first one (a reply can start with a thinking block).
  Run it twice and you get two different replies.
- **`chatbot.py`: the chatbot.**
  - `MODEL` and `SYSTEM` are constants. `SYSTEM` is the system prompt, the instructions Claude reads before the
    conversation: here a personality (Captain Byte, a friendly pirate) and rules (short answers, plain text). Python
    joins strings that sit next to each other inside the parentheses into one string, so the first two end with a space.
  - `get_reply(client, messages)` sends the whole list with the system prompt and returns the text (or `""` if a reply
    has no text block, which can happen when Claude turns down a request).
  - `main()` checks `os.environ.get("ANTHROPIC_API_KEY")` first, then loops (lesson 16): `quit` ends the chat cleanly.
    **The API doesn't remember anything between requests**, so every message goes into `messages` with `append()`:
    yours as `"user"`, Claude's as `"assistant"`, and each request sends all of them. That's the memory.
  - `except anthropic.AuthenticationError` (a wrong key) comes before `except anthropic.APIError` (every other error
    the SDK raises, like no internet), because AuthenticationError is a kind of APIError (lesson 50 had the same
    order). After an error, `messages.pop()` takes your last message back off the list, since it never got an answer.
- **The common mistakes:**
  - Leaving the placeholder (or a typo) in your key: the API answers 401, and the chatbot prints
    `That API key didn't work.` Set the variable again with your real key.
  - A `temperature=0.7` line from older examples: this version of the package doesn't take it, so Python stops with
    `TypeError: Messages.create() got an unexpected keyword argument 'temperature'` before anything is sent. Take the
    line out.

## Files
- `first_chat.py`, `chatbot.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs. `solution.py`: one way to solve it (Bolt, a cheerful robot).
- `predict.py`, `tokens.py`, `reset.py`: practice problems 1, 2 and 3 (`tokens.py` and `reset.py` are one answer
  each: try them yourself first).

## Run it
```
python3 chatbot.py      # Mac
python chatbot.py       # Windows
```
Turn the venv on and set your key first. The same goes for every other file. Your replies are going to be different
from the video's, because the model writes a new reply every time.

## Your turn
Give the bot a personality of your own: change the three strings in `SYSTEM` (a robot, a wizard, a coach), then put
its name in the two prints (lines 32 and 49) and chat with it. `solution.py` is Bolt; when it was asked
"Hi! Who are you?" it said something like: `Bolt: I'm Bolt, a cheerful robot here to help you learn Python. What
would you like to explore first?`

## Practice
1. Predict, then run `predict.py` (no key or internet needed):
   ```python
   messages = []
   for text in ["Hi!", "What's 2 + 2?"]:
       messages.append({"role": "user", "content": text})
       reply = "(a reply to " + text + ")"
       messages.append({"role": "assistant", "content": reply})

   print(len(messages))
   print(messages[2]["content"])
   print(messages[-1]["role"])
   ```
   (`4`, `What's 2 + 2?` and `assistant`: two messages go in each time around the loop.)
2. Write `tokens.py`: make `get_reply()` print how many tokens each request used, with `response.usage.input_tokens`
   and `response.usage.output_tokens`, before it returns the text. A real run printed `(tokens: 62 in, 58 out)` for
   "Hi!" (yours will be different).
3. Write `reset.py`: if you type `reset`, clear the history with `messages.clear()`, print `Starting over.` and go
   back to the top of the loop with `continue`. Tell it your name, type `reset`, then ask what your name is: it won't
   know anymore.

More ideas: save the conversation to a JSON file when you quit (lesson 33), or let the user pick the personality when
the program starts with `input()`.
