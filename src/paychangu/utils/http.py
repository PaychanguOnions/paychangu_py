import json
import requests

def handle_response(response):
    try:
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON response from the API")
    except requests.exceptions.HTTPError as e:
        raise Exception(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error occurred while making the request: {e}") 