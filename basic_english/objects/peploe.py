from random import randint

import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from .utils.people_repository_inheritance import PeploeRepositoryInheritance

class Peploe(PeploeRepositoryInheritance):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def how_is_anyone_specific(self, visualization="phrase"):
        if self.verification_None_and_empty(visualization):
            return f"{self.__name} is speaking... {self.how_is_anyone_dict()[randint(1, 6)][visualization]}"
        return self.msg_none_or_empty(visualization)

    def how_is_anyone_all(self):
        return f"These are the phrases of the type how is anyone: \n{self.how_is_anyone_dict()}"

    def how_am_me_specific(self, visualization="phrase"):
        if self.verification_None_and_empty(visualization):
            return f"{self.__name} is speaking... {self.how_am_me_dict()[randint(1, 6)][visualization]}"
        return self.msg_none_or_empty(visualization)

    def how_am_me_all(self):
        return f"These are the phrases of the type how am me: \n{self.how_am_me_dict()}"

    def ask_job_specific(self, visualization="phrase"):
        if self.verification_None_and_empty(visualization):
            return f"{self.__name} is speaking... {self.ask_job_dict()[randint(1, 3)][visualization]}"
        return self.msg_none_or_empty(visualization)

    def ask_job_all(self):
        return f"These are the phrases of the type ask about the job: \n{self.ask_job_dict()}"