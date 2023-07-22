import requests
import shutil
import os

# The URL of the API to get the updated game code
url = f'https://rps-api.eliaskhoury1.repl.co/update/'

# Send a GET request to the API to fetch the updated code
response = requests.get(url)

# Check if the request was successful (status code 200 means success)
if response.status_code == 200:
    try:
        # Write the received content to a file named 'game.py' in binary mode ('wb')
        with open('game.py', 'wb') as f:
            f.write(response.content)

        # Copy the content of 'game.py' to a file named 'main.py'
        shutil.copyfile('game.py', 'main.py')

        # Delete the 'game.py' file to clean up the temporary file
        os.remove('game.py')

        # Inform the user that the game code was updated successfully
        print('Game code updated successfully! Please restart the program to take effect')
    except Exception as e:
        # If an error occurs during the update process, print the error message
        print(f'An error occurred while updating the game code: {e}')
else:
    # If the API request fails, print the status code returned by the API
    print(f'Failed to update the game code. Error code: {response.status_code}')
