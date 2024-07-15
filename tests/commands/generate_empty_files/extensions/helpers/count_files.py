import os


def get_all_files(path_to_dir: str) -> list[str]:
    return [
        name for name in os.listdir(path_to_dir)
        if os.path.isfile(os.path.join(path_to_dir, name))]


def count_files(path_to_dir: str) -> int:
    return len(get_all_files(path_to_dir))


def count_files_per_ext(path_to_dir: str, ext: str):
    return len([name for name in get_all_files(path_to_dir) if name.endswith(ext)])
