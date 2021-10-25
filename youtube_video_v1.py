# Video Downloader
# By @Bethu05
# v1.0

from pytube import YouTube

# video_url = YouTube('https://youtu.be/crYum29M-VE')
print('\tYoutube MP4 Video Downloader')
# Get Video Url from User


def get_video_id():
    # get User to Paste the video Url
    url = input('Paste The Video Url: ')
    video_url = YouTube(url)
    return video_url


def video_downloader(url, folder):  # ? Download Specific Video
    # Get The highest resolution with pregressive=True and .mp4 file extension
    highest_res = url.streams.filter(
        progressive=True, file_extension='mp4').get_highest_resolution()
    # Download the Highest Resolution to entered folder
    highest_res.download(output_path=f'Downloads/{folder}')


try:
    folder = input('Enter Folder Name: ')
    video_id = get_video_id()
    video_downloader(video_id, folder)
except Exception as e:
    print(e)
