from pydantic import BaseModel

class ContextRequest(BaseModel):
    context: str

class DescriptionResponse(BaseModel):
    prompt: str

class CacheRequest(BaseModel):
    id: str

class CacheListResponse(BaseModel):
    descriptions: dict

class ContextRequest(BaseModel):
    context: str