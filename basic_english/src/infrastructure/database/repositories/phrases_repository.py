from ..entities.phrases import Phrases
from ..settings.connection import DBConnetionHandler
from basic_english.src.data.interfaces.phrases_repository import PhrasesRepositoryInterface
from ..entities.phrases import Phrases
from typing import List

class PhrasesRepository(PhrasesRepositoryInterface):
    @classmethod
    def insert_phrase(cls, phrase: str, translation: str, formal: bool, type_phrase: str) -> None:
        with DBConnetionHandler() as database:
            try:
                new_resgistry = Phrases(phrase=phrase, translation=translation, formal=formal, type_phrase=type_phrase)
                database.session.add(new_resgistry)
                database.session.commit()
                return True

            except Exception as exception:
                database.session.rollback()
                return exception
    
    @classmethod
    def read_specific_phrase(cls, phrase: str) -> List[Phrases]:
        with DBConnetionHandler() as database:
            try:
                return database.session.query(Phrases).filter_by(phrase=phrase).all()
                return True

            except Exception as exception:
                database.session.rollback()
                return exception
            
    @classmethod
    def read_all_phrases(cls) -> List[Phrases]:
        with DBConnetionHandler() as database:
            try:
                return database.session.query(Phrases).all()
                return True

            except Exception as exception:
                database.session.rollback()
                return exception
            
    @classmethod
    def update_phrase(cls, phrase_corrent: str, json: dict) -> None:
        with DBConnetionHandler() as database:
            try:
                database.session.query(Phrases).filter_by(phrase=phrase_corrent).update(json)
                database.session.commit()
                return True

            except Exception as exception:
                database.session.rollback()
                return exception

    @classmethod
    def delete_phrase(cls, phrase: str) -> bool:
        with DBConnetionHandler() as database:
            try:
                database.session.query(Phrases).filter_by(phrase=phrase).delete()
                database.session.commit()
                return True

            except Exception as exception:
                database.session.rollback()
                return exception

