import discord
from discord.ext import commands
from discord.ext import tasks

import os
import json

import config


if config.REPLIT_MODE is not False:
    TOKEN = os.getenv("TOKEN")
else:
    TOKEN = config.TOKEN

intents = discord.Intents.all()

bot = discord.Bot(
    owner_id=898360989991448586,
    intents=intents
)