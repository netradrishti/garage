from pathlib import Path
from typing import Optional
import sys
import os

def in_collab() -> bool:
  return 'google.colab' in sys.modules


def get_garage_dir(create : bool = True) -> Path:
  
  garage_dir = None
  
  if 'XDG_CACHE_HOME' in os.environ:
    garage_dir = Path(os.environ['XDG_CACHE_HOME'])/"garage"
  elif not in_collab():
    garage_dir = Path.home() / "garage"
  else:
    garage_dir = Path("/content") / "garage"
  
  if garage_dir:
     garage_dir.mkdir(exist_ok=True)
  
  return garage_dir
  

def get_garage_code_dir(subdir : str) -> Path:
    return get_garage_dir( ) / subdir/ "code"


def get_garage_datasets_dir(subdir : str) -> Path:
    return str(get_garage_dir( ) / subdir / "datasets")


def get_create_garage_workspace_dir(project: str, experiment: str, exist_ok=True) -> Path:
  """Creates Workspace Directory in Garage"""

  root_workspace = workspace_dir = Path(get_garage_dir( ) / "workspace")
  root_workspace.mkdir(exist_ok=True)

  project_dir = root_workspace / project
  project_dir.mkdir(exist_ok=True)

  workspace_dir = project_dir / experiment
  workspace_dir.mkdir(exist_ok=exist_ok)

  return workspace_dir