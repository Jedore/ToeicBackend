from fastapi import APIRouter

from wechat.model import day19

router = APIRouter(prefix='/day19', tags=['Day19'])


@router.get('', response_model=day19.Day19Rsp)
def get():
    data = [{'id': 1, 'name': 'day 1'}, {'id': 2, 'name': 'day2'}]
    return day19.Day19Rsp(data=data)
