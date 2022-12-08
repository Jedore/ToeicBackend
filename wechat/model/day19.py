import typing

from sqlmodel import SQLModel, Field

from model import Rsp


class Day19(SQLModel):
    id: str
    name: str


class Day19Rsp(Rsp):
    data: typing.List[Day19] = Field([])
