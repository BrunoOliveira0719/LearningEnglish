from ast import Return
from typing import Dict
from basic_english.src.domain.use_cases.word_insert import WordInsert as WordInsertInterface
from ..interfaces.words_repository import WordsRepositoryInterface

class WordInsert(WordInsertInterface):
    def __init__(self, words_repository: WordsRepositoryInterface) -> None:
        self.__words_repository = words_repository

    def insert(self, word: str = None, translation: str = None, formal: bool = None, type_word: str = None) -> Dict:
        self.__verification_word(word)
        self.__verification_insert(translation)
        self.__verification_insert(formal)
        self.__verification_insert(type_word)
        
        self.__insert_word_information(word, translation, formal, type_word)

        return self.__format_response(word, translation, formal, type_word)

    def __insert_word_information(self, word: str, translation: str, formal: bool, type_word: str) -> None:
        self.__words_repository.insert_word(word, translation, formal, type_word)

    @classmethod
    def __verification_insert(cls, attribute) -> None:
        if attribute == None or attribute == " " :
            raise Exception("fill in all the fields")

    @classmethod
    def __verification_word(cls, attribute) -> None:
        for char in attribute:
            if char == " " or char.isalpha() or attribute == None:
                raise Exception("The word cannot contain spaces!")

    @classmethod
    def __format_response(cls, word: str = None, translation: str = None, formal: bool = None, type_word: str = None) -> Dict:
        return {"type": "Words", "count": 1, "attributes": {
            "word": word, "translation": translation, "formal": formal, "type_word": type_word
        }}