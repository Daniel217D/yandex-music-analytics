import os
from dotenv import load_dotenv
from yandex_music import Client

load_dotenv()

token = os.getenv('YANDEX_MUSIC_TOKEN')
if not token:
    raise ValueError('YANDEX_MUSIC_TOKEN environment variable is not set')

client = Client(token)
client.init()

tracks_ids = [track.track_id for track in client.users_likes_tracks()]
tracks = client.tracks(tracks_ids)

for track in tracks:
    print(track.title)
    