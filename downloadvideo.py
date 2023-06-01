from pytube import YouTube
from pytube.exceptions import *

# URL of the YouTube video you want to download
video_url = input('Enter the YouTube video url/link: ')

# Resolution preference for download (e.g., "1080p", "720p", "480p", "360p", etc.)
preferred_resolution = '1080p'

try:
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the best quality stream for the preferred resolution
    stream = yt.streams.filter(progressive=True, file_extens