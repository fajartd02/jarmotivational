import discord
import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("DISCORD_BOT_TOKEN")

# CREATE BOT
custom_intents = discord.Intents(messages=True, guilds=True)
custom_intents.message_content = True
bot = discord.Client(intents=custom_intents)

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count += 1
    print(f"Bot is in {guild_count} guilds.")

@bot.event
async def on_message(message):
    print(message)
    if message.content == "hello":
        id = message.author.id
        await message.channel.send(f"hey dirty bag <@{id}>" )

bot.run(token)