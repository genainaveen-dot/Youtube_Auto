"""
Generate captions for the video
"""
import os
from config import CAPTIONS_DIR


def generate_captions(script: str, video_duration: int = 60) -> str:
    """
    Generate captions from the script
    
    Args:
        script: The video script
        video_duration: Duration of video in seconds
    
    Returns:
        Path to the generated captions file
    """
    try:
        # Split script into segments
        sentences = script.split('.')
        
        # Calculate timing for each sentence
        time_per_sentence = video_duration / len(sentences)
        
        srt_content = ""
        start_time = 0
        
        for idx, sentence in enumerate(sentences):
            if sentence.strip():
                end_time = start_time + time_per_sentence
                
                # Format as SRT subtitle
                srt_content += f"{idx + 1}\n"
                srt_content += f"{format_time(start_time)} --> {format_time(end_time)}\n"
                srt_content += f"{sentence.strip()}\n\n"
                
                start_time = end_time
        
        # Save to file
        output_file = os.path.join(CAPTIONS_DIR, "captions.srt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(srt_content)
        
        print(f"✓ Captions generated: {output_file}")
        return output_file
        
    except Exception as e:
        print(f"✗ Error generating captions: {e}")
        return ""


def format_time(seconds: float) -> str:
    """Convert seconds to SRT time format (HH:MM:SS,mmm)"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


if __name__ == "__main__":
    sample_script = "This is a test. The future is bright. AI is amazing."
    caption_file = generate_captions(sample_script, 60)
