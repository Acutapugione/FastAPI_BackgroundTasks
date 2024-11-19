from typing import Annotated
from fastapi import APIRouter, Request, Query, Body, Path, Header, Depends
from pydantic import BaseModel, Field

prod = APIRouter(prefix="/prod", tags=["prod"])


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)


@prod.get("/")
def items(
    filtered: Annotated[FilterParams, Query()],
    x_cli: Annotated[str, Header()],
    # skip: int | None = None,
    # step: int = 1,
    # limit: int | None = None,
):
    print(f"{x_cli=}")
    return filtered
    return [x for x in range(0 + skip, limit, step)]
