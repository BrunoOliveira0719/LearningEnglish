from urllib import response

from flask.config import T
from ..entities.words import Words
from ..settings.connection import DBConnetionHandler
from basic_english.src.data.interfaces.words_repository import WordsRepositoryInterface
from typing import List

class WordsRepository(WordsRepositoryInterface):
    @classmethod
    def insert_word(cls, word: str, translation: str, formal: bool, type_word: str) -> None:
        with DBConnetionHandler() as database:
            try:
                new_resgistry = Words(word=word, translation=translation, formal=formal, type_word=type_word)
                database.session.add(new_resgistry)
                database.session.commit()
                return True

            except Exception as exception:
                database.session.rollback()
                return exception
    
    @classmethod
    def read_specific_word(cls, word: str) -> List[Words]:
        with DBConnetionHandler() as database:
            try:
                return database.session.query(Words).filter_by(word=word).all()

            except Exception as exception:
                database.session.rollback()
                return exception
            
    @classmethod
    def read_all_words(cls) -> List[Words]:
        with DBConnetionHandler() as database:
            try:
                return database.session.query(Words).all()

            except Exception as exception:
                database.session.rollback()
                return exception
    
    @classmethod
    def read_all_type_words(cls, type_word: str) -> List[Words]:
        with DBConnetionHandler() as database:
            try:
                response = database.session.query(Words).filter_by(type_word=type_word).all()
                return response

            except Exception as exception:
                database.session.rollback()
                return exception
            
    @classmethod
    def update_word(cls, word_corrent: str, json: dict) -> None:
        with DBConnetionHandler() as database:
            try:
                database.session.query(Words).filter_by(word=word_corrent).update(json)
                database.session.commit()
                return True

            except Exception as exception:
                database.session.rollback()
                return exception

    @classmethod
    def delete_word(cls, word: str) -> bool:
        with DBConnetionHandler() as database:
            try:
                database.session.query(Words).filter_by(word=word).delete()
                database.session.commit()
                return True

            except Exception as exception:
                database.session.rollback()
                return exception