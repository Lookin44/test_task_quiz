from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from .db_settings import engine


Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer)
    question_text = Column(String)
    answer_text = Column(String)
    created_at = Column(DateTime)


Base.metadata.create_all(engine)
