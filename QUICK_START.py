#!/usr/bin/env python3
"""
Quick Start Reference for YouTube AI Shorts Generator
"""

def print_quick_start():
    commands = """
╔═══════════════════════════════════════════════════════╗
║   YouTube AI Shorts Generator - Quick Start          ║
╚═══════════════════════════════════════════════════════╝

INSTALLATION (One-time setup)
─────────────────────────────

1. Create directories:
   python setup.py

2. Install dependencies:
   pip install -r requirements.txt

3. Get API keys and add to .env:
   - OpenAI: https://platform.openai.com/api-keys
   - ElevenLabs: https://elevenlabs.io/api
   - Pexels: https://www.pexels.com/api/

4. Add topics to topics/topics.csv


RUNNING THE GENERATOR
─────────────────────

Single command to generate all videos:

   python main.py

This will:
  • Load topics from topics/topics.csv
  • Generate AI scripts
  • Synthesize voice audio
  • Download relevant images
  • Create SRT captions
  • Compose final videos
  • Save to output/ directory

Output videos are in MP4 format (1080x1920 vertical)


CONFIGURATION
──────────────

Edit config.py to customize:

  Video Duration:
    VIDEO_DURATION = 60  # seconds

  Video Quality:
    VIDEO_FPS = 30  # frames per second

  Voice:
    VOICE_STABILITY = 0.5  # 0-1 range
    SPEECH_RATE = 1.0  # speed multiplier

  Script Length:
    MAX_SCRIPT_LENGTH = 500  # characters
    MIN_SCRIPT_LENGTH = 100  # characters


ADDING TOPICS
──────────────

Edit topics/topics.csv:

  topic_id,topic_title,category,difficulty
  1,AI Future,Technology,Medium
  2,Cooking Tips,Food,Easy

Fields:
  • topic_id: Unique number
  • topic_title: Video subject
  • category: Content type
  • difficulty: Easy/Medium/Hard


COMMON COMMANDS
───────────────

Setup project directories:
  python setup.py

Install all dependencies:
  pip install -r requirements.txt

View setup instructions:
  python SETUP_GUIDE.py

Run the full pipeline:
  python main.py

Test individual modules:
  python generate_script.py    # Test script generation
  python generate_voice.py     # Test voice synthesis
  python generate_images.py    # Test image download
  python generate_captions.py  # Test caption generation


TROUBLESHOOTING
────────────────

Issue: ModuleNotFoundError
Fix: pip install -r requirements.txt

Issue: API Key errors
Fix: Check .env file has correct keys

Issue: No videos generated
Fix: Check topics/topics.csv has data

Issue: File not found errors
Fix: Run python setup.py first

Issue: FFmpeg not found
Fix: Install FFmpeg for your OS


PROJECT FILES
──────────────

Core Modules:
  • config.py - Configuration
  • main.py - Main orchestrator
  • generate_script.py - Script creation
  • generate_voice.py - Voice synthesis
  • generate_images.py - Image download
  • generate_captions.py - Caption generation
  • create_video.py - Video composition

Configuration:
  • .env - API keys
  • config.py - Settings
  • topics/topics.csv - Video topics

Setup & Documentation:
  • setup.py - Project initialization
  • requirements.txt - Dependencies
  • README.md - Full documentation
  • SETUP_GUIDE.py - Setup instructions
  • PROJECT_SUMMARY.txt - Overview


DIRECTORY LAYOUT
──────────────────

youtube-ai-shorts/
├── assets/
│   ├── backgrounds/    # Background images
│   └── music/          # Background music
├── audio/              # Generated audio
├── captions/           # Generated captions
├── images/             # Downloaded images
├── output/             # Final videos
├── scripts/            # Custom scripts
├── topics/
│   └── topics.csv      # Topics list
└── [Python files]


PERFORMANCE TIPS
────────────────

• Start with 1 topic to test
• Check output quality before scaling
• Use shorter video durations for faster processing
• Monitor API usage and rate limits
• Run during off-peak hours for faster response times


GETTING HELP
──────────────

For detailed information:
  1. Read README.md
  2. Check SETUP_GUIDE.py
  3. Review config.py for options
  4. Check documentation in each .py file


═════════════════════════════════════════════════════════════

Ready to create amazing AI-generated YouTube Shorts? 

Start here: python setup.py

═════════════════════════════════════════════════════════════
    """
    print(commands)

if __name__ == "__main__":
    print_quick_start()
