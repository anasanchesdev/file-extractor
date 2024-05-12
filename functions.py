import zipfile


def extract_archive(archive_path, dest_dir):
    """
    :param archive_path: archive to be extracted
    :param dest_dir: destination directory
    """
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == '__main__':
    extract_archive('files/to-decompress.zip', 'files')