from fastapi import FastAPI
from requests import get

from .app_serializers import ValueInput


app = FastAPI()


@app.post('/question')
async def main_page(value: ValueInput):
    url = f'https://jservice.io/api/random?count={value.questions_num}'
    response = get(url)
    print(response)
    data = response.json()
    for item in data:
        print(item)

    return {'message': 'Hello World'}
