import requests
import json
import keys

site_id = keys.site_id
api_key = keys.api_key

BASE_URL = 'https://monitoringapi.solaredge.com'

def get_site_overview(site_id, api_key):
    """
    Retrieves the site overview data from the SolarEdge API.
    """
    
    url = f"{BASE_URL}/site/{site_id}/overview"
    params = {
        'api_key': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        
        # Exception raising
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Call the function and print the results
overview_data = get_site_overview(site_id, api_key)

if overview_data:
    print(json.dumps(overview_data, indent=4))
