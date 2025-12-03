from typing import List

from fastapi import APIRouter

from model.question_stats_response import QuestionStatsResponse
from model.question_total_response import QuestionTotalResponse
from model.user_answers_summary_response import UserAnswersSummaryResponse
from model.user_total_questions_response import UserTotalQuestionsResponse
from service import answer_stats_service

router = APIRouter(
    prefix="/answer_stats",
    tags=["answer_stats"],
)


# By passing the question id- how many users choose each of the question options
@router.get("/question/{question_id}/options", response_model=QuestionStatsResponse)
async def get_question_options_stats(question_id: int) -> QuestionStatsResponse:
    return await answer_stats_service.get_question_stats(question_id)


# By passing the question id- how many users answer to this question in total
@router.get("/question/{question_id}/total", response_model=QuestionTotalResponse)
async def get_question_total_answers(question_id: int) -> QuestionTotalResponse:
    return await answer_stats_service.get_question_total_answers(question_id)


# By passing the user id- Return the user answer to each question he submitted
@router.get("/user/{user_id}/answers", response_model=UserAnswersSummaryResponse)
async def get_user_answers_summary(user_id: int) -> UserAnswersSummaryResponse:
    return await answer_stats_service.get_user_answers_summary(user_id)


# By passing the user id- Return how many questions this user answered to in total
@router.get("/user/{user_id}/total", response_model=UserTotalQuestionsResponse)
async def get_user_total_questions(user_id: int) -> UserTotalQuestionsResponse:
    return await answer_stats_service.get_user_total_questions(user_id)


# Return all questions + options + how many chose each option
@router.get("/all_questions", response_model=List[QuestionStatsResponse])
async def get_all_questions_stats() -> List[QuestionStatsResponse]:
    return await answer_stats_service.get_all_questions_stats()
