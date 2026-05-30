"""
YouTube AI Shorts Generator - Architecture & Data Flow Diagram
"""

ARCHITECTURE = """
╔═══════════════════════════════════════════════════════════════════╗
║          YOUTUBE AI SHORTS GENERATOR - ARCHITECTURE               ║
╚═══════════════════════════════════════════════════════════════════╝


DATA FLOW DIAGRAM:
──────────────────

                          ┌─────────────────┐
                          │  topics.csv     │
                          │ (Video Topics)  │
                          └────────┬────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │   main.py       │
                          │ (Orchestrator)  │
                          └────────┬────────┘
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
            ▼                      ▼                      ▼
    ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
    │ generate_script  │  │ generate_images  │  │ generate_voice   │
    │     (GPT API)    │  │  (Pexels API)    │  │(ElevenLabs API)  │
    └────────┬─────────┘  └────────┬─────────┘  └─────────┬────────┘
             │                     │                      │
             │ Script              │ Images              │ Audio
             ▼                     ▼                      ▼
    ┌─────────────────────────────────────────────────────────────┐
    │              create_video.py                                │
    │         (Video Composition & Rendering)                     │
    │                                                             │
    │  • Combine images with timing                              │
    │  • Sync audio track                                        │
    │  • Add generated captions                                  │
    │  • Overlay background music                                │
    │  • Render final MP4 (1080x1920)                            │
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │  output/        │
                          │  final_video.mp4│
                          └─────────────────┘


MODULE ARCHITECTURE:
────────────────────

┌──────────────────────────────────────────────────────────────────┐
│                        MAIN APPLICATION                           │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────┐      ┌──────────────────────────────┐  │
│  │   config.py        │      │  main.py (Orchestrator)      │  │
│  │                    │      │                              │  │
│  │ • API Keys         │      │ • Load topics                │  │
│  │ • Paths            │◄─────┤ • Coordinate modules         │  │
│  │ • Settings         │      │ • Error handling             │  │
│  │ • Constants        │      │ • Progress tracking          │  │
│  └────────────────────┘      └──────────────────────────────┘  │
│                                           │                      │
│                                           ▼                      │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │           GENERATION MODULES                             │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │                                                          │  │
│  │  generate_script.py      generate_voice.py             │  │
│  │  • OpenAI GPT API        • ElevenLabs API              │  │
│  │  • Script creation       • Voice synthesis             │  │
│  │  • Customizable styles   • Multiple voices             │  │
│  │                                                          │  │
│  │  generate_images.py      generate_captions.py          │  │
│  │  • Pexels API            • SRT generation              │  │
│  │  • Image search          • Time synchronization        │  │
│  │  • Auto download         • Format conversion           │  │
│  │                                                          │  │
│  │  create_video.py                                        │  │
│  │  • MoviePy library                                      │  │
│  │  • Image sequencing                                     │  │
│  │  • Audio mixing                                         │  │
│  │  • Caption overlay                                      │  │
│  │  • MP4 rendering                                        │  │
│  │                                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘


API INTEGRATIONS:
────────────────

┌─────────────────────────────────────────────────────────────────┐
│  OPENAI GPT API                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Module: generate_script.py                                     │
│  Purpose: Generate engaging short-form scripts                  │
│  Input: Topic, style preference                                 │
│  Output: 100-500 character script                               │
│  Rate Limit: Depends on API tier                                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  ELEVENLABS API                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Module: generate_voice.py                                      │
│  Purpose: Convert text to natural-sounding speech               │
│  Input: Script text                                             │
│  Output: MP3 audio file                                         │
│  Features: Multiple voices, stability control                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  PEXELS API                                                     │
├─────────────────────────────────────────────────────────────────┤
│  Module: generate_images.py                                     │
│  Purpose: Search and download stock images                      │
│  Input: Search query                                            │
│  Output: Image files (JPG)                                      │
│  Features: Free API, no authentication needed                   │
└─────────────────────────────────────────────────────────────────┘


FILE I/O STRUCTURE:
───────────────────

INPUT:
  topics/topics.csv ................. Video topics & metadata
  config.py ......................... Configuration & settings
  .env ............................. API keys

GENERATION:
  topics/ ........................... Input data
  audio/ ........................... Generated audio files
  images/ .......................... Downloaded images
  captions/ ........................ Generated SRT files

OUTPUT:
  output/ ........................... Final MP4 videos

ASSETS:
  assets/backgrounds/ ............... Background images
  assets/music/ ..................... Background music


PROCESSING PIPELINE:
────────────────────

For each topic:
  
  1. SCRIPT GENERATION
     Input:  Topic title
     Process: Send to OpenAI GPT API
     Output: Script text → audio/scripts/ (in memory)
  
  2. VOICE SYNTHESIS
     Input:  Script text
     Process: Send to ElevenLabs API
     Output: MP3 file → audio/{topic_id}.mp3
  
  3. IMAGE ACQUISITION
     Input:  Topic title
     Process: Query Pexels API, download images
     Output: JPG files → images/{topic}_{idx}.jpg
  
  4. CAPTION GENERATION
     Input:  Script text, video duration
     Process: Parse sentences, calculate timings
     Output: SRT file → captions/captions.srt
  
  5. VIDEO COMPOSITION
     Input:  MP3, JPG files, SRT file
     Process: Compose using MoviePy
     Output: MP4 file → output/youtube_short_{id}.mp4

"""

CONFIG_OPTIONS = """
CUSTOMIZABLE SETTINGS (config.py):
──────────────────────────────────

VIDEO SETTINGS:
  VIDEO_WIDTH = 1080              Width of output video
  VIDEO_HEIGHT = 1920             Height (vertical shorts)
  VIDEO_FPS = 30                  Frames per second
  VIDEO_DURATION = 60             Length in seconds

AUDIO SETTINGS:
  VOICE_ID = "EXAVITQu4vr4x..."   ElevenLabs voice identifier
  SPEECH_RATE = 1.0               Speed of speech (1.0 = normal)
  VOICE_STABILITY = 0.5           Consistency of voice (0-1)

TEXT GENERATION:
  MAX_SCRIPT_LENGTH = 500         Maximum characters
  MIN_SCRIPT_LENGTH = 100         Minimum characters
  TEMPERATURE = 0.7               Creativity level (0-1)

IMAGE SETTINGS:
  IMAGE_QUALITY = 85              JPEG compression quality
  NUM_IMAGES = 10                 Images to download per topic

API ENDPOINTS:
  Defined in respective modules
  Authentication via .env file
"""

if __name__ == "__main__":
    print(ARCHITECTURE)
    print("\n" + CONFIG_OPTIONS)
