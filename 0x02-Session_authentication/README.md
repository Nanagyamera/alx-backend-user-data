SESSION AUTHENTICATION

Error Handling

The Flask API includes custom error handlers for the following HTTP status codes:

404 Not Found: Returns a JSON response {"error": "Not found"}.

401 Unauthorized: Returns a JSON response {"error": "Unauthorized"}.

403 Forbidden: Returns a JSON response {"error": "Forbidden"}.

A new endpoint (GET /users/me) is created to retrieve the authenticated User object.

Testing

To test the custom error handlers:

Access the testing endpoints using curl or a web browser. Observe the returned JSON responses for each status code.

License

This project is licensed under the MIT License
