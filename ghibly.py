from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Movie(BaseModel):
    id: str
    title: str
    original_title: str
    original_title_romanised: str
    image: str
    movie_banner: str
    description: str
    director: str
    producer: str
    release_date: str
    running_time: str
    rt_score: str
    people: List[str]
    species: List[str]
    locations: List[str]
    vehicles: List[str]
    url: str


class Model(BaseModel):
    __root__: List[Movie]
