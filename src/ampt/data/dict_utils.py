import os
import json


class JSONDict(dict):
    def __init__(self, fp, *args, **kwargs):
        super(JSONDict, self).__init__(*args, **kwargs)
        self.fp = fp
        if path.exists(fp):
            with open(self.fp) as fp:
                data = json.load(fp)
            self.update(data)

    def __getattr__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        super(JSONDict, self).__setitem__(key, value)
        self.__update_json__()

    def __delitem__(self, key):
        super(JSONDict, self).__delitem__(key)
        self.__update_json__()

    def clear(self):
        super(JSONDict, self).clear()
        self.__update_json__()

    def update(self, other):
        super(JSONDict, self).update(other)
        self.__update_json__()

    def __update_json__(self):
        with open(self.fp, "w") as fp:
            json.dump(self, fp, sort_keys=True, indent=4)


def find_key(dict_, key_):
    """
    :param dict_: dict() - dictionary to search
    :param key_: str() - key to find
    :return: list() - [ (<key>, <value>), (<key>, <value>), ...]
    """

    if not isinstance(dict_, dict):
        raise TypeError('%s is not a dict()' % dict_)

    if not isinstance(key_, str):
        raise TypeError('%s is not a str()' % key_)

    stack = list()

    for k in dict_:
        # inspect the k for equality
        if k == key_:
            stack.append((k, dict_[k]))

        # inspect the key as a nested dictionary
        if isinstance(dict_[k], dict):
            nested_stack = find_key(dict_[k], key_)
            if len(nested_stack):
                stack.extend(nested_stack)

        # inspect the key as a list for nested dictionaries
        if isinstance(dict_[k], list):
            for i in dict_[k]:
                if isinstance(i, dict):
                    nested_stack = find_key(i, key_)
                    if len(nested_stack):
                        stack.extend(nested_stack)

    return stack

def directory_to_dict(path):
    dir = {}
    path = path.rstrip(os.sep)
    start = path.rfind(os.sep) + 1
    for path, dirs, files in os.walk(path):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir