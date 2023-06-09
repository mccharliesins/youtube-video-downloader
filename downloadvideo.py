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
    stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=preferred_resolution).first()

    # If the preferred resolution is not available, get the highest available quality
    if not stream:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Download the video
    stream.download()
    print('Download completed!')

except (VideoUnavailable, PytubeError) as e:
    print('Error: Failed to download the YouTube video.')
    print(e)

#Find more cool stuffs:~
##MY SOCIALS:
###GITHUB PROFILE: https://github.com/mccharliesins
###INSTAGRAM: https://instagram.com/itsmccharliesins
###LINKEDIN: https://www.linkedin.com/in/mccharliesins/