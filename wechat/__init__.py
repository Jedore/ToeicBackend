from fastapi import APIRouter

from .api import auth, day19

router = APIRouter(prefix='/wechat', tags=['WeChat'])
router.include_router(auth.router)
router.include_router(day19.router)
