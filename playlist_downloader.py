from pytube import Playlist 
import os
import directories

def start():
    playlist = prompt_playlist()
    title = prompt_title()
    playlist_target = prompt_save_location(title)
    mp4 = prompt_mp4()
    start, stop = prompt_range(playlist)

    print("\nNumber of videos:", 1 + stop - start)
    counter = 0
    current_video = 1
    for video in playlist.videos:
        if current_video < start:
            current_video += 1
            continue
        if current_video > stop:
            break

        if mp4:
            video.streams.get_highest_resolution().download(playlist_target)
        else:
            audio = video.streams.filter(only_audio=True).first().download(output_path = playlist_target)
            base, ext = os.path.splitext(audio)
            os.rename(audio, base + ".mp3")
        counter += 1
        if counter == 1:
            print("Downloaded 1 video")
        else:
            print("Downloaded", counter, "videos")
        current_video += 1
    
    print("\n")



def prompt_playlist():
    url = input("Youtube Playlist URL: ")
    return Playlist(url)

def prompt_title(): 
    title = input("Title of playlist [playlist]: ")
    if title == "":
        title = "playlist"
    return title

def prompt_save_location(title):
    save_folder = input(f"Save location [{directories.get_downloads_folder()}]: ")
    if save_folder == "":
        save_folder = directories.get_downloads_folder()
    playlist_location = directories.create_folder(save_folder, title)
    return playlist_location

def prompt_range(playlist): 
    playlist_size = len(playlist.video_urls)
    range = input(f"Enter range in playlist (separated by comma, no space, both enpoints inclusive) [1,{playlist_size}]: ")
    if range == "":
        start = 1
        stop = playlist_size
    else:
        range = range.split(",")
        start = int(range[0])
        stop = int(range[1])
    return (start, stop)

def prompt_mp4():
    choice = ""
    while choice != "y" and choice != "n":
        choice = input("Download as mp4? [Y/n]: ").lower()
        if choice == "":
            choice = "y"
    
    return choice == "y"
