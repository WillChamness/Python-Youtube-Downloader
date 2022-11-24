import os
import sys

def get_downloads_folder():
    home = os.path.expanduser("~")
    downloads = os.path.join(home, "Downloads")
    return downloads

def create_folder(parent_dir, new_child_dir):
    if sys.platform == "win32":
        full_dir = parent_dir + "\\" + new_child_dir
    else:
        full_dir = parent_dir + "/" + new_child_dir
    os.mkdir(full_dir)
    return full_dir


if __name__ == "__main__":
    print(get_downloads_folder())