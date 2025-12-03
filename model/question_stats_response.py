from pydantic import BaseModel


class QuestionStatsResponse(BaseModel):
    question_id: int
    question_title: str

    option_1: str
    option_2: str
    option_3: str
    option_4: str

    option_1_count: int
    option_2_count: int
    option_3_count: int
    option_4_count: int