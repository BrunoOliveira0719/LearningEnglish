from typing import Dict, List
from basic_english.src.domain.use_cases.phrase_insert import PhraseInsert as PhraseInsertInterface
from ..interfaces.phrases_repository import PhrasesRepositoryInterface

class PhraseInsert(PhraseInsertInterface):
    def __init__(self, phrases_repository: PhrasesRepositoryInterface) -> None:
        self.__phrases_repository = phrases_repository

    def insert(self, phrase: str = None, translation: str = None, formal: bool = None, type_phrase: str = None) -> Dict:
        self.__verification_insert(phrase)
        self.__verification_insert(translation)
        self.__verification_insert(formal)
        self.__verification_insert(type_phrase)
        
        self.__insert_phrase_information(phrase, translation, formal, type_phrase)

        return self.__format_response(phrase, translation, formal, type_phrase)

    def __insert_phrase_information(self, phrase: str, translation: str, formal: bool, type_phrase: str) -> None:
        self.__phrases_repository.insert_phrase(phrase, translation, formal, type_phrase)

    @classmethod
    def __verification_insert(cls, attribute) -> None:
        if attribute == None or attribute == " " :
            raise Exception("fill in all the fields")

    @classmethod
    def __format_response(cls, phrase: str = None, translation: str = None, formal: bool = None, type_phrase: str = None) -> Dict:
        return {"type": "Phrases", "count": 1, "attributes": {
            "phrase": phrase, "translation": translation, "formal": formal, "type_phrase": type_phrase
        }}