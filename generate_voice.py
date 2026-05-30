"""
Generate voice audio from text using Edge-TTS (Microsoft)
"""
import os
import asyncio
import edge_tts
from config import AUDIO_DIR, TTS_VOICE, SPEECH_RATE, SPEECH_PITCH


async def generate_voice_async(text: str, filename: str) -> str:
    """
    Convert text to speech using Edge-TTS (async function)
    
    Args:
        text: The text to convert to speech
        filename: Output filename
    
    Returns:
        Path to the generated audio file
    """
    try:
        output_path = os.path.join(AUDIO_DIR, filename)
        
        # Create communicate object with voice settings
        communicate = edge_tts.Communicate(
            text=text,
            voice=TTS_VOICE,
            rate=f"+{int((SPEECH_RATE - 1) * 100)}%",  # Convert to percentage format
            pitch=f"+{int((SPEECH_PITCH - 1) * 50)}Hz"  # Convert to Hz format
        )
        
        # Save audio file
        await communicate.save(output_path)
        
        print(f"✓ Voice generated: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Error generating voice: {e}")
        return ""


def generate_voice(text: str, filename: str) -> str:
    """
    Synchronous wrapper for Edge-TTS voice generation
    
    Args:
        text: The text to convert to speech
        filename: Output filename
    
    Returns:
        Path to the generated audio file
    """
    try:
        # Run async function in event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(generate_voice_async(text, filename))
        loop.close()
        return result
    except Exception as e:
        print(f"✗ Error in generate_voice: {e}")
        return ""


if __name__ == "__main__":
    sample_text = "Welcome to AI Shorts! This is a test of the text-to-speech system using Edge-TTS."
    audio_file = generate_voice(sample_text, "test_audio.mp3")
    print(f"Generated: {audio_file}")
