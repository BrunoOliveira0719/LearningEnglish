from typing import Dict, List
from basic_english.src.domain.use_cases.phrase_update import PhraseUpdate as PhraseUpdateInterface
from ..interfaces.phrases_repository import PhrasesRepositoryInterface
from basic_english.src.domain.models.phrases import Phrases

class PhraseUpdate(PhraseUpdateInterface):
    def __init__(self, phrases_repository: PhrasesRepositoryInterface) -> None:
        self.__phrases_repository = phrases_repository

    def update(self, phrase_corrent: str = None, phrase: str = None, translation: str = None, formal: bool = None) -> Dict:
        json = self.__verification_update(phrase, translation, formal)

        self.__update_phrase_information(phrase_corrent, json)

        return self.__format_response(phrase_corrent, json)

    def __update_phrase_information(self, phrase_courrent: str, json: Dict) -> None:
        self.__phrases_repository.update_phrase(phrase_courrent, json)

    @classmethod
    def __verification_update(cls, phrase: str = None, translation: str = None, formal: bool = None) -> Dict:
        if phrase != None and phrase != " " and translation != None and translation != " " and formal != None and formal != " ":
            json = {"phrase": phrase, "translation": translation, "formal": formal}

        elif phrase != None and phrase != " " and translation != None and translation != " ":
            json = {"phrase": phrase, "translation": translation}

        elif phrase != None and phrase != " " and formal != None and formal != " ":
            json = {"phrase": phrase, "formal": formal}

        elif translation != None and translation != " " and formal != None and formal != " ":
            json = {"translation": translation, "formal": formal}

        elif phrase != None and phrase != " ":
            json = {"phrase": phrase}

        elif translation != None and translation != " ":
            json = {"translation": translation}

        elif formal != None and formal != " ":
            json = {"formal": formal}

        return json

    @classmethod
    def __format_response(cls, phrase: str, json) -> Dict:
        return {"Phrase": f"{phrase} updated", "phrase_current": json}