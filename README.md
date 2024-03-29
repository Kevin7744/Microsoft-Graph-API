# Microsoft Graph API Event Management

This Python script demonstrates how to use the Microsoft Graph API to manage calendar events. It includes the following functionalities:

1. Generating an access token for authentication.
2. Creating an event with basic details.
3. Creating an event with detailed information.
4. Deleting an event.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- `msal` library (`pip install msal`)
- `rich` library (`pip install rich`)

## Usage

1. Update `APP_ID` and `SCOPES` in `main.py` with your Azure App ID and desired scopes.
2. Run `main.py`.

### Step 1: Generating an Access Token

- The `generate_access_token` function in `ms_graph.py` handles the access token generation.
- The function utilizes the `msal` library for authentication.
- If the access token expires, the function initiates a new authentication flow.

### Step 2.1: Creating an Event (Basic)

- The `construct_event_detail` function in `main.py` constructs the request body for creating an event with basic details.
- The `requests.post` method sends a POST request to create the event.
- The response contains the details of the created event.

### Step 2.2: Creating an Event (Detailed)

- An example is provided for creating an event with detailed information, including event body, start and end times, location, and attendees.
- The `construct_event_detail` function is used with additional parameters for detailed event creation.
- The `requests.post` method sends a POST request to create the detailed event.

### Deleting an Event

- To delete an event, use the event ID obtained from the creation response.
- The `requests.post` method sends a POST request to cancel the event.

## Additional Notes

- The `ms_graph.py` file contains the `generate_access_token` function for managing access tokens.
- Access tokens are cached in a file (`ms_graph_api_token.json`) for reuse.

## Disclaimer

This script demonstrates basic usage of the Microsoft Graph API for educational purposes. Use it responsibly and ensure compliance with Microsoft's API terms of use.
