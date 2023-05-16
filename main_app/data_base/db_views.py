from main_app.data_base.db_models import Question

from .db_settings import session


def get_question(question_id: int) -> Question:
    question = session.query(Question).get(question_id)
    return question


def set_question(question_text: str, answer_text: str) -> Question:
    question = Question(question_text=question_text, answer_text=answer_text)
    session.add(question)
    session.commit()
    return question
