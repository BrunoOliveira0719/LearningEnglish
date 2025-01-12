from typing import Dict
from basic_english.src.domain.use_cases.word_update import WordUpdate as WordUpdateInterface
from ..interfaces.words_repository import WordsRepositoryInterface
from basic_english.src.domain.models.words import Words

class WordUpdate(WordUpdateInterface):
    def __init__(self, words_repository: WordsRepositoryInterface) -> None:
        self.__words_repository = words_repository

    def update(self, word_corrent: str = None, word: str = None, translation: str = None, formal: bool = None, type_word: str = None) -> Dict:
        json = self.__verification_update(word, translation, formal, type_word)

        self.__update_word_information(word_corrent, json)

        return self.__format_response(word_corrent, json)

    def __update_word_information(self, word_courrent: str, json: Dict) -> None:
        self.__words_repository.update_word(word_courrent, json)

    @classmethod
    def __verification_update(cls, word: str = None, translation: str = None, formal: bool = None, type_word: str = None) -> Dict:
        if word != None and word != " " and translation != None and translation != " " and formal != None and formal != " " and type_word != None and type_word != " ":
            json = {"word": word, "translation": translation, "formal": formal, "type_word": type_word}

        elif word != None and word != " " and translation != None and translation != " " and type_word != None and type_word != " ":
            json = {"word": word, "translation": translation, "type_word": type_word}

        elif word != None and word != " " and formal != None and formal != " " and type_word != None and type_word != " ":
            json = {"word": word, "formal": formal, "type_word": type_word}

        elif translation != None and translation != " " and formal != None and formal != " " and type_word != None and type_word != " ":
            json = {"translation": translation, "formal": formal, "type_word": type_word}

        elif word != None and word != " " and formal != None and formal != " " and translation != None and translation != " ":
            json = {"word": word, "formal": formal, "translation": translation}

        elif word != None and word != " " and translation != None and translation != " ":
            json = {"word": word, "translation": translation}

        elif word != None and word != " " and formal != None and formal != " ":
            json = {"word": word, "formal": formal}

        elif word != None and word != " " and type_word != None and type_word != " ":
            json = {"word": word, "type_word": type_word}

        elif translation != None and translation != " " and formal != None and formal != " ":
            json = {"translation": translation, "formal": formal}

        elif translation != None and translation != " " and type_word != None and type_word != " ":
            json = {"translation": translation, "type_word": type_word}

        elif formal != None and formal != " " and type_word != None and type_word != " ":
            json = {"formal": formal, "type_word": type_word}

        elif word != None and word != " ":
            json = {"word": word}

        elif translation != None and translation != " ":
            json = {"translation": translation}

        elif formal != None and formal != " ":
            json = {"formal": formal}

        elif type_word != None and type_word != " ":
            json = {"type_word": type_word}

        return json

    @classmethod
    def __format_response(cls, word: str, json) -> Dict:
        return {"word": f"{word} updated", "word_current": json}