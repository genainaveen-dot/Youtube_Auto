"""
Create the final video by combining audio, images, captions, and background music
"""
import os
from moviepy.editor import (
    ImageSequenceClip, AudioFileClip, CompositeAudioClip,
    CompositeVideoClip, TextClip, concatenate_videoclips
)
from config import (
    VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_FPS, OUTPUT_DIR,
    AUDIO_DIR, IMAGES_DIR, MUSIC_DIR
)


def create_video(
    audio_path: str,
    images_paths: list,
    background_music_path: str = None,
    output_filename: str = "output_video.mp4"
) -> str:
    """
    Combine audio, images, and music into a video
    
    Args:
        audio_path: Path to the main audio file
        images_paths: List of image file paths
        background_music_path: Path to background music
        output_filename: Name for the output video
    
    Returns:
        Path to the created video
    """
    try:
        # Load audio
        audio = AudioFileClip(audio_path)
        duration = audio.duration
        
        # Create video from images
        image_clip = ImageSequenceClip(images_paths, durations=[duration / len(images_paths)] * len(images_paths))
        image_clip = image_clip.set_size((VIDEO_WIDTH, VIDEO_HEIGHT))
        
        # Create audio composite
        audio_composite = audio
        
        if background_music_path and os.path.exists(background_music_path):
            background_audio = AudioFileClip(background_music_path)
            # Loop background music if needed
            if background_audio.duration < duration:
                num_loops = int(duration / background_audio.duration) + 1
                background_audio = concatenate_videoclips([background_audio] * num_loops)
            background_audio = background_audio.subclipped(0, duration).volumex(0.3)
            audio_composite = CompositeAudioClip([audio, background_audio])
        
        # Create final video
        video = image_clip.set_audio(audio_composite)
        video = video.set_fps(VIDEO_FPS)
        
        # Save video
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        video.write_videofile(output_path, verbose=False, logger=None)
        
        print(f"✓ Video created: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Error creating video: {e}")
        return ""


if __name__ == "__main__":
    # Example usage
    print("Video creation module loaded. Use create_video() function to generate videos.")
