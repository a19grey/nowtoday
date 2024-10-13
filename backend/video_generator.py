import os
import sys
from heygen import generate_video_with_heygen
import time

def generate_video(content):
    # Get the absolute path of the backend directory
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    generated_video_path = os.path.join(backend_dir, "generated.mp4")

    start_time = time.time()

    # Check if generated.mp4 already exists in the backend folder
    if os.path.exists(generated_video_path):
        print(f"Using existing video file: {generated_video_path}")
        video_url = f"file://{generated_video_path}"
    else:
        # If the file doesn't exist, use HeyGen API to generate video
        # Uncomment the following line when HeyGen API is implemented
        # video_url = generate_video_with_heygen(content)
        
        # For now, we'll use a placeholder URL
        # video_result = generate_video_with_heygen(content)
        video_url = f"file://{generated_video_path}"

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
