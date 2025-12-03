from pydantic import BaseModel


class AnswerResponse(BaseModel):
    question_id: int
    question_title: str
    selected_option: int
    selected_option_text: str