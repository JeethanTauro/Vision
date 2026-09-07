from session_model import *
from datetime import datetime
from sqlmodel import Session, select
from memory import get_engine


#memory_save
def memory_save(content: str, source: str, importance: float):
    created_at = datetime.now()

    session_memory = Session_memory(
        content=content,
        source=source,
        importance=importance,
        created_at=created_at,
        updated_at=created_at
    )

    with Session(get_engine()) as session:
        session.add(session_memory)
        session.commit()
        session.refresh(session_memory)

    return session_memory

#memory_delete
def memory_delete(id: int):
    with Session(get_engine()) as session:
        statement = select(Session_memory).where(
            Session_memory.id == id
        )

        memory = session.exec(statement).first()

        if memory is None:
            return False

        session.delete(memory)
        session.commit()

        return True

#memory_get
def memory_get(id: int):
    with Session(get_engine()) as session:
        statement = select(Session_memory).where(
            Session_memory.id == id
        )

        memory = session.exec(statement).first()

        if memory is None:
            return None

        memory.last_used = datetime.now()
        session.add(memory)
        session.commit()
        session.refresh(memory)

        return memory

#memory_search
def memory_search(query: str):
    with Session(get_engine()) as session:
        statement = (
            select(Session_memory)
            .where(Session_memory.content.contains(query))
            .order_by(Session_memory.importance.desc())
        )

        return session.exec(statement).all()


#memory_update
def memory_update(
    id: int,
    content: str | None = None,
    importance: float | None = None
):
    with Session(get_engine()) as session:
        statement = select(Session_memory).where(
            Session_memory.id == id
        )

        memory = session.exec(statement).first()

        if memory is None:
            return None

        if content is not None:
            memory.content = content

        if importance is not None:
            memory.importance = importance

        memory.updated_at = datetime.now()

        session.add(memory)
        session.commit()
        session.refresh(memory)

        return memory