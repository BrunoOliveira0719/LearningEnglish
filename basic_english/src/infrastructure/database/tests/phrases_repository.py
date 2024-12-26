from ....domain.models.phrases import Phrases
from typing import List

class PhrasesRepositorySpy:

    def __init__(self) -> None:
        self.insert_phrase_attributes = {}
        self.select_phrase_attributes = {}

    def insert_phrase(self, phrase: str, translation: str, formal: bool) -> None:
        self.insert_phrase_attributes["phrase"] = phrase
        self.insert_phrase_attributes["translation"] = translation
        self.insert_phrase_attributes["formal"] = formal

    def read_specific_phrase(self, phrase: str) -> List[Phrases]:
        self.select_phrase_attributes["phrase"] = phrase

        return [Phrases(1, phrase, "translation", False)
                ,Phrases(2, phrase, "translation2", False)
                ,Phrases(3, phrase, "translation3", False)]  
            
    def read_all_phrases(self) -> List[Phrases]:
        return [Phrases(4, "phrase4", "translation4", False)
                ,Phrases(5, "phrase5", "translation5", False)
                ,Phrases(6, "phrase6", "translation6", False)]  
    
    def update_phrase(self, phrase_corrent: str, json: dict) -> None: pass

    def delete_phrase(self, phrase: str) -> None: pass