import requests

API_KEY = 'Enter Youtube APi key'
CHANNEL_ID = 'Enter Channel ID'
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

def video_picker():
    api_key=API_KEY;
    channel_id=CHANNEL_ID 
    video_urls = []
    params = {
        'key': api_key,
        'channelId': channel_id,
        'part': 'snippet',
        'order': 'date',
        'maxResults': 10,
        'type': 'video'
    }

    response = requests.get(BASE_URL, params=params).json()
    for item in response.get('items', []):
        video_id = item['id']['videoId']
        video_urls.append(f'https://www.youtube.com/watch?v={video_id}')
        
    print(video_urls)
    return video_urls
