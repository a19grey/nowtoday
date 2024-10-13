# Placeholder for Jina API integration
import requests
import os
import json

def call_jina_api(url='https://news.ycombinator.com/'):
    jina_url = f'https://r.jina.ai/{url}'
    headers = {
        "Accept": "text/event-stream",
        "Authorization": f"Bearer {os.environ.get('JINA_API_KEY')}",
        "X-Timeout": "10",
        "X-With-Generated-Alt": "true",
        "X-With-Links-Summary": "true"
    }

    try:
        response = requests.get(jina_url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.text  # Return the raw text response
    except requests.RequestException as e:
        print(f"An error occurred while calling the JINA API: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response text: {e.response.text[:200]}...")  # Print first 200 characters
        return None

if __name__ == "__main__":
    result = call_jina_api()
    if result:
        print(result)  # Print the raw response
        # Optionally, you can still try to parse it as JSON if needed:
        # try:
        #     json_result = json.loads(result)
        #     print(json.dumps(json_result, indent=2))
        # except json.JSONDecodeError:
        #     print("Response is not in JSON format")
    else:
        print("Failed to get a response from the JINA API.")
