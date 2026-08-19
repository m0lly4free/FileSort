from pathlib import Path
import sys
from tkinter import Tk
from tkinter import filedialog

root = Tk()
root.withdraw()
fold_path = filedialog.askdirectory(title="Select a folder")

if not fold_path:
    print("Folder not selected")
    sys.exit()

print("Folder selected: ", fold_path)
folder_path = Path(fold_path)

CATEGORIES = {".jpg" : "Images",
              ".png" : "Images",

              ".mp4" : "Videos",

              ".pdf" : "Documents",
              ".txt" : "Documents",
              ".docx" : "Documents",
              ".xlsx" : "Documents",
              ".pptx" : "Documents",

              ".zip" : "Archives",
              ".rar" : "Archives",
              ".7z" : "Archives",
              
              ".flp" : "FL Projects",

              ".mp3" : "Music",
              ".wav" : "Music"
              }

def main():
    if not folder_path.exists():
        print("This folder does not exist", folder_path)
        return

    for item in folder_path.iterdir():
        if item.is_file():
            category = CATEGORIES.get(item.suffix.lower(), "Other")
            dest_dir = folder_path / category
            dest = dest_dir / item.name
            if dest.exists():
                print(item.name, " it's already in the folder ", category)
            else:
                dest_dir.mkdir(exist_ok=True)
                item.rename(dest)
           
if __name__ == "__main__":
    main()