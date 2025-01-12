from typing import Dict, List
from basic_english.src.domain.use_cases.word_delete import WordDelete as WordDeleteInterface
from ..interfaces.words_repository import WordsRepositoryInterface
from basic_english.src.domain.models.words import Words

class WordDelete(WordDeleteInterface):
    def __init__(self, words_repository: WordsRepositoryInterface) -> None:
        self.__words_repository = words_repository

    def delete(self, word: str = None) -> Dict:
        self.__verification_delete(word)
        self.__words_repository.delete_word(word)

        return self.__format_response(word)

    
    @classmethod
    def __verification_delete(cls, words: list) -> None:
        if words == " " and words == None:
            raise Exception("Database is empty.")

    @classmethod
    def __format_response(cls, words: List[Words]) -> str:
        return f"Word: {words} deleted with success."