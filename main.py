from pathlib import Path

target_dir = Path("test_folder")
categories = {".jpg" : "Images",
              ".png" : "Images",
              ".pdf" : "Documents",
              ".txt" : "Documents",
              ".docx" : "Documents",
              ".xlsx" : "Documents",
              ".pptx" : "Documents",
              ".zip" : "Archives",
              ".rar" : "Archives",
              ".flp" : "FL Projects",
              ".mp3" : "Music",
              ".wav" : "Music"
              }


def main():
    if not target_dir.exists():
        print("Такой папки не существует", target_dir)
        return

    for item in target_dir.iterdir():
        if item.is_file():
            category = categories.get(item.suffix.lower(), "Other")
            dest_dir = target_dir / category
            dest_dir.mkdir(exist_ok=True)
            item.rename(dest_dir / item.name)

if __name__ == "__main__":
    main()