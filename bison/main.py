import discord, logging, os, json, random
from discord.ext import commands, tasks # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]

# Load tokens
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Initialize bot
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/', intents=intents)

    async def setup_hook(self):
        GUILD_ID = 1318926273829142550
        guild = discord.Object(id=GUILD_ID)

        await self.load_extension('socials')
        await self.load_extension('issues')
        # feedtracker.py is currently disabled
        # await self.load_extension('feedtracker')

        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

bot = MyBot()

# Startup event
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')
    await run_loops()

async def run_loops():
    if not daily_song.is_running():
        daily_song.start()
    if not update_member_count.is_running():
        update_member_count.start()

# say hello command
@bot.tree.command(name="hello", description="Responds with a greeting")
async def hello_slash(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

# Welcome new members
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

@tasks.loop(hours=24)
async def daily_song():
    print("Sending daily song...")
    await bot.wait_until_ready()
    YOUR_CHANNEL_ID_HERE = 1318926274550435854

    channel = bot.get_channel(YOUR_CHANNEL_ID_HERE)
    if not channel:
        print("Channel not found!")
        return

    with open('songs.json', 'r') as f:
        songs = json.load(f)

    song = random.choice(songs["songs"])

    await channel.send(
        f"🎵 **Song of the Day** 🎵\n"
        f"**Title:** {song['title']}\n"
        f"**URL:** {song['url']}"
    )
    print("Daily song sent.")

@tasks.loop(seconds=60)
async def update_member_count():
    print("Updating member count...")
    await bot.wait_until_ready()

    GUILD_ID = 1318926273829142550
    VC_CHANNEL_ID = 1459895164263731244
    ROLE_ID = 1318945370742722700

    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        return

    channel = guild.get_channel(VC_CHANNEL_ID)
    if channel is None:
        return
    
    role = guild.get_role(ROLE_ID)
    if role is None:
        return

    member_count = len(role.members)

    # Update the VC name
    try:
        await channel.edit(name=f"Members: {member_count}")
        print(f"Updated member count to: {member_count}")
    except discord.Forbidden:
        print("Missing permissions to edit the VC!")
    except discord.HTTPException as e:
        print(f"Failed to edit VC: {e}")

# Run bot
bot.run(token, log_handler=handler, log_level=logging.DEBUG)