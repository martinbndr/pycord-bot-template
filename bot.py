import discord
from discord.ext import commands
from discord.commands import slash_command, Option, OptionChoice
from config import *

intents = discord.Intents.all()
intents.typing = False

client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{client.user} (ID: {client.user.id}) is ready!")

client.run(token)