from pathlib import Path
from typing import Optional
import sys
import os


ENV_GARAGE_HOME = 'GARAGE_HOME'
ENV_XDG_CACHE_HOME = 'XDG_CACHE_HOME'
DEFAULT_CACHE_DIR = '~/.cache'
GARAGE_TOKEN = "garage"
CODE_TOKEN = "code"
DATASETS_TOKEN = "datasets"
WORKSPACE_TOKEN = "workspace"
GOOGLE_CONTENT_DIR = "/content"



def in_collab() -> bool:
  '''Checks whether script is running in Google Colab'''

  return 'google.colab' in sys.modules


def get_garage_home()->Path:
    """garage home directory"""

    if in_collab():
       garage_home = Path(GOOGLE_CONTENT_DIR) / GARAGE_TOKEN
    else:    
      garage_home = os.path.expanduser(
          os.getenv(ENV_GARAGE_HOME,
            os.path.join(os.getenv(ENV_XDG_CACHE_HOME,
            DEFAULT_CACHE_DIR), GARAGE_TOKEN)))
      
    return Path(garage_home)



def get_garage_code_dir( code_name : Optional[str] = None ) -> Path:
    """directory in which to put external code"""

    code_dir = get_garage_home( ) / CODE_TOKEN
    if code_name:
       code_dir = code_dir / code_name
      
    return code_dir



def get_garage_datasets_dir( dataset_name : Optional[str] = None ) -> Path:
    """directory in which to put datasets"""

    dataset_dir = get_garage_home( ) / DATASETS_TOKEN
    if dataset_name:
       dataset_dir = dataset_dir / dataset_name
      
    return dataset_dir



def get_garage_workspace_dir( workspace_name : Optional[str] = None ) -> Path:
    """directory in which to put datasets"""

    workspace_dir = get_garage_home( ) / WORKSPACE_TOKEN
    if workspace_name:
       workspace_dir = workspace_dir / workspace_name
      
    return workspace_dir



def create_experiment_dir(workspace_dir: os.PathLike, experiment_name: str, exist_ok=True) -> Path:
  """Creates Experiment Directory in Workspace"""

  experiment_dir = Path(workspace_dir) / experiment_name
  experiment_dir.mkdir(parents=True, exist_ok=exist_ok)

  return experiment_dir