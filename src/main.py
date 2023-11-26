import os

import discord

"""
Quick example of creating a basic bot
From: Discord.py quickstart https://discordpy.readthedocs.io/en/stable/quickstart.html
"""

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('BOT_TOKEN'))