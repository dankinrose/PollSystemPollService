from typing import List
from pydantic import BaseModel

from model.answer_response import AnswerResponse


class UserAnswersSummaryResponse(BaseModel):
    user_id: int
    answers: List[AnswerResponse]

