# Inspired by: Dario Radečić on Medium
import pathlib


def cwd():
    """Get a path to the current working directory"""
    return pathlib.Path.cwd()


def pwd(index=0):
    """Get a parent folder path, Default is first(0).\n Count up for each parent higher (Index=1, 2, etc...)"""
    return pathlib.Path.cwd().parents[index]


def combine_parent_path_to_file(parent_index, filename):  # name need to be shortened
    """Join a dynamic parent path to a file"""
    path = pwd(parent_index)
    return path.joinpath(filename)


def create_folder(folder):
    path = pathlib.Path.cwd().joinpath(folder)
    if not path.exists():
        path.mkdir()


