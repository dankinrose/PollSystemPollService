from typing import List, Set

from fastapi import HTTPException, status

from model.answer import Answer
from model.answer_response import AnswerResponse
from model.question_stats_response import QuestionStatsResponse
from model.question_total_response import QuestionTotalResponse
from model.user_answers_summary_response import UserAnswersSummaryResponse
from model.user_total_questions_response import UserTotalQuestionsResponse
from repository import answer_repository, question_repository



async def _build_answer_response(answer: Answer) -> AnswerResponse:
    question = await question_repository.get_question_by_id(answer.question_id)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {answer.question_id} not found",
        )

    if answer.selected_option == 1:
        option_text = question.option_1
    elif answer.selected_option == 2:
        option_text = question.option_2
    elif answer.selected_option == 3:
        option_text = question.option_3
    else:
        option_text = question.option_4

    return AnswerResponse(
        question_id=question.id,
        question_title=question.title,
        selected_option=answer.selected_option,
        selected_option_text=option_text,
    )


# ------------------------------------------------------------------------------------------
# By passing the user id Return the user answer to each question he submitted

async def get_user_answers_summary(user_id: int) -> UserAnswersSummaryResponse:
    answers = await answer_repository.get_answers_by_user(user_id)
    answer_responses = [await _build_answer_response(a) for a in answers]

    return UserAnswersSummaryResponse(
        user_id=user_id,
        answers=answer_responses,
    )


# --------------------------------------------------------------------------------------------
# By passing the user id Return how many questions this user answered to in total

async def get_user_total_questions(user_id: int) -> UserTotalQuestionsResponse:
    answers = await answer_repository.get_answers_by_user(user_id)
    question_ids: Set[int] = {a.question_id for a in answers}

    return UserTotalQuestionsResponse(
        user_id=user_id,
        total_questions_answered=len(question_ids),
    )


# --------------------------------------------------------------------------------------
# By passing the question id Return how many users choose each of the question options

async def get_question_stats(question_id: int) -> QuestionStatsResponse:
    question = await question_repository.get_question_by_id(question_id)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question with id {question_id} not found",
        )

    answers = await answer_repository.get_answers_by_question(question_id)

    option_1_count = option_2_count = option_3_count = option_4_count = 0

    for ans in answers:
        if ans.selected_option == 1:
            option_1_count += 1
        elif ans.selected_option == 2:
            option_2_count += 1
        elif ans.selected_option == 3:
            option_3_count += 1
        elif ans.selected_option == 4:
            option_4_count += 1

    return QuestionStatsResponse(
        question_id=question.id,
        question_title=question.title,
        option_1=question.option_1,
        option_2=question.option_2,
        option_3=question.option_3,
        option_4=question.option_4,
        option_1_count=option_1_count,
        option_2_count=option_2_count,
        option_3_count=option_3_count,
        option_4_count=option_4_count,
    )


# ----------------------------------------------------------------------------------------
# By passing the question id Return how many users answer to this question in total

async def get_question_total_answers(question_id: int) -> QuestionTotalResponse:
    answers = await answer_repository.get_answers_by_question(question_id)
    total = len(answers)

    return QuestionTotalResponse(
        question_id=question_id,
        total_answers=total,
    )


# -------------------------------------------------------------------------------------------------
# Return all questions and all possible options and for each question return how many users choose each of the question options

async def get_all_questions_stats() -> List[QuestionStatsResponse]:
    questions = await question_repository.get_all_questions()
    result: List[QuestionStatsResponse] = []

    for q in questions:
        stats = await get_question_stats(q.id)
        result.append(stats)

    return result
