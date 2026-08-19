from pathlib import Path

target_dir = Path("test_folder")

def main():
    if not target_dir.exists():
        print ("Папки нет", target_dir)
        return

    for item in target_dir.iterdir():
        if item.is_file():
            print(item.name)

if __name__ == "__main__":
    main()