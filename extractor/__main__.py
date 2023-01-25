"""
__main__.py module makes it possible to run application as module like this: python -m extractor
"""

import sys
from pathlib import Path

# add extractor package path to sys.path
extractor_pkg_dir_path = str(Path(__file__).parent.resolve())
sys.path.insert(1, extractor_pkg_dir_path)

from extractor import main

if __name__ == "__main__":
    main()