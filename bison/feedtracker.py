import json
from discord.ext import commands
from aiohttp import web
import xml.etree.ElementTree as ET

DISCORD_CHANNEL_ID = 1318954070115090492  # Replace with your Discord channel
YOUTUBE_CHANNEL_ID = "UCbAA5EYU0KHZGdKNEYItIHw"  # Your YouTube channel ID
TRACKED_FILE = "youtube_tracked.json"

class YouTubeTracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_video_id = None

        # Load last-seen video ID
        try:
            with open(TRACKED_FILE, "r") as f:
                data = json.load(f)
                self.last_video_id = data.get("youtube")
        except FileNotFoundError:
            self.last_video_id = None

        # Start the webhook server
        self.bot.loop.create_task(self.start_webserver())

    async def start_webserver(self):
        app = web.Application()
        app.router.add_post("/youtube-webhook", self.youtube_webhook)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", 8080)  # Port 8080, change if needed
        await site.start()
        print("YouTube webhook server running on port 8080")

    async def youtube_webhook(self, request):
        # YouTube PubSubHubbub sends XML data
        raw_body = await request.text()
        try:
            root = ET.fromstring(raw_body)
            # XML namespace for YouTube feed
            ns = {"yt": "http://www.youtube.com/xml/schemas/2015", "atom": "http://www.w3.org/2005/Atom"}
            entry = root.find("atom:entry", ns)
            if entry is None:
                return web.Response(text="No entry", status=400)

            video_id = entry.find("yt:videoId", ns).text
        except Exception as e:
            print("Failed to parse XML:", e)
            return web.Response(text="Error parsing XML", status=500)

        # First-run safety: ignore old videos
        if video_id != self.last_video_id:
            channel = self.bot.get_channel(DISCORD_CHANNEL_ID)
            if channel:
                await channel.send(f"📹 **New YouTube Video!**\nhttps://youtu.be/{video_id}")
            self.last_video_id = video_id

            # Save last-seen video ID
            with open(TRACKED_FILE, "w") as f:
                json.dump({"youtube": self.last_video_id}, f, indent=4)

        return web.Response(text="OK")


async def setup(bot):
    await bot.add_cog(YouTubeTracker(bot))