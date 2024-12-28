from ..settings.base import Base
from sqlalchemy import Column, String, Integer, Boolean

class Phrases(Base):
    __tablename__ = "phrases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phrase = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    formal = Column(Boolean, nullable=False)
    type_phrase = Column(String, nullable=False)

    def __repr__(self):
        return f"Phrases [(id={self.id}, phrase={self.phrase}, translation={self.translation}, formal={self.formal}, type_phrase={self.type_phrase})]"