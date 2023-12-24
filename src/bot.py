import discord, os, logging
from discord.ext import commands
from discord import Intents, app_commands
logger = logging.getLogger("main")

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(";", help_command=None,intents=Intents.default())