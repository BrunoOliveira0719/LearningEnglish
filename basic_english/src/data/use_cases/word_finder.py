from http.client import BAD_REQUEST
from typing import Dict, List, Union
from xml.dom import NotFoundErr
from basic_english.src.domain.use_cases.word_finder import WordFinder as WordFinderInterface
from ..interfaces.words_repository import WordsRepositoryInterface
from basic_english.src.domain.models.words import Words
from basic_english.src.errors.types import HttpBadRequest, HttpNotFound

class WordFinder(WordFinderInterface):
    def __init__(self, words_repository: WordsRepositoryInterface) -> None:
        self.__words_repository = words_repository

    def find(self, word: str) -> Dict:
        words = self.__words_repository.read_specific_word(word)
        print(words)

        response = self.__validation_database(words)

        if self.__verification_error(response):
            print(self.__format_response_database(words))
            return self.__format_response_database(words)

        return {"Error": response}

    def find_all(self) -> Dict:
        words = self.__words_repository.read_all_words()
        print(words)

        if self.__validation_db_global(words):
            return self.__format_response_database(words, self.__validation_db_global(words))
        
        response = self.__validation_database(words)

        if self.__verification_error(response):
            print(self.__format_response_database(words))
            return self.__format_response_database(words)

        return {"Error": response}

    def find_all_type_word(self, type_word: str) -> Dict:
        type_words = self.__words_repository.read_all_type_words(type_word)
        print(type_words)

        response = self.__validation_database(type_words)

        if self.__verification_error(response):
            print(self.__format_response_database(type_words))
            return self.__format_response_database(type_words)

        return {"Error": response}

    @classmethod
    def __validation_database(cls, words: list) -> Union[HttpNotFound, HttpBadRequest, None]:
        if words == [] or isinstance(words, NotFoundErr):
            return HttpNotFound("Word not found.")
        
        if isinstance(words, Exception):
            if isinstance(words, BAD_REQUEST):
                return HttpBadRequest("Invalid word to search.")
            
            elif isinstance(words, NotFoundErr):
                return HttpBadRequest("Invalidate key word to search.")
            
    @classmethod        
    def __validation_db_global(cls, words: list) -> Union[HttpNotFound]:
        if words == []:
            return HttpNotFound("Database is empty.")

    @classmethod
    def __verification_error(cls, response) -> bool:
        return response == None

    @classmethod
    def __format_response_database(cls, words: List[Words]) -> Dict:
        attributes = []
        
        if isinstance(words, list):
            for word in words:
                attributes.append({"word": word.word, "translation": word.translation, "formal": word.formal, "type_word": word.type_word})
        else:
            attributes.append({"word": words.word, "translation": words.translation, "formal": words.formal, "type_word": words.type_word})

        return {"type": "words", "count": len(words), "attributes": attributes}