import os
import sys
from heygen import generate_video_with_heygen
import time

# Update this constant to match your backend URL
BACKEND_URL = "http://localhost:5002"

def generate_video(content):
    # Use a relative path for the generated video
    generated_video_filename = "generated.mp4"
    generated_video_path = generated_video_filename  # No need for 'backend' prefix

    start_time = time.time()

    # Check if generated.mp4 already exists in the backend folder
    if os.path.exists(generated_video_path):
        print(f"Using existing video file: {generated_video_path}")
    else:
        # If the file doesn't exist, use HeyGen API to generate video
        # Uncomment the following line when HeyGen API is implemented
        # video_url = generate_video_with_heygen(content)
        
        # For now, we'll use a placeholder
        # You may want to create an empty file here for testing purposes
        print(f"Using existing video file: {generated_video_path}")

    # Construct a proper URL that can be accessed by the frontend
    video_url = f"http://localhost:5002/generated.mp4"

    end_time = time.time()
    run_time = end_time - start_time

    video_result = {
        "video_url": video_url,
        "video_path": generated_video_path,
        "run_time": f"{run_time:.2f} seconds"
    }

    return video_result

def main():
    if len(sys.argv) < 2:
        print("Usage: python video_generator.py <content>")
        sys.exit(1)
    
    content = sys.argv[1]
    result = generate_video(content)
    print(f"Video generation result: {result}")

if __name__ == "__main__":
    main()
