import os

from dotenv import load_dotenv

from src.discordbot import DiscordBot
from src.langchain_wrapper import LangChainGpt

if __name__ == '__main__':
    load_dotenv()
    discord_api_key = os.getenv("DISCORD_API_KEY")  # this is for discord bot

    try:
        with open('system_message.txt', 'r') as f:
            system_message = f.read()
    except FileNotFoundError:
        print('File not found')

    langchain_gpt = LangChainGpt(system_message=system_message)

    client = DiscordBot(chat_gpt=langchain_gpt)
    client.run(discord_api_key)
