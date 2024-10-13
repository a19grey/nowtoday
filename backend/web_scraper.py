import os
import json
from jina import call_jina_api
from url_validator import validate_and_normalize_url

def scrape_url(url='https://news.ycombinator.com/', save_to_file=True):
    normalized_url = validate_and_normalize_url(url)
    raw_content = call_jina_api(normalized_url)
    
    # Process the raw content as needed
    processed_content = process_raw_content(raw_content)
    
    if save_to_file:
        save_result_to_file(url, processed_content)
    
    return processed_content

def process_raw_content(raw_content):
    # Implement any necessary processing of the raw content
    # This is a placeholder implementation
    return f"Processed content: {raw_content}..."  # Increased to 500 characters for more context

def save_result_to_file(url, content):
    # Create a 'scraped_data' directory if it doesn't exist
    os.makedirs('scraped_data', exist_ok=True)
    
    # Create a filename based on the URL
    filename = os.path.join(f"scrape_{url.replace('://', '_').replace('/', '_')}.md")
    
    # Save the content to a JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({
            'url': url,
            'content': content
        }, f, ensure_ascii=False, indent=2)
    
    print(f"Results saved to {filename}")

def load_result_from_file(url):
    filename = os.path.join('scraped_data', f"{url.replace('://', '_').replace('/', '_')}.json")
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Loaded results from {filename}")
        return data['content']
    return None

if __name__ == "__main__":
    # This block will only run if the script is executed directly
    default_url = 'https://news.ycombinator.com/'
    
    # Try to load from file first
    result = load_result_from_file(default_url)
    
    if result is None:
        # If not found in file, scrape and save
        result = scrape_url(default_url)
    
    print(f"Content from {default_url}:")
    print(result)
