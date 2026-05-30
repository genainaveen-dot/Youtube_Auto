"""
UPDATED SETUP GUIDE - OpenRouter + Edge-TTS Version
"""

SETUP_INSTRUCTIONS = """
╔════════════════════════════════════════════════════════════════╗
║  YouTube AI Shorts Generator - Setup Guide (Updated)           ║
║  Now with OpenRouter + Edge-TTS                               ║
╚════════════════════════════════════════════════════════════════╝

UPDATED FEATURES:
─────────────────

✅ OpenRouter API (Instead of OpenAI)
   • Access to multiple LLMs (Gemini, Claude, GPT, Llama)
   • More cost-effective
   • Better value for money
   • Free tier available

✅ Edge-TTS (Instead of ElevenLabs)
   • FREE voice synthesis
   • Microsoft's high-quality voices
   • No API key needed
   • Multiple languages and voices
   • Better quality than TTS libraries


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

Dependencies include (UPDATED):
    • requests - API calls
    • edge-tts - FREE voice synthesis ⭐ NEW
    • moviepy - Video creation
    • opencv-python - Image processing
    • pexels - Image search
    • python-dotenv - Environment variables
    • numpy, pandas - Data processing


STEP 3: Configure OpenRouter API Key
────────────────────────────────────
Edit the .env file and add your OpenRouter API key:

    OPENROUTER_API_KEY=sk-or-v1-...

To get your API key:
    1. Visit: https://openrouter.ai/
    2. Sign up (FREE)
    3. Go to: https://openrouter.ai/keys
    4. Create new API key
    5. Copy the key
    6. Paste into .env file

Cost:
    • Free tier available
    • Pay-as-you-go for production
    • Usually $0.01-0.05 per script
    • Much cheaper than OpenAI!


STEP 4: Pexels API (For Images)
───────────────────────────────
Edit the .env file and add Pexels API key:

    PEXELS_API_KEY=your_key_here

To get your key:
    1. Visit: https://www.pexels.com/api/
    2. Sign up (FREE)
    3. Create API key
    4. Copy and paste into .env

Cost: COMPLETELY FREE!


STEP 5: Edge-TTS (Voice Synthesis)
──────────────────────────────────
✅ NO API KEY NEEDED!

Edge-TTS is built-in and FREE:
    • No registration required
    • No API key needed
    • Completely free to use
    • Uses Microsoft's Azure voice engines
    • Available voices:
      - en-US-AriaNeural (default)
      - en-US-GuyNeural
      - en-US-JennyNeural
      - en-GB-RyanNeural
      - Many more...

To use different voices, edit config.py:
    TTS_VOICE = "en-US-GuyNeural"  # Change voice


STEP 6: Add Video Topics
─────────────────────────
Edit topics/topics.csv to add your video topics:

Example:
    topic_id,topic_title,category,difficulty
    1,10 AI Facts,Technology,Medium
    2,Cooking Tips,Food,Easy
    3,Study Hacks,Education,Medium

Format:
    • topic_id: Unique number for each topic
    • topic_title: Subject for the video
    • category: Content category
    • difficulty: Easy/Medium/Hard


STEP 7: Customize Configuration (Optional)
───────────────────────────────────────────
Edit config.py to customize:

Video Settings:
    • VIDEO_WIDTH = 1080 (shorts are vertical)
    • VIDEO_HEIGHT = 1920
    • VIDEO_FPS = 30
    • VIDEO_DURATION = 60 (seconds)

Audio Settings (Edge-TTS):
    • TTS_VOICE = "en-US-AriaNeural" (Microsoft voice)
    • SPEECH_RATE = 1.0 (0.5 = half speed, 2.0 = double)
    • SPEECH_PITCH = 1.0 (adjust voice pitch)

Text Generation:
    • MAX_SCRIPT_LENGTH = 500 (characters)
    • MIN_SCRIPT_LENGTH = 100 (characters)
    • TEMPERATURE = 0.7 (creativity level)
    • OPENROUTER_MODEL = "google/gemini-2.0-flash-lite"

Image Settings:
    • NUM_IMAGES = 10 (images per video)
    • IMAGE_QUALITY = 85 (JPG quality)


STEP 8: Run the Generator
─────────────────────────
Execute the main script:

    python main.py

This will:
    1. Load topics from topics/topics.csv
    2. Generate scripts using OpenRouter API
    3. Create voice audio using Edge-TTS (FREE!)
    4. Download images from Pexels
    5. Generate captions (SRT format)
    6. Compose final video (MP4)
    7. Save output to output/ directory

Progress will be displayed for each step.


AVAILABLE EDGE-TTS VOICES
──────────────────────────

English (US):
    • en-US-AriaNeural (Female) ⭐ Default
    • en-US-GuyNeural (Male)
    • en-US-JennyNeural (Female)
    • en-US-AmberNeural (Female)

English (GB):
    • en-GB-RyanNeural (Male)
    • en-GB-SoniaNeural (Female)

Other Languages:
    • es-ES-AlvaroNeural (Spanish)
    • fr-FR-DeniseNeural (French)
    • de-DE-ConradNeural (German)
    • ja-JP-NanamisNeural (Japanese)
    • And many more...


COST COMPARISON
────────────────

OpenAI GPT-4:
    • ~$0.03 per request
    • Limited requests/month on free tier

OpenRouter (Gemini):
    • ~$0.002 per request
    • Much cheaper!

ElevenLabs TTS:
    • ~$0.30 per 1000 characters
    • Limited free tier

Edge-TTS:
    • COMPLETELY FREE ⭐
    • No limits
    • No API key needed

Pexels Images:
    • COMPLETELY FREE ⭐
    • 50 requests per hour

TOTAL COST:
    • Scripts: ~$0.01-0.05 per video
    • TTS: $0 (FREE!)
    • Images: $0 (FREE!)
    • Total: ~$0.01-0.05 per video


TROUBLESHOOTING
───────────────

Q: Getting "ModuleNotFoundError" errors?
A: Run: pip install -r requirements.txt

Q: Getting API errors?
A: Check your OpenRouter API key in .env file

Q: TTS not working?
A: Edge-TTS should work without any key
   Make sure you have internet connection
   Try: pip install --upgrade edge-tts

Q: No images downloading?
A: Check Pexels API key is correct
   Check rate limits (50 per hour)

Q: Video creation is slow?
A: Normal - depends on video length and system specs

Q: FFmpeg not found?
A: Install FFmpeg:
   Windows: choco install ffmpeg
   Mac: brew install ffmpeg
   Linux: sudo apt-get install ffmpeg

Q: Different voice not working?
A: Make sure voice name is correct
   Test with: python generate_voice.py


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
├── generate_script.py      # Script generation (OpenRouter)
├── generate_voice.py       # Voice synthesis (Edge-TTS) ⭐ UPDATED
├── generate_images.py      # Image acquisition
├── generate_captions.py    # Subtitle generation
├── create_video.py         # Video composition
├── setup.py                # Project setup
├── requirements.txt        # Dependencies ⭐ UPDATED
├── .env                    # API keys
├── README.md               # Documentation
└── topics/
    └── topics.csv          # Video topics


NEXT STEPS
──────────
1. Follow all setup steps above
2. Test with a single topic first
3. Monitor costs (mainly OpenRouter)
4. Adjust config.py settings as needed
5. Scale up with more topics


KEY CHANGES FROM ORIGINAL
─────────────────────────
✅ OpenAI → OpenRouter (cheaper)
✅ ElevenLabs → Edge-TTS (free)
✅ Updated requirements.txt
✅ Updated config.py
✅ Updated generate_script.py
✅ Updated generate_voice.py
✅ Better cost efficiency


For more info, see README.md
"""

if __name__ == "__main__":
    print(SETUP_INSTRUCTIONS)
    
    # Save to file
    with open("SETUP_GUIDE_UPDATED.txt", "w", encoding="utf-8") as f:
        f.write(SETUP_INSTRUCTIONS)
    
    print("\n✓ Updated setup guide saved to SETUP_GUIDE_UPDATED.txt")
