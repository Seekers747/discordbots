from discord import app_commands, Interaction
from discord.ext import commands
from github import Github # pyright: ignore[reportMissingImports]
import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]

# Replace 'your_github_token' and 'your_repo_name' with actual values
load_dotenv()
github = Github(os.getenv('GITHUB_TOKEN'))
repo = github.get_repo(os.getenv('GITHUB_REPO'))

class Issues(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="bot_issue", description="Report a bot issue to the developer")
    async def report(self, interaction: Interaction, title: str, description: str):
        try:
            title = "Bot name: bison | " + title
            issue = repo.create_issue(title=title, body=description)
            await interaction.response.send_message(f"Issue created: {issue.html_url}")
        except Exception as e:
            await interaction.response.send_message(f"Failed to create issue: {e}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Issues(bot))
