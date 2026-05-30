"""
YOUTUBE AI SHORTS GENERATOR
Complete Project Structure & Setup Guide
"""

PROJECT_TREE = """
youtube-ai-shorts/
│
├── 📁 DOCUMENTATION
│   ├── START_HERE.txt .................. 👈 Start here!
│   ├── README.md ....................... Full documentation
│   ├── PROJECT_SUMMARY.txt ............. Overview
│   ├── SETUP_GUIDE.py .................. Interactive setup
│   ├── QUICK_START.py .................. Quick reference
│   └── INDEX.py ........................ Project structure
│
├── 📁 CORE MODULES
│   ├── main.py ......................... Main orchestrator
│   ├── config.py ....................... Configuration
│   └── setup.py ........................ Project initialization
│
├── 📁 GENERATION MODULES
│   ├── generate_script.py .............. Script generation (GPT)
│   ├── generate_voice.py ............... Voice synthesis (ElevenLabs)
│   ├── generate_images.py .............. Image download (Pexels)
│   ├── generate_captions.py ............ Caption generation
│   └── create_video.py ................. Video composition
│
├── 📁 CONFIGURATION
│   ├── .env ............................ API keys & secrets
│   ├── .gitignore ...................... Git configuration
│   ├── requirements.txt ................ Python dependencies
│   └── __init__.py ..................... Package init
│
└── 📁 DIRECTORIES TO CREATE (run setup.py)
    ├── assets/
    │   ├── backgrounds/ ................ Background images
    │   └── music/ ....................... Background music
    ├── audio/ ........................... Generated audio files
    ├── captions/ ........................ Generated subtitles
    ├── images/ .......................... Downloaded images
    ├── output/ .......................... Final MP4 videos
    ├── scripts/ ......................... Custom utilities
    └── topics/
        └── topics.csv ................... Video topics list
"""

INSTALLATION_STEPS = """
╔═══════════════════════════════════════════════════════════════╗
║            INSTALLATION & SETUP STEPS                         ║
╚═══════════════════════════════════════════════════════════════╝

STEP 1: PROJECT SETUP
─────────────────────

Open command prompt in project directory and run:

    python setup.py

This creates all required directories:
  • assets/ (backgrounds, music)
  • audio/
  • captions/
  • images/
  • output/
  • scripts/
  • topics/


STEP 2: INSTALL DEPENDENCIES
─────────────────────────────

Install required Python packages:

    pip install -r requirements.txt

Installs:
  • python-dotenv
  • openai
  • elevenlabs
  • moviepy
  • opencv-python
  • Pillow
  • requests
  • numpy
  • pandas


STEP 3: CONFIGURE API KEYS
──────────────────────────

Edit the .env file with your API keys:

    OPENAI_API_KEY=sk-...
    ELEVENLABS_API_KEY=...
    PEXELS_API_KEY=...

Get API keys from:
  1. OpenAI: https://platform.openai.com/api-keys
  2. ElevenLabs: https://elevenlabs.io/
  3. Pexels: https://www.pexels.com/api/


STEP 4: ADD VIDEO TOPICS
────────────────────────

Edit topics/topics.csv:

    topic_id,topic_title,category,difficulty
    1,10 AI Facts,Technology,Medium
    2,Cooking Tips,Food,Easy
    3,Study Hacks,Education,Medium

Add as many topics as you want to generate.


STEP 5: GENERATE VIDEOS
───────────────────────

Run the main script:

    python main.py

This will:
  1. Load topics from topics/topics.csv
  2. For each topic:
     • Generate AI script
     • Create voice audio
     • Download images
     • Generate captions
     • Create MP4 video
  3. Save all videos to output/

Videos will be in 1080x1920 format (vertical shorts).


OPTIONAL: CUSTOMIZE SETTINGS
──────────────────────────────

Edit config.py to customize:

  Video Duration:
    VIDEO_DURATION = 60  # Change to 30, 45, 90, etc.

  Video Quality:
    VIDEO_FPS = 30  # 24, 30, or 60

  Voice Settings:
    VOICE_STABILITY = 0.5  # 0-1 (lower = more variation)
    VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Different voice

  Script Length:
    MAX_SCRIPT_LENGTH = 500
    MIN_SCRIPT_LENGTH = 100

"""

QUICK_REFERENCE = """
╔═══════════════════════════════════════════════════════════════╗
║                    QUICK REFERENCE                            ║
╚═══════════════════════════════════════════════════════════════╝

FILES CREATED:
──────────────

Main Scripts:
  main.py .................... Main execution script
  config.py .................. Configuration file
  setup.py ................... Project setup

Generation Modules:
  generate_script.py ......... Create AI scripts
  generate_voice.py .......... Synthesize voices
  generate_images.py ......... Download images
  generate_captions.py ....... Generate subtitles
  create_video.py ............ Compose videos

Configuration:
  .env ....................... API keys (secret!)
  requirements.txt ........... Python packages
  .gitignore ................. Git rules

Documentation:
  START_HERE.txt ............. Quick guide
  README.md .................. Full docs
  SETUP_GUIDE.py ............. Setup instructions
  QUICK_START.py ............. Quick commands
  PROJECT_SUMMARY.txt ........ Overview
  INDEX.py ................... Structure index


COMMANDS:
─────────

Project setup:
  python setup.py

Install packages:
  pip install -r requirements.txt

Generate videos:
  python main.py

View documentation:
  python SETUP_GUIDE.py
  python QUICK_START.py
  python INDEX.py


API REQUIREMENTS:
─────────────────

OpenAI GPT (Script generation):
  • Get key: https://platform.openai.com/api-keys
  • Add to .env as OPENAI_API_KEY
  • Used for: Generating creative scripts

ElevenLabs (Voice synthesis):
  • Get key: https://elevenlabs.io/
  • Add to .env as ELEVENLABS_API_KEY
  • Used for: Creating voice audio

Pexels (Stock images):
  • Get key: https://www.pexels.com/api/
  • Add to .env as PEXELS_API_KEY
  • Used for: Downloading images


OUTPUT:
───────

Final videos saved to: output/

Files generated per topic:
  • youtube_short_{id}.mp4 ...... Final video
  • audio_{id}.mp3 .............. Voice audio
  • captions.srt ................ Subtitles
  • Images in images/ folder .... Visual content


TROUBLESHOOTING:
────────────────

Setup error → Run: python setup.py
Missing modules → Run: pip install -r requirements.txt
API errors → Check .env file for correct keys
FFmpeg error → Install FFmpeg for your OS
No output → Check topics/topics.csv has data


NEXT STEPS AFTER SETUP:
───────────────────────

1. Run: python setup.py
2. Run: pip install -r requirements.txt
3. Edit .env with your API keys
4. Edit topics/topics.csv with topics
5. Run: python main.py
6. Check output/ for generated videos

"""

if __name__ == "__main__":
    print("\n" + "="*65)
    print(PROJECT_TREE)
    print("\n" + INSTALLATION_STEPS)
    print("\n" + QUICK_REFERENCE)
    print("="*65 + "\n")
