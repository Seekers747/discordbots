# Discord Bots Collection

A growing collection of custom Discord bots for various communities and purposes. Each bot is designed to be modular, extensible, and easy to customize for different use cases.

## 🤖 Current Bots

### Bison Bot
A community management bot built for the PsyBison Discord server featuring automated member engagement, social media tracking, and content delivery systems.

**Core Features:**
- Automated welcome system with custom messaging
- Daily content delivery (songs, posts, etc.)
- Real-time member statistics tracking
- Social media feed monitoring
- Community issue tracking

**Extension System:**
- `socials.py` - Social media integration module
- `issues.py` - Issue tracking and management module
- `feedtracker.py` - RSS/feed tracking (currently disabled, ready for future use)

---

## 🔧 Architecture & Customization

### Modular Design
Each bot uses Discord.py's extension (cog) system, making it easy to add, remove, or modify features without touching the core bot logic.

### Configurable Components

**IDs & Targeting:**
- Guild/Server IDs
- Channel IDs (for daily posts, announcements, etc.)
- Role IDs (for member counting, permissions)
- User IDs (for specific user targeting)

**Task Loops:**
- Interval timing (daily, hourly, by minute)
- Task scheduling and automation
- Background processes

**Data Storage:**
- JSON-based data files for easy modification
- `songs.json` - Content database (easily expandable)
- `socials.json` - Social media configurations
- `youtube_tracked.json` - Tracking data
- Additional data files can be added as needed

**Commands:**
- Slash command system
- Easy to add new commands via Discord.py tree
- Guild-specific or global command deployment

### Extension Points

The bot framework is designed to be extended:
- Add new cogs/extensions for additional features
- Implement new task loops for automated behaviors
- Create custom event handlers
- Expand data models with new JSON schemas

---

## 📁 Project Structure

```
discordbots/
├── bison/                   # Bison community bot
│   ├── main.py             # Core bot + task loops
│   ├── socials.py          # Social media extension
│   ├── issues.py           # Issue tracking extension
│   ├── feedtracker.py      # Feed tracker (disabled)
│   ├── requirements.txt    # Dependencies
│   └── *.json             # Data files
│
└── [future bots]/          # Additional bots to be added
```

Each bot folder contains:
- Main bot file with core functionality
- Extension modules for specific features
- Configuration and data files
- Dependencies list

---

## 🚀 Technical Stack

- **Discord.py** - Discord API wrapper with slash command support
- **python-dotenv** - Environment variable management
- **Task Loops** - Discord.py's built-in scheduled task system
- **JSON Storage** - Simple, readable data persistence

---

## 🎯 Future Expansion

This repository will grow to include:
- Additional community bots for different servers
- New feature modules and extensions
- Enhanced automation capabilities
- Improved data tracking and analytics
- Cross-bot shared utilities

Each bot is built with scalability in mind, allowing features to be easily adapted, reused, or expanded upon.

---

## 📝 Notes

This is a personal project showcasing custom Discord bot development. Each bot is tailored to specific community needs and serves as a reference for modular bot architecture.

---

Made with ❤️ for Discord communities