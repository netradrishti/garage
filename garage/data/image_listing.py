import os
from typing import Dict, List, Optional, Set, Tuple, Union

from ..utils.misc import natural_key
from .readers import get_img_extensions


__all__ = ["find_images"]

def find_images(
        folder: str,
        types: Optional[Union[List, Tuple, Set]] = None,
        sort: bool = True
):
    """ Walk folder recursively to discover images.

    Args:
        folder: root of folder to recrusively search
        types: types (file extensions) to search for in path
        sort: re-sort found images by name (for consistent ordering)

    Returns:
        A list of images
    """
    types = get_img_extensions(as_set=True) if not types else set(types)

    filenames = []

    for root, subdirs, files in os.walk(folder, topdown=False, followlinks=True):

        for f in files:
            base, ext = os.path.splitext(f)
            if ext.lower() in types:
                filenames.append(os.path.join(root, f))

    image_files = filenames
    if sort:
        image_files = sorted(image_files, key=lambda k: natural_key(k[0]))
    return image_files