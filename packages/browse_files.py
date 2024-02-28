from tkinter import filedialog
import os, shutil
from colorama import Fore

__all__ = ["browse_files", "browse_image"]


def browse_files(
    move_path: str = "target", /, move: bool = False, delete: bool = False
) -> tuple[str | None, list[str] | None, list[str] | None]:
    """Opens filedialog and let's user to select multiple files for archiving.

    Args:
        move_path (str, optional): Directory where the selected files are to be copied/moved. Defaults to "target".
        move (bool, optional): Specify weather to move or copy files. Defaults to False.

    Returns:
        tuple[str | None, list[str] | None, list[str] | None]: Returns (None, None, None)
            if user didn't select any files.
                If user select files,
                    returns path where files are copied or moved,
                    list of files with new path, and
                    list of files that encountered error when moving or copying.
    """
    files = filedialog.askopenfilenames()

    if len(files) == 0:
        return None, None, None
    os.makedirs(move_path, exist_ok=True)

    error_files: list[str] = []
    new_paths: list[str] = []
    for file in files:
        try:
            if move:
                shutil.move(file, move_path)
            else:
                shutil.copy(file, move_path)
            if delete:
                try:
                    os.remove(file)
                except:
                    print(f"{Fore.LIGHTRED_EX}Cannot delete file\n{file}")
            new_paths.append(os.path.join(move_path, os.path.basename(file)))
        except (shutil.Error, shutil.SameFileError, shutil.SpecialFileError, OSError):
            error_files.append(file)
    return move_path, new_paths, error_files


def browse_image() -> str | None:
    """Return images

    Returns:
        str | None: Path of the selected image
    """
    return filedialog.askopenfilename(
        defaultextension=("JPEG", "*.jpg"),
        filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")],
    )


if __name__ == "__main__":
    browse_files()
    print(browse_image())
