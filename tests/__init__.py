import os
import sys

# we need this, so imports are working correctly inside tests
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)


from .state_tests import GameTests
from .board_tests import BoardTests
