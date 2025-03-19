import requests

try:
    response = requests.get('https://httpbin.org/ip', timeout=5)  # Timeout added
    response.raise_for_status()  # Raise an error for HTTP errors

    json_response = response.json()  # Try parsing JSON

    if 'origin' in json_response:
        print('Your IP is {0}'.format(json_response['origin']))
    else:
        print("Unexpected response format:", json_response)

except requests.exceptions.RequestException as e:
    print("Network error:", e)

except requests.exceptions.JSONDecodeError:
    print("Invalid JSON response received.")
