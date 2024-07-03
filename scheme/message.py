from time import time
from pydantic import BaseModel


class MessageRequest(BaseModel):
    raw: str


class MessageAccepted(BaseModel):
    timestamp: int = int(round(time() * 1000))


class QueueSize(BaseModel):
    amount: int