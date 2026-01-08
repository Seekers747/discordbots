import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.event
async def on_member_join(member):
    await member.send(f"""
Welcome to the PsyBison Discord community

Hey, and thanks for joining.
You’re now part of the official PsyBison community.

This server is built around my music and content, but it’s also a place to hang out, talk, and connect with others.

What you can do here
Stay up to date with new music and releases
Chat, chill, and socialize
Join discussions, events, and community activities
Share feedback, creativity, and ideas

Make sure to check the rules and explore the channels so you know where everything is.

Most importantly — be yourself and enjoy your time here.
Glad to have you with us.

— PsyBison 
                      """)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)