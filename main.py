import os
import discord
from dotenv import load_dotenv
from src.langchain_wrapper import LangChainGpt
from src.discord_bot import Discord_Bot


if __name__ == '__main__':
    load_dotenv()
    discord_api_key = os.getenv("DISCORD_API_KEY")  # this is for discord bot

    try:
        with open('system_message.txt', 'r') as f:
            system_message = f.read()
    except FileNotFoundError:
        print('File not found')

    langchain_gpt = LangChainGpt(system_message=system_message)

    intents = discord.Intents.default()
    intents.message_content = True

    client = Discord_Bot(intents=intents, chat_gpt=langchain_gpt)
    client.run(discord_api_key)
