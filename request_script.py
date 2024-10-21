import requests

url = "https://developer.lge.com/secure/ResetDevModeSession.dev?sessionToken=ee4bc16a2482c4e4693b420f12180c2ae66da8a81eec42ed33a777409bce1852"

# Send the request
response = requests.get(url)

# Check and log status
if response.status_code == 200:
    print("Request successful!")
else:
    print(f"Failed with status code: {response.status_code}")
