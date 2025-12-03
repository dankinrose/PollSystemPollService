from pydantic import BaseModel


class QuestionTotalResponse(BaseModel):
    question_id: int
    total_answers: int
