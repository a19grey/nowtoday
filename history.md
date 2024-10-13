
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
