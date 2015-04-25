#!/usr/bin/python

# standard libraries
import os


def clean_path(path):
    """
    Replace backslash elements to comply with cross platform path formats
    :param path: a system file path as a string()
    :return: a valid system path as a string()
    """
    return os.path.abspath(path).replace("\\", "/")


def get_extension(path):
    """
    Get the extension characters from a system file name (excluding the period)
    :param path: a valid system path as a string()
    :return: a valid system file extension index as a string()
    """
    return os.path.splitext(path)[1][1:]


def is_dir(root, path):
    """
    Validate the combined system path strings as a directory
    :param root: a valid system path as a string()
    :param path: a valid system path as a string()
    :return: True if the combined paths are a valid system directory, otherwise False
    """
    return True if os.path.isdir(os.path.join(root, path)) else False


def is_file(root, path):
    """
    Validate the combined system paths strings as a file
    :param root: a valid system path as a string()
    :param path: a valid system path as a string()
    :return: True if the combined paths are a valid system file path, otherwise False
    """
    return True if os.path.isfile(os.path.join(root, path)) else False


def has_extension(path, file_extension):
    """
    Validate that the system path file extension matches the given extension
    :param path: a valid system path as a string()
    :param file_extension: a valid system file extension
    :return: True if the extension of the given path matches the given extension, otherwise False
    """
    return True if get_extension(path) == file_extension else False


def get_files(root, file_extension=None, recursive=False, full_path=False, stdout=False):
    """

    :param root: a valid system path as a string()
    :param file_extension: a valid system file extension
    :param recursive: Will the function search deeper than one level for files? True/False
    :param full_path: Will the function output the full path of the files? True/False
    :param output: print results in std::out? True/False
    :return: returns a list of files. (Default:returns only file name and extension. see full_path param)
    """

    def out(data):
        for i in data: print i
        print "Found %s files." % len(data)

    if len(root):
        root = clean_path(root)
        directories = [d for d in os.listdir(root) if is_dir(root, d)]
        if file_extension:
            if full_path:
                files = [clean_path(os.path.abspath(os.path.join(root, f))) for f in os.listdir(root) if
                         is_file(root, f) and has_extension(f, file_extension)]
            else:
                files = [f for f in os.listdir(root) if is_file(root, f) and has_extension(f, file_extension)]
        else:
            if full_path:
                files = [clean_path(os.path.abspath(os.path.join(root, f))) for f in os.listdir(root) if
                         is_file(root, f)]
            else:
                files = [f for f in os.listdir(root) if is_file(root, f)]

        if len(directories) and recursive:
            more_files = [get_files(os.path.join(root, d), file_extension, recursive, full_path) for d in directories]
            if len(more_files):
                for chunk in more_files:
                    files.extend(chunk)
        output = [clean_path(p) for p in files]
        if stdout:
            out(output)
        return output
    return None


def module_path(path):
    return clean_path(path) if os.path.exists(clean_path(path)) else None