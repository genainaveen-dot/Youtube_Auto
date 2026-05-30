"""
Complete Setup Guide for YouTube AI Shorts Generator
"""

import os
import sys

SETUP_INSTRUCTIONS = """
╔════════════════════════════════════════════════════════════════╗
║     YouTube AI Shorts Generator - Complete Setup Guide         ║
╚════════════════════════════════════════════════════════════════╝

STEP 1: Create Directory Structure
───────────────────────────────────
Run this command in the project root:

    python setup.py

This will create all necessary folders:
    • assets/backgrounds/ - Store background images
    • assets/music/ - Store background music files
    • audio/ - Generated voice audio files
    • captions/ - Generated subtitle files
    • images/ - Downloaded images
    • output/ - Final video outputs
    • scripts/ - Custom utility scripts
    • topics/ - Topic configuration


STEP 2: Install Python Dependencies
────────────────────────────────────
Run:
    pip install -r requirements.txt

Dependencies include:
    • openai - GPT API integration
    • elevenlabs - Text-to-speech
    • moviepy - Video creation
    • opencv-python - Image processing
    • requests - API calls
    • python-dotenv - Environment variables


STEP 3: Configure API Keys
──────────────────────────
Edit the .env file and add your API keys:

    OPENAI_API_KEY=sk-xxxxx...
    ELEVENLABS_API_KEY=xxxxx...
    PEXELS_API_KEY=xxxxx...

To get API keys:

    OpenAI (GPT-3.5/4):
    → Visit: https://platform.openai.com/api-keys
    → Create new secret key
    → Copy and paste into .env

    ElevenLabs (Voice Synthesis):
    → Visit: https://elevenlabs.io/
    → Sign up / Login
    → Go to Profile → API Key
    → Copy and paste into .env

    Pexels (Stock Images):
    → Visit: https://www.pexels.com/api/
    → Sign up / Login
    → Create API key
    → Copy and paste into .env


STEP 4: Add Topics
──────────────────
Edit topics/topics.csv to add your video topics:

Example:
    topic_id,topic_title,category,difficulty
    1,10 Science Facts,Science,Medium
    2,Cooking Tips,Food,Easy
    3,Study Hacks,Education,Medium

Format:
    • topic_id: Unique number for each topic
    • topic_title: Subject for the video
    • category: Content category
    • difficulty: Easy/Medium/Hard


STEP 5: Customize Configuration (Optional)
───────────────────────────────────────────
Edit config.py to customize:

    Video Settings:
    • VIDEO_WIDTH = 1080 (shorts are vertical)
    • VIDEO_HEIGHT = 1920
    • VIDEO_FPS = 30
    • VIDEO_DURATION = 60 (seconds)

    Audio Settings:
    • VOICE_ID = "EXAVITQu4vr4xnSDxMaL" (ElevenLabs voice)
    • SPEECH_RATE = 1.0
    • VOICE_STABILITY = 0.5

    Text Generation:
    • MAX_SCRIPT_LENGTH = 500 (characters)
    • TEMPERATURE = 0.7 (creativity level)


STEP 6: Run the Generator
─────────────────────────
Execute the main script:

    python main.py

This will:
    1. Load topics from topics/topics.csv
    2. Generate scripts using OpenAI GPT
    3. Create voice audio using ElevenLabs
    4. Download images from Pexels
    5. Generate captions (SRT format)
    6. Compose final video (MP4)
    7. Save output to output/ directory

Progress will be displayed for each step.


TROUBLESHOOTING
───────────────

Q: Getting "ModuleNotFoundError" errors?
A: Run: pip install -r requirements.txt

Q: Getting API errors?
A: Check your API keys in .env file are correct

Q: Video creation is slow?
A: Normal - depends on video length and system specs

Q: FFmpeg not found?
A: Install FFmpeg:
   Windows: choco install ffmpeg
   Mac: brew install ffmpeg
   Linux: sudo apt-get install ffmpeg

Q: No images downloading?
A: Check Pexels API key and rate limits

Q: File permission errors?
A: Ensure output/ and other dirs have write permissions


EXAMPLE WORKFLOW
────────────────
1. Create directories: python setup.py
2. Install dependencies: pip install -r requirements.txt
3. Add API keys to .env
4. Add topics to topics/topics.csv
5. Run generator: python main.py
6. Check output/ directory for MP4 files


FILE STRUCTURE
──────────────
youtube-ai-shorts/
├── config.py               # Configuration settings
├── main.py                 # Main execution script
├── generate_script.py      # Script generation
├── generate_voice.py       # Voice synthesis
├── generate_images.py      # Image acquisition
├── generate_captions.py    # Subtitle generation
├── create_video.py         # Video composition
├── setup.py                # Project setup
├── requirements.txt        # Dependencies
├── .env                    # API keys (never commit!)
├── README.md               # Documentation
└── topics/
    └── topics.csv          # Video topics


NEXT STEPS
──────────
1. Follow all setup steps above
2. Test with a single topic first
3. Monitor output quality
4. Adjust config.py settings as needed
5. Scale up with more topics


For more info, see README.md
"""

if __name__ == "__main__":
    print(SETUP_INSTRUCTIONS)
    
    # Save to file
    with open("SETUP_GUIDE.txt", "w", encoding="utf-8") as f:
        f.write(SETUP_INSTRUCTIONS)
    
    print("\n✓ Setup guide saved to SETUP_GUIDE.txt")
