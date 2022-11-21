import directories
from pytube import YouTube
import os


def start():
    video = prompt_video()
    title = video.title
    save_folder = prompt_save_location()
    mp4 = prompt_mp4()
    print("Downloading:", title)
    if mp4:
        video.streams.get_highest_resolution().download(save_folder)
    else:
        audio = video.streams.filer(only_audio=True).first().download(output_path=save_folder)
        base, ext = os.path.splitext(audio)
        os.rename(audio, base + ".mp3")

    print("\n")


def prompt_video():
    url = input("Youtube video URL: ")
    return YouTube(url)

def prompt_save_location():
    save_folder = input(f"Save location [{directories.get_downloads_folder()}]: ")
    if save_folder == "":
        save_folder = directories.get_downloads_folder()
    return save_folder

def prompt_mp4():
    choice = ""
    while choice != "y" and choice != "n":
        choice = input("Download as mp4? [Y/n]: ").lower()
        if choice == "":
            choice = "y"
    
    return choice == "y"

