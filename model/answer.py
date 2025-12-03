from typing import Optional
from pydantic import BaseModel, Field

class Answer(BaseModel):
    id: Optional[int] = None
    user_id: int
    question_id: int
    selected_option: int = Field(..., ge=1, le=4)