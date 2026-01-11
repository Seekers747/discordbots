# socials.py
import json
import discord
from discord import app_commands
from discord.ext import commands # pyright: ignore[reportMissingImports]

# Load socials data
with open('socials.json', 'r') as f:
    socials_data = json.load(f)
socials_data_keys = list(socials_data.keys())

class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="socials", description="Get social links")
    @app_commands.choices(platform=[
        app_commands.Choice(name=key.capitalize(), value=key) for key in socials_data_keys
    ])
    async def socials(
        self,
        interaction: discord.Interaction,
        platform: app_commands.Choice[str]
    ):
        url = socials_data.get(platform.value)

        if url:
            await interaction.response.send_message(f"My {platform.name} link: {url}")
        else:
            await interaction.response.send_message("Sorry, I don't have that social media link.")

async def setup(bot):
    await bot.add_cog(Socials(bot))