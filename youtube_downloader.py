# YouTube Video & MP3 Downloader
"""This Python script allows users to download YouTube videos in either
MP3 (audio only) or video format using yt-dlp. Simply enter the YouTube video URL
and choose whether to download the full video or extract the audio as an MP3.
The script ensures high-quality downloads and saves files with the original video title."""
# pip install yt-dlp
# pip install imagio[ffmpeg]

import yt_dlp

# function for downloading YouTube Video
def download_yt_video(url, output_path="."):
    """Download YouTube video in the best format."""
    ydl_opts = {
        'format': 'bestvideo[height<=480]+bestaudio/best',
        'noplaylist' : True,
        'merge_output_format': 'mp4',  #ensure proper merging
        'outtmpl': f"{output_path}/%(title)s.mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# function for downloading YouTube to MP3
def download_audio(url, output_path="."):
    """Download and convert YouTube video to MP3."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': f"{output_path}/%(title)s.mp3"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Usage
if __name__ == "__main__":
    choice = input("Do you want to download the Video or convert to AUDIO? (Type 'video' or 'mp3'): ").strip().lower()
    video_url = input("Enter the YouTube Video URL: ").strip()

    if choice == "mp3":
        download_audio(video_url)
    elif choice == "video":
        download_yt_video(video_url)
    else:
        print("Invalid choice. Please type 'video' or 'mp3'.")

