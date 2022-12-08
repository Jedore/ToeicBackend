from fastapi import APIRouter

from .api import auth

router = APIRouter(prefix='/wechat', tags=['WeChat'])
router.include_router(auth.router)
