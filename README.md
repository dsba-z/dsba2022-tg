# Workshop 21. Telegram bots

One of the ways to provide interface for the project is to make a Telegram bot. Here we consider some examples to get you started.

## Introduction

The most common ways of making Telegram bots in Python is to use the module [python-telegram-bot](https://python-telegram-bot.org). 

There are two main versions of it right now: the stable one (v13) and the pre-release one (v20). We'll use the newer pre-release one.

Install the module (to a virtual environment) with

```shell
pip install python-telegram-bot --pre
```

## Token

Before making features for bots, let's run an example bot from https://python-telegram-bot.org

To run any bot you need to use a token - a special key string that tells Telegram that you're the owner of this bot.

To get a token, send a message https://t.me/botfather and follow instructions.

Copy the code from the link above, run it and send a message to your bot.

## Examples

python-telegram-bot comes with many great examples for basic features:

https://docs.python-telegram-bot.org/en/v20.0a5/examples.html

Let's modify the current greeting bot and try some of the examples from that page.

# Practice

## Live example

I'll show how to build a weather bot using <https://openweathermap.org> API.

The main steps are:

1. Make a new command.
2. Get the text from the user's message.
3. Make a request using the text.
4. Return the response to the user.

## Safety

When building bots and working with APIs, one of important things to consider is the safety of your API keys and tokens.

Usually such keys are stored as **environment variables**.

In Python you can use the following code to read such variables:

```python
    my_token = os.getenv("TOKEN")
```

It gets the string stored in the variable `TOKEN` without actually showing this string in the code. This way you can share the code of your bot without sharing access to your bot.

### Writing environment variables

Environment variables are written in different ways depending on the system that runs your code. For example, GitHub and some other hosting services on the internet provide UI pages where you can set variables.

On Mac/Linux you can run `export TOKEN=token_value1234secretcode` before you run your applications. On Windows, `set TOKEN=token_value1234secretcode` should work.

For example,

```python
export TOKEN=token_value1234secretcode
python my_bot.py
```

This way `my_bot.py` will see the variable `TOKEN` in its `os.getenv()` call.

