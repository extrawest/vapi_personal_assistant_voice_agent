from pydantic import BaseModel


class MemoryRecallArgs(BaseModel):
    query: str
    namespace: str = "default"


class MemoryRememberArgs(BaseModel):
    content: str
    namespace: str = "default"
