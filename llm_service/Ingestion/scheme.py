from pydantic import BaseModel
from typing import List, Optional


class Benefit(BaseModel):
    title: str
    description: str


class Eligibility(BaseModel):
    requirement: str


class Document(BaseModel):
    name: str
    mandatory: Optional[bool] = None
    description: Optional[str] = None


class ApplicationStep(BaseModel):
    step: int
    description: str


class Source(BaseModel):
    url: str
    authority: Optional[str] = None
    last_updated: Optional[str] = None


class Scheme(BaseModel):
    name: str
    description: str

    authority: Optional[str] = None
    state: Optional[str] = None

    benefits: List[Benefit]
    eligibility: List[Eligibility]
    documents: List[Document]
    application_process: List[ApplicationStep]

    source: Source