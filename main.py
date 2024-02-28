from packages import create_archive, browse_files, browse_image, clean
from colorama import Fore, init, Style
import os
import shutil


init(autoreset=True)
columns: int = os.get_terminal_size().columns
string: str = f"{Fore.CYAN}{Style.BRIGHT}File Merger"
print(f"\n{string:^{columns}}\n\n")

def main() -> None:
    while True:
        #? Loop controlling
        print(
            f"{Fore.LIGHTGREEN_EX}Do you want to continue? {Fore.LIGHTCYAN_EX}(yes/{Style.BRIGHT}No) → ",
            end="",
        )
        if not input().lower() in ["y", "yes"]:
            break

        #? Selecting Files for archival
        print(f"\n{Fore.LIGHTBLUE_EX}Select images for archiving", end="")
        archive_folder, files, error_files = browse_files()

        if not archive_folder:
            print(f"{Fore.LIGHTRED_EX}\nUser didn't select any files.")
            continue
        print(f" → x{len(files)}")
        if len(error_files) > 0:
            print(f"{Fore.RED}{Style.BRIGHT}Following files are not added to the archive")
            for file in error_files:
                print(f"{Fore.LIGHTRED_EX}{file}")

        if len(files) == 0:
            print(f"{Fore.LIGHTRED_EX}No files to archive.")
            continue

        #? Creating archive
        rar_archive_path, _ = create_archive(files)
        
        #? Selecting thumbnail
        print(
            f"{Fore.LIGHTBLUE_EX}Select thumbnail for the archive (None - Select automatically)", end=""
        )
        thumbnail = browse_image()
        if not thumbnail:
            thumbnail = max(files, key=lambda x: x.endswith(".jpg"))
            if not thumbnail.endswith(".jpg"):
                print(f"{Fore.LIGHTRED_EX} → No thumbnail selected\n")
                clean(archive_folder, rar_archive_path)
                continue
        shutil.copy(thumbnail, ".")
        thumbnail = os.path.basename(thumbnail)
        print(f" → {thumbnail}")

        #? Merging files
        new_image = "_output".join(os.path.splitext(thumbnail))
        with open(new_image, "wb") as output:
            with open(os.path.join(".", thumbnail), "rb") as image:
                with open(rar_archive_path, "rb") as file:
                    output.write(image.read())
                    output.write(file.read())
        print(
            f"{Fore.GREEN}{Style.BRIGHT}\nFiles merged successfully.\n{Fore.LIGHTGREEN_EX}{Style.NORMAL}\t{new_image}\n",
            end="\n",
        )
        clean(archive_folder, rar_archive_path, thumbnail)

if __name__ == "__main__":
    main()