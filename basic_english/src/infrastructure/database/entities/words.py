from ..settings.base import Base
from sqlalchemy import Column, String, Integer, Boolean

class Words(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    formal = Column(Boolean, nullable=False)
    type_word = Column(String, nullable=False)

    def __repr__(self):
        return f"Words [(id={self.id}, word={self.word}, translation={self.translation}, formal={self.formal}, type_word={self.type_word})]"