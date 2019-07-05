import os
import re


class ProjectUtils(object):
    "Project Utilities"

    __root_folder__ = None

    @classmethod
    def get_project_root(cls):
        '''
        Return path of the project directory.
        '''
        if (cls.__root_folder__ != None):
            return cls.__root_folder__

        # path = os.getcwd()
        path = os.path.dirname(os.path.dirname(__file__))
        seperator_matches = re.finditer("/|\\\\", path)

        paths_to_search = [path]
        for match in seperator_matches:
            p = path[:match.start()]
            paths_to_search.insert(0, p)

        for path in paths_to_search:
            if os.path.isfile("{0}/.wtf_root_folder".format(path)):
                cls.__root_folder__ = path + "/"
                return cls.__root_folder__

        raise RuntimeError("Missing root project folder locator file '.wtf_root_folder'." \
                           + "Check to make sure this file is located in your project directory.")
