import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from phrases.how_is_anyone import HowIsAnyone
from phrases.how_am_me import HowAmMe
from phrases.ask_job import AskJob
from .utils_peploe import UtilsPeploe
from .msg_error_and_sucess import Error

class PeploeRepositoryInheritance(HowIsAnyone, HowAmMe, AskJob, UtilsPeploe, Error):
    def __init__(self):
        pass