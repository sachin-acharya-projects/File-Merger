import shutil
import os

__all__ = ["clean"]


def clean(target_folder: str, archive_name: str, image: str | None = None) -> None | str:
    """Clean aftermath of the merging process

    Args:
        target_folder (str): Folder where all the archived images were copied.
        archive_name (str): Name of the archive.
        image (str): Thumbnail

    Returns:
        None | str: None when successfully clean and string when error occured. String is the error message.
    """
    try:
        shutil.rmtree(target_folder)
        os.remove(archive_name)
        if image:
            os.remove(image)

        return None
    except Exception as e:
        return str(e)
