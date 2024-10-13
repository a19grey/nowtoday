# Project History

## 2023-05-XX: Simplified Backend Structure

- Moved all Python files to the `backend` directory.
- Updated imports to use direct imports instead of package imports.
- Removed unnecessary `__init__.py` files.
- Simplified project structure for easier management and clearer imports.

This change makes the project structure more straightforward and reduces confusion with Python imports. All backend-related files are now in a single directory, making it easier to navigate and maintain the codebase.

#2024-10-13 1am: Fixed backend url by changing to 5002 flask port. MAC OS OWNS PORT 5000!!!! jesus fuck.

# 2023-05-XX: Debugging Frontend-Backend Communication

- Added more detailed logging in the frontend's `handleSubmit` function.
- Updated the backend Flask server to include more comprehensive request logging.
- Ensured CORS is properly configured on the backend.
- Provided additional troubleshooting steps for diagnosing communication issues between frontend and backend.

These changes aim to identify why the Flask server is not receiving requests from the frontend when submitting URLs.


# Created Development Branch for Experimental Changes

- Created a new 'dev' branch to safely store and experiment with recent changes
- This includes updates to port configuration and other modifications
- Main branch remains untouched until changes are finalized and ready for merging
- Now it works after restarting the server. 

#2024/10/13 - 10:22 pm
Working. Needed to reset everthing. Some extra npm servers stuck running. 

#First entry
Everything is broken so I panicked and hard went back to an older git repo without stashing changes. And now stuff is broken. 

# 2023-05-XX: Resolved CORS Issues in Frontend-Backend Communication

- Updated CORS configuration in Flask backend to allow requests from frontend origin.
- Added support for OPTIONS method to handle CORS preflight requests.
- Manually added CORS headers to Flask responses.
- Updated frontend fetch request to include credentials.

These changes resolve the CORS policy errors that were preventing communication between the frontend and backend.

## 2023-05-XX: Recreated url_validator.py

- Recreated the accidentally deleted `url_validator.py` file.
- The file contains the `validate_and_normalize_url` function which:
  - Ensures the URL starts with 'https://' if no protocol is specified.
  - Adds 'www.' to the domain if it's missing and there's no existing subdomain.
  - Validates the URL structure.
  - Returns a cleaned and normalized URL.

This change restores the URL validation and normalization functionality that was lost when the file was accidentally deleted.

## 2023-05-XX: Updated web_scraper.py for Standalone Execution

- Modified `web_scraper.py` to allow standalone execution with a default URL.
- Added a `__main__` block to `web_scraper.py` for direct script execution.
- Increased the preview length of processed content to 500 characters for more context.
- Verified that `main.py` does not require any changes to accommodate these updates.

These changes allow for easier testing and debugging of the web scraping functionality independently of the main application.

## 2023-05-XX: Updated content_refiner.py for Standalone Execution

- Modified `content_refiner.py` to allow standalone execution.
- Added a `__main__` block to `content_refiner.py` for direct script execution.
- When run independently, `content_refiner.py` now calls `web_scraper.py` with default settings.
- Implemented a workflow that scrapes content, then refines it, and displays both results.

These changes allow for easier testing and debugging of the content refinement functionality, while also demonstrating the full workflow from web scraping to content refinement when run independently.
