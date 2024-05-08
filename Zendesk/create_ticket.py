import requests
import json
from zendesk_credentials import username, api_token, create_ticket_url

# Ticket data
ticket_data = {
    "ticket": {
        "subject": "Test Ticket",
        "comment": {
            "body": "This is a test ticket created via API."
        }
    }
}

# Convert the ticket data to JSON
payload = json.dumps(ticket_data)

# Set up the request headers
headers = {
    'Content-Type': 'application/json',
}

# Make the API request to create the ticket
response = requests.post(create_ticket_url, data=payload, auth=(username, api_token), headers=headers)

# Check if the request was successful
if response.status_code == 201:
    print("Ticket created successfully!")
    ticket_id = response.json()['ticket']['id']
    print("Ticket ID:", ticket_id)
else:
    print("Failed to create ticket. Status code:", response.status_code)
    print("Response:", response.text)