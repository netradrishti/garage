from pathlib import Path
import inspect
import os, sys

from configparser import ConfigParser

__all__ = [
    "get_project_root",
    "add_project_root_syspath",
    "read_project_conf",
]

def get_project_root()->os.PathLike | None:
    """returns root directory of the project """

    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    path = Path(module.__file__).parent.resolve()

    while path.parent != path:
        pconf = path / "project.conf"
        if pconf.exists():
            return str(path)
        path = path.parent
    
    return None



def add_project_root_syspath()->os.PathLike:
    """adds project root to system path"""

    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    path = Path(module.__file__).parent.resolve()

    project_root = None

    while path.parent != path:
        pconf = path / "project.conf"
        if pconf.exists():
            project_root = str(path)
            break
        path = path.parent
    
    if project_root:
        sys.path.insert(1, project_root)

    return project_root


def read_project_conf(project_conf: str | None = None) -> dict | None:
    
    if project_conf is None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])

        path = Path(module.__file__).parent.resolve()

        project_conf = None

        while path.parent != path:
            pconf = path / "project.conf"
            if pconf.exists():
                project_conf = str(pconf)
                break
            path = path.parent
    
    
    if project_conf:
        conf = ConfigParser()
        conf.read(project_conf)
        if "project" in conf:
            return dict(conf["project"])
    return None