import requests
from zendesk_credentials import username, api_token, zendesk_api_url

# Function to fetch all macros
def fetch_all_macros():
    url = f'{zendesk_api_url}/macros.json'
    response = requests.get(url, auth=(username, api_token))
    response.raise_for_status()  # Raise an error for non-200 status codes
    macros = response.json()['macros']
    return macros

# Function to find macro by name
def find_macro_by_name(name):
    macros = fetch_all_macros()
    for macro in macros:
        if macro['title'] == name:
            return macro
    return None

# Function to delete macro by name
def delete_macro_by_name(name):
    macro = find_macro_by_name(name)
    if macro:
        macro_id = macro['id']
        url = f'{zendesk_api_url}/macros/{macro_id}.json'
        response = requests.delete(url, auth=(username, api_token))
        if response.status_code == 204:
            print(f"Macro '{name}' deleted successfully!")
        else:
            print(f"Failed to delete macro '{name}'. Status code: {response.status_code}, Error: {response.text}")
    else:
        print(f"Macro '{name}' not found.")

# Example usage
if __name__ == "__main__":
    macro_name = "Example Macro11"  # Change this to the name of the macro you want to delete
    delete_macro_by_name(macro_name)
