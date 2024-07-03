from fastapi import FastAPI, status

from scheme.message import (
    MessageRequest,
    MessageAccepted,
    QueueSize
)
from priority_queue import queue

application = FastAPI()


@application.get(
    path="/health",
    status_code=status.HTTP_200_OK
)
async def health():
    return {"status": "healthy"}

@application.post(
    path="/messages",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=MessageAccepted
)
async def publsih_message(request: MessageRequest):
    queue.enqueue(message=request.raw)
    return MessageAccepted


@application.get(
    path="/messages",
    status_code=status.HTTP_200_OK,
    response_model=QueueSize
)
async def current_size():
    return QueueSize(amount=queue.size())