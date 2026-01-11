# Discord Bots

A collection of Discord bots for community management and engagement.

## 🤖 Bots

### Bison Bot

A feature-rich Discord bot designed for the PsyBison community with automated member management, social media tracking, and daily content delivery.

#### Features

- **Welcome System**: Automatically sends personalized welcome messages to new members
- **Daily Song**: Posts a random song daily from a curated playlist
- **Member Counter**: Real-time member count display in a voice channel
- **Social Media Integration**: Track and monitor social media feeds (via socials.py extension)
- **Issue Tracking**: Manage community issues and feedback (via issues.py extension)

#### Commands

- `/hello` - Get a friendly greeting from the bot

## 🚀 Setup

### Prerequisites

- Python 3.8 or higher
- Discord Bot Token
- Discord Server with appropriate permissions

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Seekers747/discordbots.git
cd discordbots/bison
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the `bison` directory:
```env
DISCORD_TOKEN=your_discord_token_here
```

4. Configure your settings in `main.py`:
   - Set your `GUILD_ID`
   - Set your channel IDs for daily songs and member counter
   - Set your role IDs as needed

5. Prepare your data files:
   - `songs.json` - List of songs for daily song feature
   - `socials.json` - Social media tracking configuration

### Running the Bot

```bash
cd bison
python main.py
```

## 📁 Project Structure

```
discordbots/
└── bison/
    ├── main.py              # Main bot file with core functionality
    ├── socials.py           # Social media tracking extension
    ├── issues.py            # Issue tracking extension
    ├── feedtracker.py       # Feed tracking extension (disabled)
    ├── requirements.txt     # Python dependencies
    ├── songs.json           # Song database for daily posts
    ├── socials.json         # Social media configuration
    ├── youtube_tracked.json # YouTube tracking data
    └── .gitignore          # Git ignore rules
```

## 🔧 Configuration

### Environment Variables

- `DISCORD_TOKEN` - Your Discord bot token (required)

### Bot Settings

Edit `main.py` to configure:
- Guild/Server ID
- Channel IDs for features
- Role IDs for member counting
- Task intervals (daily song, member count updates)

## 📝 Dependencies

- `discord.py` - Discord API wrapper
- `python-dotenv` - Environment variable management

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.

## 💡 Future Features

- RSS feed tracking (feedtracker.py currently disabled)
- Additional community engagement commands
- Enhanced social media monitoring

---

Made with ❤️ for the PsyBison community