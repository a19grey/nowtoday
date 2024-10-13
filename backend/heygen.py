import requests
import time
import os
import json

# Placeholder for HeyGen API integration
def generate_video_with_heygen(content):
    avatar_id = "acc4cc649ff94b9cb95e1953f190b7c5"
    voice_id = "a338630296dc482b95d908153401459e"
    api_key = os.environ.get("HEYGEN_API_KEY")

    if not api_key:
        raise ValueError("HEYGEN_API_KEY environment variable is not set")

    # Limit content to 1450 characters
    content = content[:1450]

    # Generate video
    generate_url = "https://api.heygen.com/v2/video/generate"
    headers = {
        "X-Api-Key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": avatar_id,
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "text",
                    "input_text": content,
                    "voice_id": voice_id,
                    "speed": 1.5
                }
            }
        ],
        "test": True,
        "aspect_ratio": "16:9",
        "dimension": {
            "width": 1280,
            "height": 720
        }
    }

    response = requests.post(generate_url, headers=headers, json=payload)
    response.raise_for_status()
    video_id = response.json().get("data", {}).get("video_id")

    if not video_id:
        raise ValueError("Failed to get video_id from HeyGen API")

    # Check video status
    status_url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
    
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        print(f"Time elapsed: {elapsed_time:.2f} seconds")

        status_response = requests.get(status_url, headers=headers)
        status_response.raise_for_status()
        status_data = status_response.json().get("data", {})
        status = status_data.get("status")

        print(f"Current status: {status}")

        if status == "completed":
            video_url = status_data.get("video_url")
            return {"status": "Video generation completed", "video_url": video_url}
        elif status == "failed":
            error_message = status_data.get("error", {}).get("message", "Unknown error")
            error_code = status_data.get("error", {}).get("code", "Unknown code")
            full_response = status_response.json()
            error_details = {
                "status": "Video generation failed",
                "error_message": error_message,
                "error_code": error_code,
                "full_response": full_response
            }
            print("Error details:")
            print(json.dumps(error_details, indent=2))
            raise ValueError(f"Video generation failed: {error_message} (Code: {error_code})")
        
        time.sleep(30)  # Wait for 5 seconds before checking again

def download_video(video_url="https://files2.heygen.ai/aws_pacific/avatar_tmp/23f05e1c16234004b03482521b61f1f6/e3ae7dc2e08443a391b042fa1a0c19b4.mp4?Expires=1729423534&Signature=pH7w8UJH7YNHCs1zlS-I-oMD4gExYjdo7ca3clbYpwRcpL9rorrHmhoAn39AB7T71BdqdPfnREpCeP2aTtpLtiU1qoBuLyUrlAM4tt8U-62KZhyAXIUyvSkO4vjXZsHvOy1c~4wWaacUuS9t4GvhMocZssM7iufmvBXnlcv~pAJ9l8x~6aMoNUCY63DfsJIgUqFKQEhxG2ra~dPFr214GaABAPXuBypo5pw8DvIxueh5odRqinddW3l4OECDUDtvG~ggzmY~l1X72vAjbm0VYqzOSRb6gdPtRcmLDY2MNohKPsn0xxLJBb1Vm-LkanEbwC-YFOYj3Gi3QdUkQ~wBOw__&Key-Pair-Id=K38HBHX5LX3X2H", output_filename="generated.mp4"):
    # Check if genvideo.txt exists in the /backend folder
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    genvideo_path = os.path.join(backend_dir, "genvideo.txt")
    
    if os.path.exists(genvideo_path):
        with open(genvideo_path, "r") as file:
            video_url = file.read().strip()
        print(f"Using video URL from /backend/genvideo.txt: {video_url}")

    response = requests.get(video_url, stream=True)
    response.raise_for_status()

    with open(output_filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    
    return os.path.abspath(output_filename)

# Modified main script
if __name__ == "__main__":
    script_path = "script.md"
    
    if os.path.exists(script_path):
        with open(script_path, "r") as file:
            script_content = file.read().strip()
        
        if script_content:
            print("Generating video with content from script.md...")
            result = generate_video_with_heygen(script_content)
            print(result)

            if result["status"] == "Video generation completed":
                video_url = result["video_url"]
                print("Downloading video...")
                downloaded_file_path = download_video(video_url)
                print(f"Video downloaded and saved at: {downloaded_file_path}")
            else:
                print("Video generation did not complete successfully.")
        else:
            print("script.md is empty. Please add content to the file.")
    else:
        print("No material available. Please create a script.md file with your video content.")
