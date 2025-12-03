from pydantic import BaseModel


class UserTotalQuestionsResponse(BaseModel):
    user_id: int
    total_questions_answered: int

