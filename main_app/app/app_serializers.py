from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ValueInput(BaseModel):
    questions_num: int


class QuestionSchema(BaseModel):
    id: Optional[int]
    service_id: Optional[int]
    question_text: Optional[str]
    answer_text: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
