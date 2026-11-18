from fastapi import APIRouter, Query
from .schema import chat_payload
from . import service
from core.database import sqlite
from fastapi import HTTPException


ai_agent_router = APIRouter(prefix="/ai")



@ai_agent_router.post("/chat")
def initiate_chat(payload: chat_payload):
    answer = service.chat(payload.query, payload.session_id)
    return {"session_id": payload.session_id, "answer": answer}

@ai_agent_router.get("/history")
def get_history(session_id: str | None = Query(default=None, max_length=200)):
    if session_id is None:
        return {"sessions": service.get_all_history()}
    if not session_id.strip():
        return {"detail": "session_id cannot be empty"}
    return {
        "session_id": session_id, 
        "messages": service.get_history(session_id)
    }


@ai_agent_router.delete("/history/{session_id}")
def delete_history(session_id: str):
    if not session_id.strip() or len(session_id) > 200:
        raise HTTPException(status_code=400, detail="Session_id is required")
    deleted_count = sqlite.delete_session_messages(session_id)
    return {"session_id": session_id, "deleted": deleted_count > 0}

# @ai_agent_router.get("/history")
# def get_all_history():
#     return { 
#         "messages": service.get_history()
#     }
