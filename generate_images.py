"""
Generate or fetch images for video using Pexels API
"""
import os
import requests
from config import PEXELS_API_KEY, IMAGES_DIR, NUM_IMAGES, IMAGE_QUALITY


def search_and_download_images(query: str, count: int = NUM_IMAGES) -> list:
    """
    Search for images on Pexels and download them
    
    Args:
        query: Search query
        count: Number of images to download
    
    Returns:
        List of downloaded image paths
    """
    try:
        url = "https://api.pexels.com/v1/search"
        headers = {"Authorization": PEXELS_API_KEY}
        params = {"query": query, "per_page": count}
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            photos = response.json().get("photos", [])
            downloaded_images = []
            
            for idx, photo in enumerate(photos):
                image_url = photo["src"]["large"]
                image_response = requests.get(image_url)
                
                if image_response.status_code == 200:
                    filename = f"{query}_{idx}.jpg"
                    filepath = os.path.join(IMAGES_DIR, filename)
                    
                    with open(filepath, 'wb') as f:
                        f.write(image_response.content)
                    
                    downloaded_images.append(filepath)
                    print(f"✓ Downloaded: {filename}")
            
            return downloaded_images
        else:
            print(f"✗ Error fetching images: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"✗ Error downloading images: {e}")
        return []


if __name__ == "__main__":
    images = search_and_download_images("technology", count=5)
    print(f"\n✓ Downloaded {len(images)} images")
