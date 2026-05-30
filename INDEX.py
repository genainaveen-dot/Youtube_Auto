"""
YouTube AI Shorts Generator - Complete Project Index

This file lists all components of the YouTube AI Shorts Generator project.
"""

PROJECT_STRUCTURE = {
    "project_name": "YouTube AI Shorts Generator",
    "version": "1.0.0",
    "description": "Automated short-form video generation using AI APIs",
    
    "core_modules": {
        "config.py": "Central configuration file with API keys and settings",
        "main.py": "Main orchestrator that coordinates the entire pipeline",
        "setup.py": "Automated project setup and directory creation",
    },
    
    "generation_modules": {
        "generate_script.py": "AI-powered script generation using OpenAI GPT",
        "generate_voice.py": "Text-to-speech synthesis using ElevenLabs API",
        "generate_images.py": "Image search and download via Pexels API",
        "generate_captions.py": "Automatic SRT caption generation",
        "create_video.py": "Video composition and MP4 rendering",
    },
    
    "configuration_files": {
        ".env": "Environment variables and API keys (DO NOT COMMIT!)",
        "requirements.txt": "Python package dependencies",
        ".gitignore": "Git ignore configuration",
        "__init__.py": "Python package initialization",
    },
    
    "documentation": {
        "README.md": "Complete project documentation and workflow",
        "PROJECT_SUMMARY.txt": "Overview of entire project",
        "SETUP_GUIDE.py": "Interactive setup and configuration guide",
        "QUICK_START.py": "Quick reference for common commands",
        "INDEX.py": "This file - project structure overview",
    },
    
    "directories_to_create": {
        "assets/": "Asset storage",
        "  backgrounds/": "Background images for videos",
        "  music/": "Background music files (MP3, WAV)",
        "audio/": "Generated voice audio files",
        "captions/": "Generated SRT subtitle files",
        "images/": "Downloaded and processed images",
        "output/": "Final MP4 video files",
        "scripts/": "Custom utility scripts",
        "topics/": "Configuration directory",
        "  topics.csv": "CSV file with video topics",
    }
}

QUICK_START_STEPS = [
    "1. Run setup: python setup.py",
    "2. Install dependencies: pip install -r requirements.txt",
    "3. Add API keys to .env file",
    "4. Add topics to topics/topics.csv",
    "5. Run generator: python main.py",
    "6. Check output/ for generated MP4 videos",
]

FILE_DESCRIPTIONS = {
    "config.py": """
    Configuration and Settings Management
    ─────────────────────────────────────
    - Load environment variables from .env
    - Define all project directories
    - Video settings (resolution, FPS, duration)
    - Audio settings (voice ID, stability, rate)
    - Text generation parameters
    - Image download settings
    
    Usage: Import in other modules for settings
    """,
    
    "main.py": """
    Main Orchestrator and Pipeline
    ──────────────────────────────
    - Load topics from topics/topics.csv
    - Execute generation pipeline for each topic:
      1. Generate script
      2. Generate voice
      3. Download images
      4. Generate captions
      5. Create video
    - Progress tracking and error handling
    - Summary reporting
    
    Usage: python main.py
    """,
    
    "generate_script.py": """
    AI Script Generation Module
    ───────────────────────────
    - Uses OpenAI GPT-3.5/4 API
    - Creates engaging short-form scripts
    - Customizable by topic and style
    - Returns 100-500 character scripts
    
    Function: generate_script(topic, style)
    Returns: str (generated script)
    """,
    
    "generate_voice.py": """
    Text-to-Speech Synthesis Module
    ───────────────────────────────
    - Uses ElevenLabs API
    - Converts scripts to natural-sounding speech
    - Supports multiple voice configurations
    - Outputs MP3 audio files
    
    Function: generate_voice(text, filename)
    Returns: str (path to audio file)
    """,
    
    "generate_images.py": """
    Image Search and Download Module
    ────────────────────────────────
    - Uses Pexels API for stock images
    - Searches for images by topic
    - Automatically downloads and saves
    - Quality optimization included
    
    Function: search_and_download_images(query, count)
    Returns: list (paths to downloaded images)
    """,
    
    "generate_captions.py": """
    Caption/Subtitle Generation Module
    ──────────────────────────────────
    - Generates SRT format subtitles
    - Time-synchronized with video
    - Automatic sentence splitting
    - Proper formatting for video players
    
    Function: generate_captions(script, video_duration)
    Returns: str (path to SRT file)
    """,
    
    "create_video.py": """
    Video Composition and Rendering Module
    ─────────────────────────────────────
    - Combines images, audio, and captions
    - Uses MoviePy library for composition
    - Supports background music mixing
    - Outputs vertical MP4 (1080x1920)
    
    Function: create_video(audio_path, images_paths, background_music_path)
    Returns: str (path to output MP4)
    """,
    
    "setup.py": """
    Project Initialization and Setup
    ────────────────────────────────
    - Creates all required directories
    - Sets up project structure
    - Can be run independently
    
    Usage: python setup.py
    """,
    
    ".env": """
    Environment Variables and API Keys
    ──────────────────────────────────
    IMPORTANT: Never commit this file to version control!
    
    Required variables:
    - OPENAI_API_KEY
    - ELEVENLABS_API_KEY
    - PEXELS_API_KEY
    
    Get keys from:
    - OpenAI: https://platform.openai.com/api-keys
    - ElevenLabs: https://elevenlabs.io/
    - Pexels: https://www.pexels.com/api/
    """,
    
    "requirements.txt": """
    Python Package Dependencies
    ────────────────────────────
    Install with: pip install -r requirements.txt
    
    Key packages:
    - python-dotenv: Environment variable management
    - openai: GPT API integration
    - elevenlabs: Text-to-speech API
    - moviepy: Video creation and editing
    - opencv-python: Image processing
    - Pillow: Image manipulation
    - requests: HTTP requests for APIs
    - numpy: Numerical operations
    - pandas: Data handling (CSV)
    """
}

def print_project_index():
    """Print comprehensive project index"""
    print("\n" + "="*70)
    print("   YOUTUBE AI SHORTS GENERATOR - PROJECT INDEX")
    print("="*70)
    
    print(f"\nProject: {PROJECT_STRUCTURE['project_name']}")
    print(f"Version: {PROJECT_STRUCTURE['version']}")
    print(f"Description: {PROJECT_STRUCTURE['description']}")
    
    print("\n" + "-"*70)
    print("QUICK START")
    print("-"*70)
    for step in QUICK_START_STEPS:
        print(f"  {step}")
    
    print("\n" + "-"*70)
    print("CORE MODULES")
    print("-"*70)
    for module, desc in PROJECT_STRUCTURE['core_modules'].items():
        print(f"  • {module}: {desc}")
    
    print("\n" + "-"*70)
    print("GENERATION MODULES")
    print("-"*70)
    for module, desc in PROJECT_STRUCTURE['generation_modules'].items():
        print(f"  • {module}: {desc}")
    
    print("\n" + "-"*70)
    print("CONFIGURATION FILES")
    print("-"*70)
    for file, desc in PROJECT_STRUCTURE['configuration_files'].items():
        print(f"  • {file}: {desc}")
    
    print("\n" + "-"*70)
    print("DOCUMENTATION")
    print("-"*70)
    for doc, desc in PROJECT_STRUCTURE['documentation'].items():
        print(f"  • {doc}: {desc}")
    
    print("\n" + "-"*70)
    print("DIRECTORIES TO CREATE")
    print("-"*70)
    for dir_name, desc in PROJECT_STRUCTURE['directories_to_create'].items():
        print(f"  • {dir_name} - {desc}")
    
    print("\n" + "="*70)
    print("For more information, see:")
    print("  • README.md - Full documentation")
    print("  • SETUP_GUIDE.py - Setup instructions")
    print("  • QUICK_START.py - Quick reference")
    print("="*70 + "\n")

if __name__ == "__main__":
    print_project_index()
