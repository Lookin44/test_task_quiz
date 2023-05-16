from .db_models import Question
from .db_settings import session


def question_exists(service_id) -> bool:
    question = session.query(Question).filter_by(service_id=service_id).first()
    return True if question else False


def get_last_question() -> Question:
    return session.query(Question).order_by(Question.id.desc()).first()


def set_question(
        service_id: int,
        answer_text: str,
        question_text: str,
        created_at: str
) -> None:
    question = Question(
        service_id=service_id,
        question_text=question_text,
        answer_text=answer_text,
        created_at=created_at,
    )
    session.add(question)
    session.commit()
