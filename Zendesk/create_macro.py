import requests
from zendesk_credentials import username, api_token, zendesk_api_url

# Function to create a new macro
def create_macro(name, actions):
    url = f'{zendesk_api_url}/macros.json'
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "macro": {
            "title": name,
            "actions": actions
        }
    }
    response = requests.post(url, json=data, auth=(username, api_token), headers=headers)
    if response.status_code == 201:
        print(f"Macro '{name}' created successfully!")
        return True
    else:
        print(f"Failed to create macro. Status code: {response.status_code}, Error: {response.text}")
        return False

# Example usage
if __name__ == "__main__":
    macro_name = "Example Macro11"
    macro_actions = [
        {
            "field": "comment_value",
            "value": "Thank you for contacting us! We'll get back to you shortly."
        },
        {
            "field": "status",
            "value": "solved"
        }
    ]
    
    success = create_macro(macro_name, macro_actions)
    if success:
        print("Macro creation successful!")
    else:
        print("Macro creation failed!")
