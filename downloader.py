import video_downloader
import playlist_downloader
import os

def print_menu():
    print("1.) Video downloader")
    print("2.) Playlist downloader")
    print("0.) Stop")

def main():
    choice = -1
    while choice != 0:
        print_menu()
        choice = int(input(">> "))
        os.system("cls || clear")
        if choice == 0:
            print("Stopping...")
        elif choice == 1:
            video_downloader.start()
        elif choice == 2:
            playlist_downloader.start()
        else:
            print("Bad input")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        os.system("pause || read -rsp 'Press any key to continue...\n' -n 1")
        