import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def extract_audio_from_youtube(link):
    yt = YouTube(link)
    stream = yt.streams.filter(only_audio=True).first()
    audio_file = stream.download(filename='temp')
    return audio_file

def extract_audio_from_video(video_file):
    video = VideoFileClip(video_file)
    audio_file = video.audio.write_audiofile('output.mp3')
    return audio_file

def main():
    print("Choose an option:")
    print("1. Download audio from YouTube")
    print("2. Upload a video file")

    choice = input("Enter your choice: ")

    if choice == '1':
        youtube_link = input("Enter the YouTube video link: ")
        audio_file = extract_audio_from_youtube(youtube_link)
        print("Audio extracted and saved as mp3 file.")
        # Move the audio file to the downloads folder
        downloads_folder = os.path.expanduser('~/Downloads')
        os.rename(audio_file, os.path.join(downloads_folder, 'output.mp3'))
    elif choice == '2':
        video_file_path = input("Enter the path to the video file: ")
        audio_file = extract_audio_from_video(video_file_path)
        print("Audio extracted and saved as mp3 file.")
        # Move the audio file to the downloads folder
        downloads_folder = os.path.expanduser('~/Downloads')
        os.rename('output.mp3', os.path.join(downloads_folder, 'output.mp3'))
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
