"""
Configuration file for YouTube AI Shorts Generator
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys and Authentication
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
CAPTIONS_DIR = os.path.join(BASE_DIR, "captions")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
TOPICS_DIR = os.path.join(BASE_DIR, "topics")
BACKGROUNDS_DIR = os.path.join(ASSETS_DIR, "backgrounds")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")

# Video Settings
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 30
VIDEO_DURATION = 60  # seconds

# Audio Settings (Edge-TTS)
TTS_VOICE = "en-US-AriaNeural"  # Edge-TTS voice (Microsoft)
SPEECH_RATE = 1.0  # 0.5 to 2.0
SPEECH_PITCH = 1.0  # 0.5 to 2.0

# Text Generation Settings
MAX_SCRIPT_LENGTH = 500  # characters
MIN_SCRIPT_LENGTH = 100  # characters
TEMPERATURE = 0.7
OPENROUTER_MODEL = "google/gemini-2.0-flash-lite"  # OpenRouter model for GPT-like capabilities

# Image Settings
IMAGE_QUALITY = 85
NUM_IMAGES = 10

print("✓ Configuration loaded successfully")
print(f"  Using OpenRouter API")
print(f"  Using Edge-TTS for voice synthesis")
