"""
Generate AI scripts for YouTube Shorts using OpenRouter API
"""
import requests
from config import OPENROUTER_API_KEY, MAX_SCRIPT_LENGTH, MIN_SCRIPT_LENGTH, TEMPERATURE, OPENROUTER_MODEL


def generate_script(topic: str, style: str = "entertaining") -> str:
    """
    Generate a short script for YouTube Shorts using OpenRouter API
    
    Args:
        topic: The topic for the script
        style: Writing style (entertaining, educational, motivational)
    
    Returns:
        Generated script text
    """
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        
        prompt = f"""Create a short, engaging YouTube Shorts script about: {topic}
        
        Requirements:
        - Length: {MIN_SCRIPT_LENGTH}-{MAX_SCRIPT_LENGTH} characters
        - Style: {style}
        - Include a hook in the first 2 seconds
        - Make it punchy and attention-grabbing
        - Perfect for 60-second vertical video
        
        Script:"""
        
        data = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": TEMPERATURE,
            "max_tokens": 200,
            "top_p": 1,
            "top_k": 0,
            "repetition_penalty": 1
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            script = result["choices"][0]["message"]["content"].strip()
            print(f"✓ Script generated for topic: {topic}")
            return script
        else:
            print(f"✗ Error generating script: {response.status_code} - {response.text}")
            return ""
        
    except Exception as e:
        print(f"✗ Error generating script: {e}")
        return ""


if __name__ == "__main__":
    topic = "The future of AI"
    script = generate_script(topic)
    print(f"\nGenerated Script:\n{script}")
