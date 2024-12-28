from http.client import BAD_REQUEST
from typing import Dict, List, Union
from xml.dom import NotFoundErr
from basic_english.src.domain.use_cases.phrase_finder import PhraseFinder as PhraseFinderInterface
from ..interfaces.phrases_repository import PhrasesRepositoryInterface
from basic_english.src.domain.models.phrases import Phrases
from basic_english.src.errors.types import HttpBadRequest, HttpNotFound

class PhraseFinder(PhraseFinderInterface):
    def __init__(self, phrases_repository: PhrasesRepositoryInterface) -> None:
        self.__phrases_repository = phrases_repository

    def find(self, phrase: str) -> Dict:
        phrases = self.__phrases_repository.read_specific_phrase(phrase)

        response = self.__validation_database(phrases)

        if self.__verification_error(response):
            return self.__format_response_database(phrases)

        return {"Error": response}

    def find_all(self) -> List:
        phrases = self.__phrases_repository.read_all_phrases()

        response = self.__validation_database(phrases)

        if self.__verification_error(response):
            return self.__format_response_database(phrases)

        return List[response]

    @classmethod
    def __validation_database(cls, phrases: list) -> Union[HttpNotFound, HttpBadRequest, None]:
        if phrases == [] or isinstance(phrases, NotFoundErr):
            return HttpNotFound("Phrase not found.")
        
        if isinstance(phrases, Exception):
            if isinstance(phrases, BAD_REQUEST):
                return HttpBadRequest("Invalid phrase to search.")
            
            elif isinstance(phrases, NotFoundErr):
                return HttpBadRequest("Invalidate key phrase to search.")

    @classmethod
    def __verification_error(cls, response) -> bool:
        if response == None:
            return True

        return False 

    @classmethod
    def __format_response_database(cls, phrases: List[Phrases], attributes: list = []) -> Dict:
        if isinstance(phrases, list):
            for phrase in phrases:
                attributes.append({"phrase": phrase.phrase, "translation": phrase.translation, "formal": phrase.formal, "type_phrase": phrase.type_phrase})
        else:
            attributes.append({"phrase": phrases.phrase, "translation": phrases.translation, "formal": phrases.formal, "type_phrase": phrases.type_phrase})

        return {"type": "Phrases", "count": len(phrases), "attributes": attributes}