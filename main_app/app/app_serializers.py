from pydantic import BaseModel


class ValueInput(BaseModel):
    questions_num: int
