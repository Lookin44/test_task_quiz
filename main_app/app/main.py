from typing import Optional, Dict, Any

from fastapi.responses import JSONResponse
from fastapi import FastAPI
from requests import get

from data_base.db_serializers import ValueInput, QuestionSchema
from data_base.db_views import set_question, get_last_question, question_exists


app = FastAPI()


def get_unique_question() -> Optional[Dict[str, Any]]:
    url = 'https://jservice.io/api/random?count=1'
    data = get(url).json()
    for item in data:
        service_id = item.get('id')
        if question_exists(service_id):
            return get_unique_question()
        return item


@app.post('/question', response_model=QuestionSchema)
async def main_page(value: ValueInput):
    url = f'https://jservice.io/api/random?count={value.questions_num}'
    last_question = get_last_question()
    data = get(url).json()
    for item in data:
        service_id = item.get('id')
        question_text = item.get('question')
        answer_text = item.get('answer')
        created_at = item.get('created_at')
        if question_exists(service_id):
            item = get_unique_question()
            service_id = item.get('id')
            question_text = item.get('question')
            answer_text = item.get('answer')
            created_at = item.get('created_at')
        set_question(service_id, question_text, answer_text, created_at)

    return last_question if last_question else JSONResponse(
        content={},
        status_code=200
    )
