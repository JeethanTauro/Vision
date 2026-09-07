from sqlmodel import Field,SQLModel
from datetime import datetime

class Session_memory(SQLModel, table=True):
    id : int |  None = Field(default=None, primary_key=True)
    content : str
    source : str   #(CONVERSATION, NOTION, GITHUB)
    created_at : datetime 
    updated_at : datetime
    last_used : datetime | None=None
    importance :  float  #0-1

    
