"""
Main orchestrator for YouTube AI Shorts generation pipeline
"""
import os
import csv
import sys
from generate_script import generate_script
from generate_voice import generate_voice
from generate_images import search_and_download_images
from generate_captions import generate_captions
from create_video import create_video
from config import TOPICS_DIR


def process_topic(topic_title: str, topic_id: int) -> bool:
    """
    Process a single topic through the entire pipeline
    
    Args:
        topic_title: Title of the topic
        topic_id: ID of the topic
    
    Returns:
        True if successful, False otherwise
    """
    print(f"\n{'='*60}")
    print(f"Processing Topic #{topic_id}: {topic_title}")
    print(f"{'='*60}")
    
    try:
        # Step 1: Generate script
        print("\n[1/5] Generating script...")
        script = generate_script(topic_title)
        if not script:
            print("✗ Failed to generate script")
            return False
        
        # Step 2: Generate voice
        print("\n[2/5] Generating voice...")
        audio_file = f"audio_{topic_id}.mp3"
        audio_path = generate_voice(script, audio_file)
        if not audio_path:
            print("✗ Failed to generate voice")
            return False
        
        # Step 3: Generate/fetch images
        print("\n[3/5] Fetching images...")
        images = search_and_download_images(topic_title.split()[0], count=10)
        if not images:
            print("⚠ Warning: No images found, but continuing...")
        
        # Step 4: Generate captions
        print("\n[4/5] Generating captions...")
        captions_file = generate_captions(script, 60)
        
        # Step 5: Create video
        print("\n[5/5] Creating video...")
        output_file = f"youtube_short_{topic_id}.mp4"
        video_path = create_video(audio_path, images, output_filename=output_file)
        
        if video_path:
            print(f"\n✓ Successfully created video for: {topic_title}")
            return True
        else:
            print(f"\n✗ Failed to create video for: {topic_title}")
            return False
            
    except Exception as e:
        print(f"\n✗ Error processing topic: {e}")
        return False


def load_topics(csv_file: str) -> list:
    """Load topics from CSV file"""
    try:
        topics = []
        csv_path = os.path.join(TOPICS_DIR, csv_file)
        
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                topics.append({
                    'id': row['topic_id'],
                    'title': row['topic_title']
                })
        
        return topics
    except Exception as e:
        print(f"✗ Error loading topics: {e}")
        return []


def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("YouTube AI Shorts Generator")
    print("="*60)
    
    # Load topics
    topics = load_topics("topics.csv")
    
    if not topics:
        print("✗ No topics found. Please add topics to topics/topics.csv")
        return
    
    print(f"\nLoaded {len(topics)} topics")
    
    # Process each topic
    successful = 0
    failed = 0
    
    for topic in topics:
        if process_topic(topic['title'], topic['id']):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(topics)}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
