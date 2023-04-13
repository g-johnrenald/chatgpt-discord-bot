import discord
from src.command_enums import Command
from src.langchain_wrapper import LangChainGpt


class Discord_Bot(discord.Client):
    def __init__(self, chat_gpt: LangChainGpt, intents):
        super().__init__(intents=intents)
        self.chat_gpt = chat_gpt

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.application_command:
            given_command = interaction.data['name']
            if given_command == Command.CHAT.value:
                await interaction.response.defer()
                message = interaction.data['options'][0]['value']
                user = interaction.user
                print(f'\n\n{user.name}: {message}')
                print("LangChain: ")
                answer = self.chat_gpt.predict(f'"ユーザー名："{user} {message}')
                response = f'{user.name}: {message} \n\n MSBN: {answer}'
                await interaction.followup.send(response)
