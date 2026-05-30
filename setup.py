"""
Project setup script - Creates directory structure
"""
import os

def setup_project():
    """Create all required directories and files"""
    base_dir = r"d:\Youtube_Auto"
    
    # Define directory structure
    directories = [
        os.path.join(base_dir, "assets", "backgrounds"),
        os.path.join(base_dir, "assets", "music"),
        os.path.join(base_dir, "audio"),
        os.path.join(base_dir, "captions"),
        os.path.join(base_dir, "images"),
        os.path.join(base_dir, "output"),
        os.path.join(base_dir, "scripts"),
        os.path.join(base_dir, "topics"),
    ]
    
    # Create all directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created: {directory}")
    
    print("\n✓ Project structure setup complete!")

if __name__ == "__main__":
    setup_project()
