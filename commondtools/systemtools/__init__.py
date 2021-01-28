import sys
from typing import List

from .beeper import *
from .environment import *

if sys.platform != "win32":
    def non_win_method() -> List[int]: ...
