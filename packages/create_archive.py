import zipfile
import datetime
import os

__all__ = ["create_archive"]


def create_archive(
    files: list[str], /, zip_path: str = ".", password: str | None = None
) -> tuple[str, str]:
    """Create a archive of files

    Args:
        files (list[str]): List of files to add to archive
        zip_path (str, optional): Path where the archive is to be created. Defaults to ".".
        password (str | None, optional): Password to add to archive. Defaults to None.

    Returns:
        tuple[str, str]: Path where archive is created and archive name.
    """
    now = datetime.datetime.now()
    archive_name = f"{now:%Y%m%d_%w_%I%M%S_%f%j}.rar"
    zip_file_path = os.path.join(zip_path, archive_name)
    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        for file in files:
            zip_file.write(file)
    return zip_file_path, archive_name


if __name__ == "__main__":
    create_archive([])
