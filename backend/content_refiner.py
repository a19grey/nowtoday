from openai_utils import call_openai_api
from web_scraper import scrape_url
import os
import glob

def refine_content(raw_content):
    """
    Refine the raw scraped content into a script suitable for video content.
    """
    # Step 1: Summarize interesting elements
    summary_prompt = f"Review the following raw website content and summarize all the interesting elements:\n\n{raw_content}"
    summary = call_openai_api(summary_prompt)
    
    # Save summary to file
    with open('summary.md', 'w') as f:
        f.write(summary)

    # Step 2: Create a 1-minute script
    script_prompt = f"Based on this summary, create a 1-minute long script to be read by a respected Instagram news personality. The script should be engaging and modern. But like someone reading a news script not cheesy or over the top. Like a TechChrunch report. No emojis or hashtags. :\n\n{summary}"
    script = call_openai_api(script_prompt)
    
    # Save script to file
    with open('script.md', 'w') as f:
        f.write(script)

    # Step 3: Double-check and clean the script
    final_prompt = """Ensure the following text contains only the script to be read, with absolutely no meta-content or descriptions. Remove any content that isn't part of the actual transcript. Remove descriptions like [Opening shot] or describing who is talking such as Newscaster or describing who is talking. Remove Host. No emojis or hashtags.:\n\n""" + script
    final_script = call_openai_api(final_prompt)
    
    # Save final script to file
    with open('final_script.md', 'w') as f:
        f.write(final_script)

    return final_script

if __name__ == "__main__":
    # This block will only run if the script is executed directly
    print("Content Refiner is running...")
    
    # Check for scrape*.md files in the current directory
    scrape_files = glob.glob('scrape*.md')
    
    if scrape_files:
        # Use the first matching file as input
        with open(scrape_files[0], 'r') as file:
            scraped_content = file.read()
        print(f"Using content from file: {scrape_files[0]}")
    else:
        # If no matching files found, call web_scraper with default settings
        scraped_content = scrape_url()
        print("No scrape*.md files found. Using web_scraper.")
    
    print("Scraped content:")
    print(scraped_content)
    print("\nRefining content...")
    
    refined_content = refine_content(scraped_content)
    
    print("\nRefined content:")
    print(refined_content)
