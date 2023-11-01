from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the API client
api_key = "AIzaSyAfpbyaOlJiRmry8ksfhj0dKzeQ3vk0hMQ"  # or you can use credentials
youtube = build('youtube', 'v3', developerKey=api_key)

try:
    # Make an API request (e.g., search for videos)
    request = youtube.search().list(q='Python Programming', type='video', part='id,snippet')
    response = request.execute()

    # Print the response
    for item in response['items']:
        print(item['snippet']['title'])

except HttpError as e:
    print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")